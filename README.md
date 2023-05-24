# Exploring Large Language Models for Software Engineering

Software Engineering (SE) has traditionally been a highly manual, human-driven process that involves a range of activities from requirement gathering and analysis, to system design, implementation, and testing. Recent advances in artificial intelligence (AI) have led to the development of powerful natural language processing models such as OpenAI's GPT, known as large language models (LLMs). These LLMs have opened a wide array of applications in various domains, including application in software engineering processes.

Here I want to explore potential benefits and challenges associated with the adoption of LLMs in software engineering, with a particular focus on requirements engineering, system design, code and test generation, and code quality reviews.

## System Design: Requirements Bot

Here's a bot supporting me with system design and requirements engineering: https://zen-reqbot.streamlit.app/. I found that my initial specs where heavily underspecified, and created this bot to help me refining my ideas and requirements. To me it feels much easier to have a conversation about my ideas than to start writing on a blank page. :)

## System Design: Epics and Stories Generation

My input:
> I want to create a webapp for a trading card game.
> Players can collect cards for heroes and items, trade cards,
> go to exploration and battle with their cards, and collect loot from these actions.

See created milestones/epics [here](https://github.com/lenzbelzner/llm-software-engineering/milestones).

See created stories [here](https://github.com/lenzbelzner/llm-software-engineering/issues).

## Implementation: Code and Artifact Generation

Disclaimer: The generated code is not complete, correct, nor executable without further editing.

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
