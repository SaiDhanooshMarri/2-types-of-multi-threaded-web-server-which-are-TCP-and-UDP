# 2-types-of-multi-threaded-web-server-which-are-TCP-and-UDP
Implemented 2 types of multi-threaded web server which are TCP and UDP, we have selected a performance metric for evaluating. We have used that to evaluate a performance metric for both. We have used multi-threading concept for evaluation.

TCP:
TCP stands for Transmission Control Protocol. It is mainly used for establishing and connecting environment from client to server. Most of the protocols which wants to transfer high level data, uses this TCP. TCP is therefore in charge of carrying and routing data via the network architecture and ensuring that it reaches the IP-defined target application or device.
TCP, being a connection-based protocol, creates and maintains a connection between applications or devices until they complete exchanging data. It decides how the original message should be divided into packets, numbers and reassembles the packets, and transmits them to other network devices such as routers, security gateways, and switches before forwarding them to their destination. TCP also transmits and receives packets from the network layer, handles the transmission of any missed packets, performs flow control, and guarantees that all packets reach their destination.
UDP:
UDP, or User Datagram Protocol, is a lightweight and connectionless transport protocol that is part of the Internet Protocol (IP) family, along with TCP (Transmission Control Protocol). Not like TCP, UDP doesn't require a connection before delivering data and does not offer the same level of dependability or error correction. Instead, UDP provides a more straightforward, best-effort, and low-overhead approach to data delivery.
In simple terms, TCP prioritizes dependable, precise data transfer over speed. UDP, on the other hand, emphasizes speed and does not give any guarantees for packet sequencing or transmission.

implemented 2 types of multi-threaded web server which are TCP and UDP, we have selected a performance metric for evaluating. We have used that to evaluate a performance metric for both. We have used multi-threading concept for evaluation. Finally, we did analysis on this performance metric to determine both TCP and UDP based multi-threaded servers. Time taken by client side for getting the number of occurences




Steps to execute the Assignment2 UDP
1. Run thhe UDP server file it runs on the localhost with port 8080 make sure these are not in use or can change them to the host and port which are available
2. Run the UDPclient file it automatically requests the image from S_files folder as server files and get the requested image saves in the C_files folder as client files.
3. This code uses multi threading we can change the number of occurence in the code to different values.(variable-->nscsrd)
4. It will show the time execution of all the occurences.

Steps to execute the Assignment2 TCP
1. Run thhe TCP server file it runs on the localhost with port 8080 make sure these are not in use or can change them to the host and port which are available
2. Run the TCPclient file it automatically requests the image from S_files folder as server files and get the requested image saves in the C_files folder as client files.
3. This code uses multi threading we can change the number of occurence in the code to different values.(variable-->nscsrd).
4. It will show the time execution of all the occurences.

