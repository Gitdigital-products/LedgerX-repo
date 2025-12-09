# Contributing Guide

Thank you for considering contributing to LedgerX!

## Development Workflow
- Clone the repo
- Install dependencies (`pip install -r requirements.txt`)
- Run governance pipeline (`./scripts/governance.sh`)

## Testing
- Add unit tests for new features
- Run `pytest` before submitting PRs

## Code Style
- Python code must pass `flake8` and `black`
- YAML/JSON must validate via pre-commit hooks