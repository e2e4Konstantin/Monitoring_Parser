from icecream import ic
from config import monitoring_data_place as config
from parsers import monitoring_materials_parse, monitoring_transport_costs_parse





if __name__ == "__main__":

    # ic(config['transport'].keys())
    # ic(config["materials"].keys())

    #
    # history_time = ["январь_2024", "февраль_2024", "март_2024", "апрель_2024"]
    # for data in history_time:
    #     src_data = config['transport'][data]
    #     ic(src_data)
    #     monitoring_transport_costs_parse(src_data)

    history_time = ["январь_2024", "февраль_2024", "март_2024", "апрель_2024"]
    for data in history_time:
        src_data = config["materials"][data]
        ic(src_data)
        monitoring_materials_parse(src_data)