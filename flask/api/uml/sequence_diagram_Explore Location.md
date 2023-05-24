```mermaid
sequenceDiagram
    participant User
    participant Server
    participant UserController
    participant ExplorationService
    participant CardService
    participant LocationService
    participant GPTManager

    User->>Server: POST /explore (user_id, cards, location)
    Server->>UserController: explore(user_id, cards, location)
    UserController->>ExplorationService: initiateExploration(user_id, cards, location)
    ExplorationService->>CardService: validateCards(user_id, cards)
    CardService->>ExplorationService: cardsValid
    ExplorationService->>LocationService: validateLocation(location)
    LocationService->>ExplorationService: locationValid
    ExplorationService->>GPTManager: generateEventDescription(cards, location)
    GPTManager->>ExplorationService: eventDescription
    ExplorationService->>ExplorationService: createExploration(user_id, cards, location, eventDescription)
    ExplorationService->>UserController: exploration
    UserController->>Server: response (Exploration object or error)
    Server->>User: response (Exploration object or error)
```
This sequence diagram represents the flow of the "Explore Location" RESTful use case, using the mermaid.js syntax in Markdown format. It shows how the User interacts with the Server, which in turn calls various classes and services to validate cards and locations, generate event descriptions, and create an Exploration object.