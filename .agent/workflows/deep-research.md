---
description: Run autonomous deep research using Google Gemini Deep Research Agent
---

# Deep Research Workflow

This workflow executes autonomous multi-step research using the Google Gemini Deep Research Agent.

## Prerequisites

1. Ensure Python 3.8+ is installed
2. Install dependencies: `pip install -r .agent/skills/skills/deep-research/requirements.txt`
3. Set GEMINI_API_KEY environment variable or create `.env` file in the skill directory

## Steps

1. Ask the user for their research query/topic

2. Inform the user that the research will take 2-10 minutes and cost approximately $2-5

// turbo
3. Run the research command:
```bash
cd .agent/skills/skills/deep-research && python scripts/research.py --query "[USER_QUERY]" --stream
```

4. Wait for the research to complete and present the results to the user

5. Ask if they want to do follow-up research or elaborate on any specific points

## Optional Parameters

- Add `--format` to specify output structure
- Add `--no-wait` to start without waiting
- Use `--continue <interaction_id>` for follow-up questions
