# htmldiff2

[![Tests](https://github.com/edsu/htmldiff2/actions/workflows/test.yml/badge.svg)](https://github.com/edsu/htmldiff2/actions/workflows/test.yml)

htmldiff2 is a library that uses [difflib], [genshi] and [html5lib] to diff
arbitrary fragments of HTML inline. htmldiff2 is a friendly fork of Armin
Ronacher's [htmldiff](https://github.com/mitsuhiko/htmldiff) which needed to be
upgraded for the [diffengine](https://github.com/docnow/diffengine) project. See
[this issue](https://github.com/mitsuhiko/htmldiff/issues/7) for context.

```python
>>> from htmldiff2 import render_html_diff
>>> render_html_diff('Foo <b>bar</b> baz', 'Foo <i>bar</i> baz')
u'<div class="diff">Foo <i class="tagdiff_replaced">bar</i> baz</div>'
>>> render_html_diff('Foo bar baz', 'Foo baz')
u'<div class="diff">Foo <del>bar</del> baz</div>'
>>> render_html_diff('Foo baz', 'Foo blah baz')
u'<div class="diff">Foo <ins>blah</ins> baz</div>'
```

## Develop

```
python -mvenv .venv
source .venv/bin/activate
python -m pip install -e .
python test.py
```

## Publish

```
python -m pip install setuptools build twine
python -m build
python -m twine upload dist/*
```

[genshi]: https://genshi.edgewall.org/
[html5lib]: https://github.com/html5lib/html5lib-python
[difflib]: https://docs.python.org/3/library/difflib.html
