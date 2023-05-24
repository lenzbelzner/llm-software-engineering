# Exploring LLMs for Software Engineering

Example output of exploring large language models for software engineering.

## System Design: Epics and Stories Creation

My input:
> I want to create a webapp for a trading card game.
> Players can collect cards for heroes and items, trade cards,
> go to exploration and battle with their cards, and collect loot from these actions.

See created milestones/epics [here](https://github.com/lenzbelzner/llm-software-engineering/milestones).

See created stories [here](https://github.com/lenzbelzner/llm-software-engineering/issues).

## Implementation

Currently there are two generated code skeletons, one for a flask app and one for a streamlit app. The specification used for code generation is a little more involved than the input for epics and stories. You can find it in [spec.md](https://github.com/lenzbelzner/llm-software-engineering/blob/main/spec.md). I created it using my requirement engineering bot: https://zen-reqbot.streamlit.app/.

### Flask

The [/flask](https://github.com/lenzbelzner/llm-software-engineering/tree/main/flask) folder contains the generated output. It is organized in three folders.
- [/model](https://github.com/lenzbelzner/llm-software-engineering/tree/main/flask/model): The data model created for the app.
- [/api](https://github.com/lenzbelzner/llm-software-engineering/tree/main/flask/api): The REST API. Contains an overview of use cases, and UML specs, code, and tests for each.
  - [/code](https://github.com/lenzbelzner/llm-software-engineering/tree/main/flask/api/code): Flask blueprints for each use case.
  - [/test](https://github.com/lenzbelzner/llm-software-engineering/tree/main/flask/api/test): Unit tests for each use case.
  - [/uml](https://github.com/lenzbelzner/llm-software-engineering/tree/main/flask/api/uml): Sequence diagrams for each use case.
- [/frontend](https://github.com/lenzbelzner/llm-software-engineering/tree/main/flask/frontend): Basic HTML mocks for each REST API endpoint.

### Streamlit

The [/streamlit](https://github.com/lenzbelzner/llm-software-engineering/tree/main/streamlit) app structure was proposed and implemented by GPT.
