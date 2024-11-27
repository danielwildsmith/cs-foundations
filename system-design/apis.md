# APIs
API stands for Application Programming Interface and provides a way for clients to perform actions with servers over the network. APIs consist of a set of rules and protocols for building and interacting with software applications. They define the methods and data formats that programs, typically software libraries or operating systems, should use to communicate with other software.

## HTTP
**Client-server architecture**: think roles. Client initiates request, server serves response. Sometimes, servers can play the role of the client when talking to another server. 

**RPC**: remote procedure call. How do we call a function that exists on a server across a network? Any network call can be classifed as an RPC.

**HTTP**: Hyper Text Transfer Protocol. A request-response protocol built on top of TCP/IP layer. A request has a header and body. Request header has URL, request method, status code.  A response also has a similar header and body. Vulnerable to "man in the middle attack," where anyone can intercept it.

**HTTPS**: Hyper Text Transfer Protocol *Secure*. Utilizes SSL/TLS, which encrypts anything within the request.

### HTTP Methods
GET, POST, PUT, DELETE

```https://youtube.com``` is the route, can have multiple HTTP methods associated with it, each with their own functionality.

GET requests do have bodies.

### HTTP Status Codes
- Information responses (100 - 199)
    - ```100 Continue```: This response indicates that everything is in order so far, and the client should proceed with the request or disregard it if it has already been completed.
    - ```101 Switching Protocols```: This response indicates that the server is switching to a different protocol as specified in the upgrade request header received from the client.
- Successful responses (200 - 299)
    - ```200 OK```: This response code indicates that the request has succeeded. It signifies that the request has been processed and the server is returning the requested data.
    - ```201 Created```: This response code indicates that the request has succeeded, resulting in the creation of a new resource. It is typically sent after POST or PUT requests, confirming that the resource has been successfully created or updated.
- Redirection messages (300 - 399)
    - ```300 Multiple Choices```: This response code means that the request has more than one possible response. The client should choose one of them.
    - ```301 Moved Permanently```: This response code means that the requested resource has been permanently moved to a new location, and the server is redirecting the client to this new location.
- Client error responses (400 - 499)
    - ```400 Bad Request```: This response code is used when the server encounters a client request that is invalid or cannot be understood. It often occurs when incorrect parameters are passed in the request, leading to a bad request.
    - ```401 Unauthorized```: This response code is returned when a client attempts to access a protected resource without proper authentication or authorization. For example, if you try to delete a video that you are not authorized to delete, the server will respond with a 401 Unauthorized status code.
- Server error responses (500 - 599)

## Websockets
HTTP can accomplish most tasks. But what about the case of a live feed of a chat, like Twitch? With HTTP, you could implement **polling**, sending a new request each second. But this seems pretty inefficient, initializing and quickly closing the connection with each request. This causes alot of overhead. Websockets solve this problem, by keeping the connection alive. First, a HTTP request initializes the connection, then the protocol gets switched to *websocket*. WebSockets are bi-directional, and this way the client will not have to keep checking the server for new data.

## API Paradigms
There are different ways to build APIs atop HTTP, all with tradeoffs and scenarios where they excel.

### Rest APIs
REST, **RE**presentational **S**tate **T**ransfer, aims to use straightforward HTTP between client and server. It has certain restrictions/standardizations. The most important is it being **stateless**: requests from the client should include all necessary information for the server, so that it does not have to store state about each client's previous requests. A good example is first fetching 10 YouTube videos, and then wanting to fetch 10 more that are different. The stateful approach would require the server to remember which videos it served the client on the previous request. With systems that utilizes a load balancer and multiple servers, this stateful approach would be problematic. REST aims to avoid this by including everything in the request, like the limit of videos to fetch and the offset to start fetching from. 

One important note is that REST utilizes the HTTP methods (GET, POST...). Because of this, REST API endpoints typically are nouns as resources. For example, ```youtube.com/videos``` could be a route that you could GET, POST, PUT, or DELETE a video resource.

A popular data format used with REST is JSON (JavaScript Object Notation). It uses key-value pairs and supports various levels of nesting (objects, arrays, etc). It is ultimately a string though, and a main advantage is how human-readable it is.

Rest APIs have problems, however, with over-fetching or under-fetching data. Imagine a comment section where you want to fetch a username, profile picture, and the comment itself. For every comment, you will make a request to ```/user```, getting unnecessary information like join_date, num_videos... This is over-fetching. One approach around this is to narrowly define endpoints, like ```/user/profile_picture```. But this could lead to a ton of requests and confusing API design. This is under-fetching. 

How do we efficiently get the data we need??

### GraphQL
To solve this problem of over-fetching and under-fetching data with REST APIs, GraphQL was created. With GraphQL, the client can specify the exact data it needs within one request. It does not use the 4 HTTP methods like REST, it typically only operates through a single HTTP POST endpoint. In GraphQL, there are two primary types of operations: **queries** and **mutations**. Queries are utilized to retrieve data, while mutations are employed for modifying data on the server.

```
{
  launchesPast(limit: 10) {
    mission_name
    launch_date_local
    launch_site {
      site_name_long
    }
    links {
      article_link
      video_link
    }
    rocket {
      rocket_name
    }
  }
}
```

### gRPC
gRPC, Google Remote Procedure Call, is the fastest way to send data because it uses protcol buffers to send data instead of JSON. Protocol buffers are a language-neutral, platform-neutral extensible mechanism for serializing structured data. gRPC uses HTTP/2 to provide bidirectional communication, but is not a replacement for Websockets because browsers cannot support this HTTP/2 low-level feature. Because of this, gRPC is typically only used server-server. gRPC is a replacement for REST APIs, not Websockets. Also, gRPC is built on top of HTTP, but it does not utilize HTTP's methods or status codes, so you are required to develop your own.

The protocol buffer schemas/messages are typically created in .proto files. Here is a sample gRPC API:

```
// The greeter service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
  rpc SayHelloAgain (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

The "1" for message and name indicates that it is the first thing to be read within the protocol buffer. Also, notice the RPCs have a verb as part of their name. This is because gRPC doesn't utilize the HTTP methods.

Compare the amount of data to send this JSON request. 

```
{
  "user_id": 123456,
  "name": "John",
  "active": true
}
```

This would take ~47 bytes, since the keys and the values need to be serialized in each request. In gRPC, the size of the request is much smaller due to the defined protocol buffer schema.

```
message User {
  int64 user_id = 1;  // 8 bytes
  string name = 2;    // ~5 bytes
  bool active = 3;    // 1 byte
}
```

### Summary
#### REST
- **Best for:** Simple CRUD operations, standard web apps, public APIs
- **Pros:** HTTP caching, tooling, simplicity, stateless
- **Cons:** Over/under-fetching, multiple round trips
- **Use when:** Resources map cleanly to URLs, standard HTTP methods suffice

#### GraphQL
- **Best for:** Complex data requirements, varied clients (web/mobile)
- **Pros:** Flexible queries, single endpoint, typed schema
- **Cons:** Caching complexity, server load, learning curve
- **Use when:** Clients need different data shapes, reducing round trips is critical

#### gRPC
- **Best for:** Microservices, internal communication
- **Pros:** High performance, strong typing, bi-directional streaming
- **Cons:** Browser limitations, complex setup, less human-readable
- **Use when:** Low latency critical, service mesh architectures

### Quick Decision Guide
- Public API → REST
- Mobile + Web Clients → GraphQL
- Internal Services → gRPC
- Simple CRUD → REST
- Real-time Updates → gRPC/WebSocket
- Complex Data Needs → GraphQL

## Other API Types
### Webhooks
Webhooks are HTTP callbacks that enable real-time data push between systems. They act as "reverse APIs" where the server pushes data to client-specified endpoints when events occur, eliminating the need for polling. Webhooks use standard HTTP POST requests with JSON or XML payloads and require the receiving endpoint to be publicly accessible. They excel at event-driven architectures but can be unreliable since there's no built-in retry mechanism or delivery guarantee. Common uses include payment processing notifications, CI/CD pipeline triggers, and CRM integrations. Webhooks are complementary to REST APIs, not a replacement, as they serve different purposes: REST for request-response interactions, Webhooks for event notifications.

## API Design
This section will discuss REST APIs, since they are most commonly used. Disregarding the implementation of the interface, it is important to design the method signature and return value well. For public-facing APIs, there can be many other applications reliant on the protocols you define, and changing them could break their applications. If possible, aim for **backwards compatibility** when updating signatures by making the new parameters optional. If not possible, it is good to use **versioning** so that the old API still works, while providing a new API altogether. Deprecating the older version prompts developers to transition to the latest version.

When designing GET endpoints, **pagination** is a helpful tool when fetching a large amount of data. The client can add an offset and limit as a query. They should also be read-only implemented so that caching the results is reliable. 

Endpoints should also be named appropriately and not conflict. 

The Stripe and Twitter APIs are good examples to look at.