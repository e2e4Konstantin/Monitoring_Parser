from icecream import ic
from parsers import get_data_material_monitoring
from config import data_path

file_name = (
    r"00_test_Отчет_март_2024.xlsx"  # Отчет март 2024.xlsx 00_test_Отчет_март_2024.xlsx
)  # Отчет март 2024.xlsx 00_test_Отчет_март_2024.xlsx

sheet_name = r"приложение А"




if __name__ == "__main__":
    result = get_data_material_monitoring(data_path, file_name, sheet_name)

    ic(result)


# cursor.executemany("INSERT INTO my_table (column1, column2) VALUES (?, ?)", data)

