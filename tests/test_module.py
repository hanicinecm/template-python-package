import pytest

import pkg_template
from pkg_template.module import get_columns, get_dataframe


@pytest.mark.parametrize("n, cols", ((1, ["a"]), (3, ["a", "b", "c"])))
def test_get_columns(n, cols):
    assert get_columns(n) == cols


@pytest.mark.parametrize("n_lines", (1, 2))
def test_get_dataframe(monkeypatch, n_lines):
    monkeypatch.setattr(pkg_template.module, "get_columns", lambda n: ["h", "a", "m"])
    assert get_dataframe((n_lines, 3)).shape == (n_lines, 3)
    assert list(get_dataframe((n_lines, 3)).columns) == "h a m".split()
    assert len(get_dataframe((n_lines, 3))) == n_lines
