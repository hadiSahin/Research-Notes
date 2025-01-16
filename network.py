import math
import networkx as nx
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from plotly.express.colors import sample_colorscale
from networkx.drawing.nx_pydot import graphviz_layout

# Create the graph
G = nx.DiGraph()
G.add_edges_from([(401, 402), (402, "sw14"), ("sw14", 430)])
G.add_edges_from([(402, 428), (428, "jax-sw01"), ("jax-sw01", 415)])
G.add_edges_from([(402, 411), (411, 414)])
G.add_edges_from([(402, 411), (411, 417), (417, 420)])
G.add_edges_from([(402, 425), (425, 427)])
G.add_edges_from([(401, 424), (424, 410), (410, 416), (416, "sao-sw04-p3"), ("sao-sw04-p3", 405)])
G.add_edges_from([(416, "sao-sw04-p31"), ("sao-sw04-p31", 419)])
G.add_edges_from([(424, 413)])
G.add_edges_from([(424, 429), (429, 412)])
G.add_edges_from([(429, "sw10"), ("sw10", 418)])
G.add_edges_from([("sw10", "pty-sw01-p6"), ("pty-sw01-p6", 423)])
G.add_edges_from([(424, 422), (422, "sju-sw03"), ("sju-sw03", "pty-sw01-p1"), ("pty-sw01-p1", 421), (421, 406)])

# Compute node positions using a directed graph layout
pos = graphviz_layout(G, prog="dot")  # Use dot layout for directed graphs
for node, position in pos.items():
    G.nodes[node]['pos'] = position

# Compute edge usage
def compute_edge_usage(graph, target_nodes):
    edge_usage = {}
    visited_nodes = set()

    def dfs(node):
        if node in visited_nodes:
            return
        visited_nodes.add(node)
        for predecessor in graph.predecessors(node):
            edge = (predecessor, node)
            edge_usage[edge] = edge_usage.get(edge, 0) + 1
            dfs(predecessor)

    for target in target_nodes:
        visited_nodes.clear()
        dfs(target)

    return edge_usage

# Load and filter data
data = pd.read_csv("data/traffic_eng01.csv")
data01 = data[~(data['VLAN'].astype(str).str.startswith('5') | (data['VLAN'] == 309))]
data01 = data01[~((data01['year'] == 2024) & (data01['month'] < 9))]

# Filter function for month and day
def filter_failed(df, measure):
    return df[df[measure] == 1]

# Dash app setup
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div([
        html.Label("Failure Type:"),
        dcc.Dropdown(
            id='measure-dropdown',
            options=[
                {'label': 'Jitter', 'value': 'jitter'},
                {'label': 'Latency', 'value': 'latency'},
                {'label': 'Out of Sequence', 'value': 'out_of_sequence'},
                {'label': 'Frame Loss', 'value': 'frame_loss'}
            ],
            value='jitter'
        ),
        html.Label("VLAN:"),
        dcc.Dropdown(
            id='vlan-dropdown',
            options=[{'label': 'All', 'value': 'All'}] + [{'label': vlan, 'value': vlan} for vlan in sorted(data01['VLAN'].unique())],
            value=['All'],
            multi=True
        ),
        html.Label("Year:"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': 'All', 'value': 'All'}] + [{'label': str(year), 'value': year} for year in sorted(data01['year'].unique())],
            value='All',
            multi=False
        ),
        html.Label("Month:"),
        dcc.Dropdown(
            id='month-dropdown',
            options=[{'label': 'All', 'value': 'All'}] + [{'label': str(month), 'value': month} for month in range(1, 13)],
            value='All',
            multi=True
        ),
    ], style={'width': '17%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    html.Div([
        dcc.Graph(id='network-graph', style={'height': '800px'})
    ], style={'width': '80%', 'display': 'inline-block'}),
])

# Callback to update graph
@app.callback(
    Output('network-graph', 'figure'),
    Input('measure-dropdown', 'value'),
    Input('vlan-dropdown', 'value'),
    Input('year-dropdown', 'value'),
    Input('month-dropdown', 'value')
)
def update_graph(measure, vlans, year, month):
    filtered_data = data01
    if vlans and 'All' not in vlans:
        filtered_data = filtered_data[filtered_data['VLAN'].isin(vlans)]
    if year != 'All':
        filtered_data = filtered_data[filtered_data['year'] == year]
    if month != 'All':
        filtered_data = filtered_data[filtered_data['month'] == month]

    failed_df = filter_failed(filtered_data, measure)
    failed_nodes = set(failed_df['VLAN'])
    failed_edge_usage = compute_edge_usage(G, failed_df['VLAN'])
    all_edge_usage = compute_edge_usage(G, filtered_data['VLAN'])

    # Compute failure ratios
    failure_ratios = {
        edge: failed_edge_usage.get(edge, 0) / all_edge_usage.get(edge, 1)
        for edge in G.edges
    }

    # Compute edge labels: "failure_usage/total_usage"
    edge_labels = {
        edge: f"{failed_edge_usage.get(edge, 0)}/{all_edge_usage.get(edge, 0)}"
        for edge in G.edges
    }

    # Normalize failure ratios and map to colors
    max_ratio = max(failure_ratios.values(), default=1)
    normalized_ratios = [ratio / max_ratio if max_ratio > 0 else 1 for ratio in failure_ratios.values()]
    edge_colors = sample_colorscale("sunsetdark", normalized_ratios, low=0, high=1)

    # Plot edges
    edge_traces = []
    for edge, color in zip(G.edges, edge_colors):
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_trace = go.Scatter(
            x=[x0, x1, None], y=[y0, y1, None],
            line=dict(width=2, color=color),
            mode='lines'
        )
        edge_traces.append(edge_trace)

    # Plot nodes
    node_x = [G.nodes[node]['pos'][0] for node in G.nodes]
    node_y = [G.nodes[node]['pos'][1] for node in G.nodes]
    node_color = ['red' if node in failed_nodes else 'lightblue' for node in G.nodes]

    # Add node labels
    node_text = [str(node) for node in G.nodes]

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            color=node_color,
            size=10
        ),
        text=node_text,
        textposition='top left'
    )

    # Create edge annotations for labels
    annotations = []
    for edge, label in edge_labels.items():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        annotations.append(
            dict(
                x=(x0 + x1) / 2 +15,
                y=(y0 + y1) / 2 +4,
                text=label,
                showarrow=False,
                font=dict(size=10, color="black"),
                align="center"
            )
        )

    # Combine all traces
    fig = go.Figure(data=edge_traces + [node_trace])
    fig.update_layout(showlegend=False, annotations=annotations)

    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
