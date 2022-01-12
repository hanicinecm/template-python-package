import pandas as pd
import numpy as np


def get_columns(n: int):
    return list("abcdefghijklmnopqrstuvwxyz"[:n])


def get_dataframe(shape: tuple[int, int]):
    return pd.DataFrame(
        np.arange(shape[0] * shape[1]).reshape(shape), columns=get_columns(shape[1])
    )
