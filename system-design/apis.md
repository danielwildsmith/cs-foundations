# APIs

## Application Protocols
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
