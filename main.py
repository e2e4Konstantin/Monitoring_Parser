from icecream import ic
import numpy
import pandas

from config import data_path, SourceData, anchors
from public import clear_string, clear_code, is_quote_code, get_float

file_name = (
    r"00_test_Отчет_март_2024.xlsx"  # Отчет март 2024.xlsx 00_test_Отчет_март_2024.xlsx
)  # Отчет март 2024.xlsx 00_test_Отчет_март_2024.xlsx
sheet_name = r"приложение А"


# find the first number from the bottom
SUPPLIER_PRICE_COLUMN_DELTA = 3
HEADER_HEIGHT = 3
RELATIVE_CODE_POSITION = 11

if __name__ == "__main__":
    data = SourceData(data_path, file_name, sheet_name)

    ic(data.__str__())

    res = data.find_cell_with_cleaning(anchors["base_column_value"].lower())
    ic(res)
    if res:
        column_number = data.cols_index[res.column] + SUPPLIER_PRICE_COLUMN_DELTA
        ic(column_number)
        start_row = data.look_number_below(res.row + HEADER_HEIGHT, column_number)
        ic(start_row)
        for row in range(start_row, data.row_max+1):  # +135
            code = clear_code(
                data.get_cell_value_by_index(
                    row, column_number - RELATIVE_CODE_POSITION
                )
            )
            if not code:
                continue
            if is_quote_code(code):
                raw_value = data.get_cell_value_by_index(row, column_number)
                value = get_float(raw_value)
                m = f"{code:>12}  {value:>13.2f}"
                # ic(row, m)
            else:
                m = f"шифр в строке {row} не соответствует шифру расценки"
                ic(m)
                break

# cursor.executemany("INSERT INTO my_table (column1, column2) VALUES (?, ?)", data)