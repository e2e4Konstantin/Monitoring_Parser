from icecream import ic
from config import monitoring_data_place as config
from parsers import monitoring_materials_parse, monitoring_transport_costs_parse


if __name__ == "__main__":
    # ic(config)
    monitoring_materials_parse(config)
    message = f"мониторинг материалов выгружен в файл {config['material_results_file']!r}"
    ic(message)
    monitoring_transport_costs_parse(config)
    message = f"мониторинг транспортных затрат выгружен в файл {config['transport_results_file']!r}"
    ic(message)