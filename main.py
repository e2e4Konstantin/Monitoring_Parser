from icecream import ic
from parsers import get_data_material_monitoring
from config import data_path
from files_features import create_abspath_file

import pandas

# Отчет март 2024.xlsx 00_test_Отчет_март_2024.xlsx
file_name = r"Отчет март 2024.xlsx"
sheet_name = r"приложение А"

csv_file_name = "monitoring_result.csv"
parquet_file_name = "monitoring_result.parquet"


if __name__ == "__main__":
    result = get_data_material_monitoring(data_path, file_name, sheet_name)
    ic(result[:5])

    df = pandas.DataFrame(
        result, columns=["code", "supplier_price", "delivery", "title"]
    )
    print(df)
    csv_file = create_abspath_file(data_path, csv_file_name)
    df.to_csv(csv_file, sep=",", index=False)

    parquet_file = create_abspath_file(data_path, parquet_file_name)
    df.to_parquet(parquet_file)
