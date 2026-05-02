# System Design

AutoCommerce-Agent uses a multi-agent pipeline. Each agent handles a specific stage in the e-commerce short-video production process.

## Pipeline

1. Product Input
2. Product Insight Agent
3. Viral Script Analysis Agent
4. Video Prompt Agent
5. Quality Review Agent
6. Report Agent

## Design Principles

- Every Agent has a clear input and output.
- Prompts and scripts are structured, not free-form.
- The workflow is optimized for repeatable production.
- Quality review standards are separated from generation logic.
- Cost control is part of the workflow, not an afterthought.

## Data Flow

```mermaid
sequenceDiagram
    participant U as User
    participant P as Pipeline
    participant A1 as Product Insight Agent
    participant A2 as Viral Script Agent
    participant A3 as Video Prompt Agent
    participant A4 as Quality Review Agent
    participant A5 as Report Agent

    U->>P: product info
    P->>A1: analyze product
    A1->>A2: product insight
    A2->>A3: script structure
    A3->>A4: model prompts
    A4->>A5: scorecard and revision rules
    A5->>U: production report
```
