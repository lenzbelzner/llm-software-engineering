```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant UserController
    participant UserService
    participant UserRepository
    participant ExplorationRepository
    participant BattleRepository
    participant CSVManager

    Client->>Server: GET /users/:id/history
    Server->>UserController: getUserGameHistory(user_id)
    UserController->>UserService: getUserGameHistory(user_id)
    UserService->>UserRepository: getUserById(user_id)
    UserRepository->>UserService: User
    UserService->>ExplorationRepository: getExplorationsByUserId(user_id)
    ExplorationRepository->>UserService: List of Explorations
    UserService->>BattleRepository: getBattlesByUserId(user_id)
    BattleRepository->>UserService: List of Battles
    UserService->>CSVManager: createCSV(User, List of Explorations, List of Battles)
    CSVManager->>UserService: CSV Data
    UserService->>UserController: List of Exploration and Battle objects or error
    UserController->>Server: Response (List of Exploration and Battle objects or error)
    Server->>Client: Response (List of Exploration and Battle objects or error)
```
This sequence diagram represents the flow of the "Get User Game History" use case using the mermaid.js markdown format. It shows the interaction between the client, server, and various classes involved in retrieving the user's game history of explorations and battles.