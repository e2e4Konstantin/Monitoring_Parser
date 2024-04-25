from collections import namedtuple
from files_features import create_abspath_file, generate_result_file_name


CellPosition = namedtuple(typename="CellPosition", field_names=["row", "column"])
CellPosition.__annotations__ = {"row": int, "column": str}

SUPPLIER_PRICE_COLUMN_DELTA = 3
HEADER_HEIGHT = 3
RELATIVE_CODE_POSITION = 11

TRANSPORT_HEADER_HEIGHT = 1

variations_delivery_value = ("с доставкой", "c доставкой")

monitoring_data_place = {
    "data_path": r"C:\Users\kazak.ke\Documents\Задачи\5_Надя\Мониторинг",
    "unload_path": r"C:\Users\kazak.ke\Documents\АИС_Выгрузка\Мониторинг",
    #
    "materials_file_name": r"Мониторинг_Март_2024_210_71.xlsx",
    "materials_sheet_name": r"приложение А",
    "materials_result_file_name": r"materials_monitoring_result.csv",
    "materials_supplement": 71,
    "materials_index": 210,
    #
    "transport_file_name": r"Раздел_0_Индексы_под загрузку_16.01.2024.xlsx",
    "transport_sheet_name": r"Лист1",
    "transport_result_file_name": r"transport_monitoring_result.csv",
    "transport_supplement": 71,
    "transport_index": 208,
}

monitoring_data_place["transport_src_file"] = create_abspath_file(
        monitoring_data_place["data_path"], monitoring_data_place["transport_file_name"])

monitoring_data_place["transport_results_file"] = create_abspath_file(
        monitoring_data_place["unload_path"], monitoring_data_place["transport_result_file_name"])

monitoring_data_place["transport_results_file"] = generate_result_file_name(
    monitoring_data_place["transport_results_file"],
    monitoring_data_place["transport_supplement"],
    monitoring_data_place["transport_index"]
)


monitoring_data_place["materials_src_file"] = create_abspath_file(
    monitoring_data_place["data_path"],
    monitoring_data_place["materials_file_name"]
)

monitoring_data_place["material_results_file"] = create_abspath_file(
    monitoring_data_place["unload_path"],
    monitoring_data_place["materials_result_file_name"],
)

monitoring_data_place["material_results_file"] = generate_result_file_name(
    monitoring_data_place["material_results_file"],
    monitoring_data_place["materials_supplement"],
    monitoring_data_place["materials_index"],
)


if __name__ == "__main__":
    from icecream import ic

    ic(monitoring_data_place)