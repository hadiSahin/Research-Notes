Rebuttal to Reviewer Comments: Survival of the Poor: Incentivizing Decentralization to Strengthen PoS Blockchain Consensus Security
===================================================================================================================================

First of all, we thank the reviewers for their valuable feedback. This feedback, along with our efforts to address it, will significantly contribute to our research. Below, we address the concerns and provide point-by-point responses to the comments.
==========================================================================================================================================================================================================================================================

**Responses to Reviewer 1:**

**R1:** I do not think that the redistribution of the stake is a solution that stakers will approve of. It is very theoretical and has no practical user-based view.

Response: We agree that permanently changing users' stakes is unacceptable. However, in our case, we do not alter users' stakes or their distribution. We only adjust stake weights for the selection process. Instead of using actual stake weights, we modify them to give lower-stakeholders a greater chance of being selected, while higher-stake holders still retain a higher probability. In summary, while we adjust stake weights for selection, we do not change users' actual stake holdings.

**R1:** I understand that the reputation aims at counteracting the problems introduced by the stake redistribution, but I do not think stakers will agree to this process.

**Response:** It is quite possible that users in an established blockchain would resist any change if it does not benefit them. However, proposed mechanisms such as Proof of Reputation (PoR) utilize reputation scores in the consensus process. And there are several works that explicitly or partially propose using reputation scores in the consensus process.

**R1:** Why is the obtained reward not studied? This is what stakers will care for.

**Response:** We focus on the distribution of stakes, as our research emphasizes the decentralization of blockchain for security and resilience. However, "obtained reward" is a key component of our argument. In the "Economics of Node Participation" and "Economics of Node Splitting" subsections of Section IV: Proposed Incentive Mechanism, we examine how individual users decide whether to participate in the consensus process or split their stakes into multiple wallets based on their potential earnings in current and future rounds.

Our incentive mechanism aims to encourage both low-stake and high-stake participants in the blockchain. As discussed and demonstrated in these sections, users will not continue participating unless they are properly incentivized with rewards. Ultimately, the obtained rewards and their likelihood are the sole determinants of participation.

**R1:** Does Fig. 1 show a distribution fitted to empirical data? Why is not the

same Gini coefficient for simulated data used as it is observed for real data?

**Response:** Figure 1 shows the initial distribution of stakes in our simulation. This distribution was created and assigned to the nodes. To simulate a real-world scenario, we used a Pareto distribution because stake distributions are quite skewed in blockchains. We also ran simulations with normal and uniform initial distributions to assess how our proposed mechanism performs in a more equal stake distribution setting. We observed similar patterns but, due to page limits, we chose to report the results using the Pareto distribution, as real-world stake distributions tend to be highly unequal. In the revised version, we will include a brief discussion on how our proposed mechanism affects inequality under different initial distributions.

**R1:** The comparison of reward distribution methods with stake distribution seems to compare apples and oranges. Why are those the same? Which staker would choose the stake redistribution instead of the reward distributions?

**Response:** We do not compare reward distribution to stake distribution. In fact, we provide no analysis of reward distribution in the paper. We study how each reward mechanism affects the distribution of stakes in the blockchain. We show that the current mechanisms increase inequality except Algorand which maintains the status quo. Our proposed mechanism decreases inequality.

We are interested in the distribution of stakes for blockchain's decentralization, which is paramount for its security and stability. In this context, rewards are important and related to stake distribution/decentralization as they are added to the wallet of the block proposer, which changes the distribution of stakes leading either to more wealth for the rich or providing a more equal and healthy distribution.

Individual users should care about the stake distribution if they have a long-term interest in the blockchain. Most users typically are not concerned with this, however, they will care if their reward earning probability becomes extremely low. They will be unhappy from round to round as they do not receive any participation rewards, while their share of stakes diminishes with the addition of reward money each period. Their stake values will become diluted and less valuable due to inflationary pressures. However, we do not assume individual users will make sophisticated calculations; however as rational actors, they will quickly realize the incentive mechanism is not benefiting them.

**Responses to Reviewer 2:**

**R2:** The analysis is not particularly rigorous. In my view,  it would benefit from providing some theoretical foundations and formal proofs for the properties of the proposed mechanism.

Response: In the original version of the paper, we included an analytical proof section and a game theory section that examined users' choices, actions, and the equilibrium outcome. However, we removed these sections due to page limits. In the revised version, we will add them as an appendix if permitted; otherwise, we will provide a succinct analytical proof.

Responses to Reviewer 3:

**R3:** The proposed FB mechanism relies heavily on the use of a reputation scheme. Indeed, it is highly vulnerable to Sybil attacks. The proposed solution for this is the introduction of a reputation scheme. It is not clear from the - just two - references cited whether a reputation scheme for PoS consensus that has the properties used in the FB mechanism (such as the reputation being an increasing function of time) is feasible. The related work does not mention any paper on reputation schemes. As a reader, the introduction of this ideal "solution" comes out of the blue, and I am not convinced from reading the paper that this is a feasible solution.

Response: We acknowledge that our discussion of the reputation literature is quite limited. Our focus is on using reputation scores to screen out newly created nodes in the first step of selection, as some of these could be Sybil nodes. We do not focus on reputation mechanisms per se; a fully developed reputation mechanism could include factors such as prior participation, good behavior (e.g., not voting on forks or rejected transactions, consistent voting, etc.), and even peer voting to help promote honest nodes. A well-designed reputation mechanism can enhance blockchain security and discourage dishonest behavior, such as the creation of Sybil nodes.

However, in this paper, we propose a basic, automatically increasing reputation score to support our incentive mechanism. We intentionally kept this aspect simple to avoid complicating the discussion with an extensive review of reputation mechanisms in the literature. More importantly, simulating a fully defined reputation mechanism is highly challenging, as it would require incorporating dishonest behavior within the simulation framework. For this reason, we kept the reputation mechanism minimal in our simulation. However, for real-world implementation, we advocate for a fully developed reputation mechanism instead of the simplified version used here.

In the revised version, we will further clarify this point and suggest ways to develop a reputation mechanism based on the literature.

**R3:** Let us assume for now that the reputation scheme could be set up to work as described in the paper. It seems to me that the FB mechanism is a temporary fix. For the number of rounds .N. large enough, and for .d=0., the expected reputation score will come arbitrarily close to 1. At that point, an adversary consisting of small child nodes will definitely earn more than an adversary consisting of one large node. Thus, for large enough .N., and for .d=0., adversaries will always be incentivized to split. At that point, everyone will be below the taxation threshold and FB reduces to the standard PoS reward mechanism. The only thing keeping that from happening is having .d>0.. I feel the paper should provide a relation between .N. and .d. in order to indicate when the FB mechanism has a beneficial effect. Even then, it could be argued that one can always find an adversary with a low enough time preference (a small enough .d.) for whom it would be worthwhile splitting. Please indicate whether this reasoning is flawed, but if it is not the paper should mention that the FB mechanism is only a temporary fix, and depends heavily on the choice of .d., which limits the proposed solution's relevance.

**Response:** It is correct that a dedicated dishonest node with no time preference could decide to keep a Sybil node or multiple of them. I would mention a few points that would support the paper's claim, but that does not totally argue against the reviewer's point.

First, in our proposed mechanism it is never rational for a node to create a Sybil node if it focuses on the current time, as the reputation score of a new node starts with 0. But nodes can focus on long-term and consider the times when a Sybil node builds enough reputation. Therefore, we introduced expected reputation, where the value of reputation is 0.1% less in the future. We show that in 5000 rounds, and possibly for further rounds, creating Sybil nodes never becomes profitable, especially given that they reduce their selection probability by slashing their main wallet. This decay value is quite low and will discourage many users. However, blockchain founders can use other methods, such as reputation decay (which is proposed in the literature to benefit newcomers) to prolong this time horizon.

Second, we use a very basic automatically increasing reputation score. But in the implementation, we envision a fully developed one in which reputation building is not straightforward and would entail constant good behavior. This would deter dishonest behavior further.

Third, in an earlier version of the paper, we discussed the costs of keeping multiple nodes for a long time, also introducing a punishment, even with a low probability of being caught, as extra precautions. We decided to keep them out to simplify the focus of the paper and due to page limits.

Finally, theoretically there are still going to be nodes that pursue this path. We expect that this number will be low and will not significantly harm the blockchain as long as they remain a few.

In the revised version, we will discuss the limitation of our proposed mechanism in this context and add a discussion on how these limitations could be addressed in real-life implementation.

**R3:** .s*. in the text just above (4) should be .s^*.,

Response: We will correct the typo in the revised version

**R3:** .N. is used first for number of nodes and then number of rounds, maybe use different symbols.

Response: Thank you for point this out, we will correct them in the revised version.

**R3:** In (5), .n. should be .k.?

Response: n is the current round number, and k is the minimum number of times a user must be selected as a block proposer to break even with their initial investment.

**R3:** Just before (9), it is mentioned that .\mathbb{E}[Rep]. is used to calculate .q_1., maybe elaborate a bit more; I suspect it replaces .r_i. in (4)?

**Response:** Yes, that is correct. For a newly created node or a Sybil node, the reputation score starts at 0 and gradually increases over time. If we only consider the current time, a user would have no incentive to create a Sybil node. However, this assumption is incorrect, as users often consider long-term benefits.

Rather than focusing solely on the short-term impact of a low reputation, users may evaluate what their reputation could be in the future. However, they will also prefer to receive rewards sooner rather than later---for example, today rather than in the 500th round. This introduces the need for a decay rate to account for the decreasing value of future rewards.

Taking all these factors into account, we calculate the expected reputation for a user over 5,000 rounds.

**R3:** Specify the parameters of the normal distribution for the reputation scores.

Response: We use a mean value of 0 and a standard deviation of 5. Then, we scale the values to ensure they all remain below 1. We will add this information to the revised version.

R3: In (5), .n. should be .k.?

Response: n is the current round number, and k is the minimum number of times a user must be selected as a block proposer to break even with their initial investment.

R3: Is there any justification from the literature why the sigmoid function would be appropriate to model the evolution of the reputation score?

Response: Our goal in using the sigmoid function is to select a distribution that slopes more gradually at the beginning and the end. The purpose of this design is to prevent new Sybil nodes from acquiring reputation too quickly.

The literature on reputation mechanisms generally does not include an automatically increasing function. However, there are a few papers that utilize an automatically increasing reputation system with a sigmoid function (Jiangshan et al., 2019; Qingcheng). These papers have differing justification for using sigmoid function. We will add citations to this paper in our revised version:

Yu, Jiangshan, David Kozhaya, Jeremie Decouchant, and Paulo Esteves-Verissimo. "Repucoin: Your reputation is your power." IEEE Transactions on Computers 68, no. 8 (2019): 1225-1237.

Li, Qingcheng, Heng Cao, Shengkui Wang, and Xiaolin Zhao. "A reputation-based multi-user task selection incentive mechanism for crowdsensing." IEEE Access 8 (2020): 74887-74900.

R3: Can nodes only split once? Or can they keep splitting?

Response: We allow only 30% of the nodes to split in a given round for visualization purposes. Otherwise, nodes can split as many times as they deem rational. We will clarify this in the revised version.

R3: Table I: What happens in between round 1 and round 5000? Could it be that some nodes split and other nodes stop participating in the network because they are no longer incentivized to participate? Maybe show a figure instead, or say it is constant the whole time?

Response: Thank you for pointing this out. We failed to mention in the paper that, in order to track Sybil behavior, we disabled the ability of nodes to drop out of participation. If this had been allowed, many Sybil nodes would have likely dropped out due to their low stakes and low reputation, making them harder to track. We will clarify this point in the revised version.
