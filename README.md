![Release](https://img.shields.io/github/v/release/phamhoangtuan/setup_python_project?color=brightgreen&sort=semver)
[![Linting](https://github.com/phamhoangtuan/setup_python_project/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/phamhoangtuan/setup_python_project/actions/workflows/lint.yml)
[![Testing](https://github.com/phamhoangtuan/setup_python_project/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/phamhoangtuan/setup_python_project/actions/workflows/test.yml)
[![Documentation](https://github.com/phamhoangtuan/setup_python_project/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/phamhoangtuan/setup_python_project/actions/workflows/pages.yml)

# setup_python_project
Follow guide in https://johschmidt42.medium.com/setting-up-python-projects-part-i-c4bd84b709d1

## Commands to run
```shell
poetry init --name example_app --no-interaction
poetry env use python3.10
poetry lock

poetry add httpx fastapi "uvicorn[standard]"
python src/example_app/app.py

poetry add --group lint isort black flake8 mypy

make format
make lint

poetry add --group test respx pytest-asyncio trio
poetry add --group test pytest-cov

make unit-tests
make unit-tests-cov
make clean-cov

poetry add --group docs mkdocs mkdocs-material
mkdocs build
mkdocs gh-deploy -m "docs: update documentation" -v --force

poetry add --group docs "mkdocstrings[python]"

git tag -a v0.1.0 -m "version v0.1.0"
git push origin v0.1.0

poetry add --group semver python-semantic-release
```
