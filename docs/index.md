# Welcome to MkDocs

## This documentation will cause the build to fail if there is a pytorch `.pth` file in the project

::: foo.Bar.baz
    options:
      show_source: true

## To reproduce the issue

```bash
git clone https://github.com/qthequartermasterman/griffe-pytorch-minimal-reproducible-example
cd griffe-pytorch-minimal-reproducible-example
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python build-pytorch-state-dict.py  # This script will create a `state_dict.pth` file
mkdocs build  # This will error.
```