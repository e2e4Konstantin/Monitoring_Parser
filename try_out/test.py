import string
import numpy as np


def set_column_names(num_columns: int) -> tuple[str, ...] | None:
    """
        Возвращает кортеж с именами колонок, которые соответствуют именам колонок в excel.
        Указанной длинны.
    """
    if num_columns <= 0:
        raise ValueError(f"num_columns <= 0: {num_columns}")

    columns = list(string.ascii_uppercase)
    if len(columns) >= num_columns:
        return tuple(columns[:num_columns])

    gen = columns
    for char in columns:
        gen_next = tuple(char + c for c in columns)
        gen = (*gen, *gen_next)
        if len(gen) >= num_columns:
            return tuple(gen[:num_columns])

    return None






if __name__ == "__main__":
    # x = set_column_names(13)
    # print(x)


    # arr = np.array([1, 2, 3])
    # idx = np.where(arr == 2)

    # print(idx)

    s = ''
    if not s:
        print("None")

    else:
        print("Gud")