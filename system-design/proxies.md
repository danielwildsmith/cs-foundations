# Proxies
Proxies are intermediary servers in between the client and the destination server, forwarding requests/responses.

## Forward Proxy
The role of a forward proxy is to send a request on the client's behalf, hiding their identity (IP) from the destination server. An example is a VPN. Instead of using your IP address, the forward proxy uses its own, providing privacy. Another example is a company proxy, where they can disallow any requests made to certain locations (e.g. YouTube). Forward proxies can allow control over network traffic in this way. They can also cache common user requests, increasing efficiency. A helpful analogy is needing to send a letter to someone but want it to be anonymously delivered, so you ask a friend to deliver it for you. 

![Forward Proxy](./images/forward-proxy.avif)

## Reverse Proxy
A reverse proxy anonymizes the destination server instead of the client. It receives requests from clients and forwards them to the appropriate server. The key benefit of a reverse proxy is its ability to protect servers by managing incoming requests and distributing the load across multiple servers. It can also safeguard against DDoS attacks by serving as a shield for the actual destination servers. An example is a CDN. Instead of clients directly accessing the origin server, the reverse proxy (CDN) handles the requests. If the requested content is available, the reverse proxy serves it directly to the client, reducing latency and alleviating the load on the origin server.

![Reverse Proxy](./images/reverse-proxy.avif)

### Load Balancers
Another main type of reverse proxy is a load balancer. Typically used with horizontally scaled server systems, load balancers use a variety of strategies to efficiently distribute incoming network requests. 

- **Round Robin**
    - Pros: simple, distributes requests in a balanced manner
    - Cons: assumes all servers can handle an equivalent workload
- **Weighted Round Robin**
    - Pros: accounts for servers having different computational powers
    - Cons: what if one request takes much longer than others? 
- **Least Number of Connections**
    - Pros: accounts for requests taking different amounts of time
- **User Location**
    - Pros: minimizes latency by minimizing the distance data needs to travel
- **OSI Layer 4 and Layer 7 Load Balancing**
    - Layer 4 routes traffic based on Layer 4 data, network data, like IP address and TCP port. It is fast and straightforward, but limited.
    - Layer 7 routes traffic based on Layer 7 data, application data, like HTTP headers, methods, or body content. It has additional processing overhead, but it offers greater flexibility and sophistication in routing decisions

## Consistent Hashing
Hashing is another technique that can be used to map requests to servers in the context of load balancing. The main benefit of mapping an IP address to a specific server becomes clear when servers cache user data. It would be inefficient to have multiple servers' caches storing the same data, so it's a good idea for a user to interact mostly with a consistent server. A simple hash function could be ```IP Address % # of Servers```. The issue with this approach becomes clear when you add or remove a server from the network. Then, each IP address could be mapped to a different server than before. 

Consistent hashing provides a solution to this. It uses a ring that represents the space of all possible hash values. Each server in the system is also represented as a point on this ring. The hash function takes the content of the request (IP address) and maps it to a hash value within the range of the ring. When a request arrives, we calculate its hash value using the hash function, and locate the next server on the ring that is equal to or follows the hash value.

![Consistent Hashing](./images/consistent-hashing.avif)

The above image shows that the hashing is consistent with the ring approach when a server goes down. But what about when a server is removed? This isn't too important for system design interviews, but there are definitely strategies to rebalance the positions of the servers. 

Consistent hashing is very useful when caching is a concern, like in CDNs or databases.