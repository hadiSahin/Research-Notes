### BERToD: An automated BER testing framework to detect packet QoS Failures at AmLight

This project aims to create an automated testing tool to check all possible links on Amlight network for QoS failures such as frame loss, jitter, out-of-sequence packets, and latency. In its final version, the tool will gather data from Netbox about network policies, from BAPM test reports, from Kytso-ng about the network topology, and send testing packets using EXFO NetBlazer. The goal is to observe failures in the network, to isolate the link that causes the problem, to identify the issue, and to remedy the problem. The test will run continuously and evaluate the network status to proactively address potential issues. See below figure for the visualization of the BertoD tool.

<img src="./images/BERToD.png" alt="BERToD - Bit Error Rate Test on Demand" width="500">

We sent packets using the EXFO NetBlazer and measured the following:

- Failures: Jitter, latency, out-of-sequence packets, and frame loss
- Packet Properties:
  - Frame size: Mixed (68, 256, 512, 10124, 1518) or fixed (9000) bytes
  - Duration
  - Number of packets sent

### January 9, 2025

The test from BERToD produced over 400,000 rows of data, including the frame size (68, 256, 512, 1024, 1518, 9000 bytes), the duration of each test run, and the total number of frames/packets sent. I also incorporated data for all the links through which the test packets were sent. For example, a link between VLANs 410 and 416 is labeled as "410_416" and is coded as 1 if the packets pass through this link and 0 otherwise. I first mapped all the network links as a tree (see the figure below). Then, I ran logistic regression and Neural Network ML models, using failures as the outcome variable and all other variables, including the links, as features.

<img src="./images/network_tree.png" alt="Network tree" width="1200">

### February 12, 2025

We read the network topology using EVC from Kytos-ng and combined it with test results obtained from the EXFO NetBlazer. We utilize statistical models and machine learning to identify the links responsible for failures.
