# Contributing to dbt-factory

## Development Setup (using uv)

We use [uv](https://github.com/astral-sh/uv) for lightning-fast dependency management and builds.

1. **Install uv**: Follow instructions at [astral.sh/uv](https://astral.sh/uv).
2. **Setup environment**:
   ```bash
   cd dbtf
   uv venv
   uv pip install -e .[test]
   ```
3. **Run Tests**:
   ```bash
   uv run pytest
   ```

## Workflow & Guidelines

- **Templates**: Add new SQL templates to `src/dbtf/dbt_project/templates/`. Use `##placeholder##` for variables.
- **Dependencies**: New dependencies should be added via `uv add <package>`.

# Publishing

We use GitHub Actions to automate publishing to PyPI.

### 1. Automated Release (Preferred)
1. **Bump Version**: Update `__version__` in `dbtf/src/dbtf/__about__.py`.
2. **Commit & Tag**:
   ```bash
   git add .
   git commit -m "release: v0.0.x"
   git tag v0.0.x
   git push origin main --tags
   ```
The GitHub Action will automatically build and publish to PyPI.

### 2. Manual Publish (Fallback)
Ensure you have the `PYPI_API_TOKEN` configured or set as an environment variable `UV_PUBLISH_TOKEN`.

1. **Build**:
   ```bash
   cd dbtf
   uv build
   ```
2. **Upload**:
   ```bash
   uv publish
   ```

## Legacy (Hatch)
Previously, this project used `hatch`. While still compatible via `hatchling` backend, `uv` is now the primary tool for development and publishing.
