from icecream import ic
import numpy
import pandas

from config import data_path, SourceData, anchors
from public import clear_string

file_name = r"test_Отчет_март_2024.xlsx"
sheet_name = r"приложение А"

def find_cell(src_df: pandas.DataFrame, target: str ) -> tuple[int, int]:
    rows, cols = numpy.where(data.df == target)
    ic(rows[0])
    return rows, cols


if __name__ == "__main__":
    data = SourceData(data_path, file_name, sheet_name)
    ic()
    ic(data.df.columns)
    # data.set_column_names()
    # for row in range(0, data.row_max + 1):
    #     for column in data.df.columns:
    #         value = clear_string(data.get_cell_value(row, column))
    #         ic(row, column, value[:10])
    #         if value.lower() == anchors["base_column_value"].lower():
    #             ic(value)
    #             break
    #     else:
    #         continue
    #     break
    x = find_cell(data.df, "1.1-1-51")
    ic(x)
