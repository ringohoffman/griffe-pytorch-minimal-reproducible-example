# griffe-pytorch-minimal-reproducible-example

This repository is a minimal reproducible example demonstrating a bug in `mkdocstrings-python` with https://github.com/mkdocstrings/python/commit/7f9757d1584555edebc56f1aefe6cc8242e6c8bb.

To reproduce:

```
git clone https://github.com/ringohoffman/mkdocstrings-python-minimum-reproducible-example
cd mkdocstrings-python-minimum-reproducible-example
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
mkdocs build
mkdocs serve
```
