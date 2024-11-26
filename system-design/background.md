# System Design Background Info

## Computer Architecture
- CPU: central processing unit, brain
    - reads/writes with various storage devices 
- Cache: memory part of CPU
    - fastest, but most expensive so its limited to MB
    - L1, L2, L3
- RAM: random access memory
    - significantly faster than disk, smaller limited to GB
- Disk: persistent storage
    - largest, can be up to TB

Upgrading one computer to improve scale and performance is a limited option. Think how Moore's Law (# of CPU transistors double every two years) is plateuing. Then, how can we utilize multiple computers to create scalable systems? The parts mentioned above have significant overlap...

## Application Architecture
![Diagram](./images/application-architecture.png)

#### Basics for the Developer
- Building and deploying code (after testing it in the CI/CD pipeline)
- App runs on a server that *serves* the user's requests
- Persistent storage (e.g. a database) that the server may need

What if the single server can't keep up with all the user requests?
1. Vertical scaling: upgrade the server's parts
2. Horizontal scaling: add more servers

We might also want some failover system, or have servers close to all global users.

Obviously horizontal scaling is better because it avoids the limitations of having only one server. We can always add more servers, and hence more computing resources! But this introduces a new problem, how do we know which server to route the user to? 

- Load Balancer
    - Route the user request to the server that has the minimum resources being used

#### Additional Developer Services:
- Logging
    - with each user request to the server, store the request/response data as well as server resource usage
- Metrics
    - produced from the logging storage, store the usage of the resources on that server (CPU/RAM/Disk)
- Alerts
    - the developer can check both of these, but also wants to be alerted immediately when something goes wrong with the server, e.g. only 95% of users are getting successful responses. Push-based unlike the other two.

## Design Requirements
When designing a complex system, there are three core elements. The design must aim to efficently accomplish each element.

1. Moving Data
2. Storing Data (Database? Blob store? File system?)
3. Transforming Data

### What makes a good design?
Bad design choices can be very costly. You may have to migrate data, rewrite portions of the app, etc.

**Availability**
$\frac{uptime}{total_time}$
Of course, it is ideal to have 100% ability but this is not realistic. We should aim instead for "9s" like 99%. However, even 99% uptime means that out of 365 days, the system would be down for 3.65 days. A good target for companies to have is 99.999% availability, which is 5 minutes of downtime in 365 days. Even though the percentage jump is small, it is a factor of 1000 in downtime reduction, which is a massive jump.

The measure of availability is used to define SLOs (service level objectives) and SLAs (service level agreements). SLA refers to an agreement a company makes with their clients or users to provide a certain metric of uptime, responsiveness, and responsibilities. SLO refers to an objective your team must hit to meet the SLA requirements. For example, AWS's monthly SLA is 99.99% and if not met, they refund a percentage of service credit.

**Reliability**: The probability that the system won't fail. In the event of a DDoS attack or thousands of users making requests, how easily does the system go down?

**Fault-Tolerance**: If servers fail, does the system keep working?

**Redundancy**: system has an "unnecessary" backup server (can also be active)

**Throughput**: the amount of data or operations we can handle over some period of time. $\frac{requests}{second}$, $\frac{queries}{second}$, or $\frac{bytes}{second}$. In the images below, it is clear how horizontal scaling is better than vertical. 

![Horizontal Scaling](./images/horizontal-scaling.avif)
![Vertical Scaling](./images/vertical-scaling.avif)

**Latency**: the amount of time it takes for each individual request to be completed (or for a user to receive a response). Think using a cache.

## Ultimate Goal
We want to design effective systems that can handle failures, have a high throughput, high availability, and low latency.