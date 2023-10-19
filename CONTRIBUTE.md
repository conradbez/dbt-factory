

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

Incement version in `dbtf/src/dbtf/__about__.py` and ensure you are in the directory containing `pyproject.toml` then run:

- `hatch build`
- `hatch publish`
