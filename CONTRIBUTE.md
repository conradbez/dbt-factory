

## Setup hatch:

`pip install hatch`
`cd dbtf`
`hatch create`
`hatch shell`

## Gotchas:

Sometime hatch wouldn't reload unless I opened a new terminal and ran:

`hatch env remove default`

`cd dbtf`

`hatch create`

`hatch shell`

# Publish

Ensure you are in the directory containing `pyproject.toml` and run:

- `hatch build`
- `hatch publish`
