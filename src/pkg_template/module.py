"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Examples:
    >>> df = get_dataframe((2, 2))
    >>> df
       a  b
    0  0  1
    1  2  4
"""

import numpy as np
import pandas as pd


def get_columns(n: int) -> list[str]:
    """Dummy function.

    Longer function description.

    Args:
        n: number of columns.

    Returns:
        list of str letters starting with "a" and of length n.
    """
    return list('abcdefghijklmnopqrstuvwxyz'[:n])


def get_dataframe(shape: tuple[int, int]) -> pd.DataFrame:
    """Dummy function one line descriptions.

    Longer description of the function.

    Args:
        shape: shape of the dataframe.

    Returns:
        What do you care?
    """
    return pd.DataFrame(
        np.arange(shape[0] * shape[1]).reshape(shape), columns=get_columns(shape[1])
    )
