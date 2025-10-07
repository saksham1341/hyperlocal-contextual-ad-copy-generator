# Hyperlocal Contextual Ad Copy Generator

**WIP**

## LangGraph Architecture

![langgraph architecture](graph.png)

## Run the project

```sh
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run through dotenv
dotenv run -- python -m graph.py
```

## Project Structure

```txt
|___ src/
    |___ models.py
    |___ nodes.py
    |___ prompts.py
    |___ schemas.py
    |___ state.py
    |___ tools.py
|___ .env.example
|___ .gitignore
|___ config.py
|___ graph.png
|___ graph.py
|___ README.md
```
