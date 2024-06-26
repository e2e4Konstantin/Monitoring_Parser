from collections import namedtuple
from files_features import create_abspath_file, generate_result_file_name
# from src_files_path import src_transport_data


CellPosition = namedtuple(typename="CellPosition", field_names=["row", "column"])
CellPosition.__annotations__ = {"row": int, "column": str}

SUPPLIER_PRICE_COLUMN_DELTA = 3
HEADER_HEIGHT = 3
RELATIVE_CODE_POSITION = 11

TRANSPORT_HEADER_HEIGHT = 1

variations_delivery_value = ("с доставкой", "c доставкой")

src_transport_path = (
    r"C:\Users\kazak.ke\Documents\Задачи\5_Надя\исходные_данные\транспорт"
)
src_material_path = (
    r"C:\Users\kazak.ke\Documents\Задачи\5_Надя\исходные_данные\материалы"
)
unload_path = r"C:\Users\kazak.ke\Documents\АИС_Выгрузка\Мониторинг"

transport_timeline = {
    "январь_2024": ("Раздел_0_Индексы_под загрузку_16.01.2024.xlsx", 71, 208, "Лист1"),
    "февраль_2024": ("Раздел_0_Индексы_под загрузку_13.02.2024.xlsx", 71, 209, "Лист1"),
    "март_2024": ("Раздел_0_Индексы_под загрузку_18.03.2024.xlsx", 71, 210, "Лист1"),
    "апрель_2024": ("Раздел_0_Индексы_под загрузку_18.04.2024.xlsx", 72, 211, "Лист1"),
    "май_2024": ("Раздел_0_Индексы_под загрузку_21.05.2024.xlsx", 72, 212, "Лист1"),
}

monitoring_timeline = {
    "январь_2024": (
        "1_Глава_1_раздел0_тарифы_ для Доп_71_01-2024 - данные 2024-01-19.xlsx",
        71,
        208,
        "Отчет мониторинга для 01-2024",
    ),
    "февраль_2024": ("2_Отчет январь 2024.xlsx", 71, 209, "приложение А"),
    "март_2024": ("3_Отчет февраль 2024.xlsx", 71, 210, "приложение А"),
    "апрель_2024": (
        "4_Глава_1_раздел0_тарифы_ для Доп_72_2 кв 2024 - данные 2024-04-18.xlsx",
        72,
        211,
        "Отчет мониторинга на 2 кв 2024",
    ),
    "май_2024": ("5_Отчет апрель 2024.xlsx", 72, 212, "приложение А"),
}
#
# мониторинг транспорта
#
src_transport_data = {x: {} for x in transport_timeline.keys()}

for data in src_transport_data.keys():
    src_transport_data[data]["file_name"] = transport_timeline[data][0]
    src_transport_data[data]["supplement"] = transport_timeline[data][1]
    src_transport_data[data]["index"] = transport_timeline[data][2]
    src_transport_data[data]["sheet_name"] = transport_timeline[data][3]
    src_transport_data[data]["file"] = create_abspath_file(
        src_transport_path, src_transport_data[data]["file_name"]
    )
    src_transport_data[data]["result_file_name"] = r"transport_monitoring_result.csv"
    src_transport_data[data]["result_file_gen"] = generate_result_file_name(
        src_transport_data[data]["result_file_name"],
        src_transport_data[data]["supplement"],
        src_transport_data[data]["index"],
    )
    src_transport_data[data]["result_file"] = create_abspath_file(
        unload_path, src_transport_data[data]["result_file_gen"]
    )
#
# мониторинг материалов
#
src_material_data = {x: {} for x in monitoring_timeline.keys()}

for data in src_material_data.keys():
    src_material_data[data]["file_name"] = monitoring_timeline[data][0]
    src_material_data[data]["supplement"] = monitoring_timeline[data][1]
    src_material_data[data]["index"] = monitoring_timeline[data][2]
    src_material_data[data]["sheet_name"] = monitoring_timeline[data][3]
    src_material_data[data]["file"] = create_abspath_file(
        src_material_path, src_material_data[data]["file_name"]
    )
    src_material_data[data]["result_file_name"] = r"materials_monitoring_result.csv"
    src_material_data[data]["result_file_gen"] = generate_result_file_name(
        src_material_data[data]["result_file_name"],
        src_material_data[data]["supplement"],
        src_material_data[data]["index"],
    )
    src_material_data[data]["result_file"] = create_abspath_file(
        unload_path, src_material_data[data]["result_file_gen"]
    )




monitoring_data_place = {
    "transport": src_transport_data,
    "materials": src_material_data,
}



if __name__ == "__main__":
    from icecream import ic
    ic(monitoring_data_place)