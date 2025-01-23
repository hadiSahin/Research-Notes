### BERToD: An automated BER testing framework to detect packet QoS Failures at AmLight

This project aims to create an automated testing tool to check all possible links on Amlight network for QoS failures such as frame loss, jitter, out-of-sequence packets, and latency. In its final version, the tool will gather data from Netbox about network policies, from BAPM test reports, from Kytso-ng about the network topology, and send testing packets using EXFO NetBlazer. The goal is to observe failures in the network, to isolate the link that causes the problem, to identify the issue, and to remedy the problem. The test will run continuously and evaluate the network status to proactively address potential issues. See below figure for the visualization of the BertoD tool.

<img src="./images/BERToD.png" alt="BERToD - Bit Error Rate Test on Demand" width="500">


### January 9, 2025

The test from BERToD produce more 400K of rows of data which includes the frame size (68, 256, 512, 1024, 1518, 9000 bytes), duration of each test run, and total number pf frames/packets sent. I also added this data all links that the test packets are send. For instance, a link between VLAns 410-416 is labeled as "410_416", and codes as 1 when the packets send passes from this link and 0 otherwise. I first all network links as a tree (See the figure below), then I run logistic regression and Neural Network ML models using the failures as the outcome and all other variables including the links as the features. 

<img src="./images/network_tree.png" alt="Network tree" width="800">