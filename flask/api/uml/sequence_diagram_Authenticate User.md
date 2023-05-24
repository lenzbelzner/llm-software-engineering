```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant User
    participant AuthManager

    Client->>+Server: POST /auth {username, password}
    Server->>+AuthManager: authenticate(username, password)
    AuthManager->>+User: findByUsername(username)
    User-->>-AuthManager: user
    AuthManager->>AuthManager: comparePassword(password, user.password)
    AuthManager->>AuthManager: generateAccessToken(user)
    AuthManager-->>-Server: accessToken
    Server-->>-Client: {accessToken} or {error}
```
This sequence diagram illustrates the flow of the "Authenticate User" use case using mermaid.js in markdown format. The client sends a POST request to the server with the username and password. The server then calls the authenticate method in the AuthManager class, which finds the user by the username and compares the provided password with the stored password. If the authentication is successful, an access token is generated and returned to the client. Otherwise, an error is returned.