Here's a mermaid.js sequence diagram for the "Add Card to Collection" use case:

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant UserController
    participant UserService
    participant UserRepository
    participant CardRepository
    participant CSVManager

    Client->>Server: POST /users/:id/collection/add
    Server->>UserController: addUserCardToCollection(user_id, card)
    UserController->>UserService: addUserCardToCollection(user_id, card)
    UserService->>UserRepository: getUserById(user_id)
    UserRepository->>UserService: return User
    UserService->>CardRepository: getCardByName(card.name)
    CardRepository->>UserService: return Card
    UserService->>UserRepository: addCardToUserCollection(User, Card)
    UserRepository->>CSVManager: updateCSV(User)
    CSVManager->>UserRepository: return success
    UserRepository->>UserService: return Updated Collection
    UserService->>UserController: return Updated Collection
    UserController->>Server: return Updated Collection
    Server->>Client: return Updated Collection or error
```

This sequence diagram illustrates the flow of the "Add Card to Collection" use case using the provided classes and parameters. The diagram starts with the client making a POST request to the server, and ends with the server returning the updated card collection or an error.