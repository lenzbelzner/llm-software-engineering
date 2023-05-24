# Exploring LLMs for Software Engineering

Example output of exploring large language models for software engineering.

## System Design: Epics and Stories Creation

My input:
> I want to create a webapp for a trading card game.
> Players can collect cards for heroes and items, trade cards,
> go to exploration and battle with their cards, and collect loot from these actions.

Created milestones/epics:
https://github.com/lenzbelzner/llm-software-engineering/milestones

Created stories:
https://github.com/lenzbelzner/llm-software-engineering/issues

## Implementation

Currently there are created two code skeletons, one for a flask app and one for a streamlit app.
 
The spec used for code generation is a little more involved than the input for epics and stories. You can find it in spec.md. I created it using a requirement engineering bot here: https://zen-reqbot.streamlit.app/

### Flask

The /flask folder contains the generated output. It is organized in three folders.
- /model: The data model created for the app.
- /api: The REST API. Contains an overview of use cases, and UML specs, code, and tests for each.
  - /code: Flask blueprints for each use case.
  - /test: Unit tests for each use case.
  - /uml: Mermaid.js sequence diagrams for each use case.
- /frontend: Basic HTML mocks for each REST API endpoint.