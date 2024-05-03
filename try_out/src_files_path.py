import sys
sys.path.append(r"c:\Users\kazak.ke\Documents\PythonProjects\Monitoring_Parser")
# print(sys.path)
# print(__file__)

from config import create_abspath_file

src_data_path = r"C:\Users\kazak.ke\Documents\Задачи\5_Надя\Мониторинг"

timeline = {
    "январь_2024": ("Раздел_0_Индексы_под загрузку_16.01.2024.xlsx", 71, 208),
    "февраль_2024": ("Раздел_0_Индексы_под загрузку_13.02.2024.xlsx", 71, 209),
    "март_2024": ("Раздел_0_Индексы_под загрузку_18.03.2024.xlsx", 71, 210 ),
    "апрель_2024": ("Раздел_0_Индексы_под загрузку_18.04.2024.xlsx", 72, 211)
}

src_transport_data = { x : {} for x in timeline.keys() }


for data in src_transport_data.keys():
    src_transport_data[data]['file_name'] = timeline[data][0]
    src_transport_data[data]["supplement"] = timeline[data][1]
    src_transport_data[data]["index"] = timeline[data][2]
    src_transport_data[data]["file"] = create_abspath_file(
        src_data_path, src_transport_data[data]["file_name"]
    )


# print(src_transport_data["апрель_2024"])
