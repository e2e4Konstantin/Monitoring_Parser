from icecream import ic
import pandas

from config import SourceData, anchors, TRANSPORT_HEADER_HEIGHT
from files_features import (
    create_abspath_file,
    output_message_exit,
    generate_result_file_name,
)
from public import clear_code, is_quote_code, get_float, clear_string


def get_df_transport_costs_monitoring(
    excel_file: str, sheet_name: str
) -> list[tuple[str, float]] | None:
    """
    Получить данные из файла мониторинга транспортных расходов.
    Возвращает список кортежей (шифр, 'текущая цена поставщика')
    Находит якорную колонку. Высчитывает столбец в котором записаны цены поставщика.
    Высчитывает строку с которой будет искать шифры расценок.
    Считывает шифр расценки и цену.
    """
    result = []
    data = SourceData(excel_file, sheet_name)
    code_anchor_position = data.find_cell_with_cleaning(
        anchors["transport_base_column_value"].lower()
    )
    price_anchor_position = data.find_cell_with_cleaning(
        anchors["transport_price_header_value"].lower()
    )

    if not code_anchor_position or not price_anchor_position:
        output_message_exit(
            "Не найдены 'якорные'ячейки",
            f"файл: {excel_file!r} таблица: {sheet_name!r}",
        )
        return None
    code_column_number = data.cols_index[code_anchor_position.column]
    price_column_number = data.cols_index[price_anchor_position.column]
    start_row = code_anchor_position.row + TRANSPORT_HEADER_HEIGHT
    for row in range(start_row, data.row_max + 1):
        code = clear_code(data.get_cell_value_by_index(row, code_column_number))
        if not code:
            continue
        if is_quote_code(code):
            raw_value = data.get_cell_value_by_index(row, price_column_number)
            price = get_float(raw_value)
            if price and isinstance(price, float) and price > 0:
                # ic(code, price)
                result.append((code, price))
        else:
            output_message_exit(
                f"Шифр не соответствует шаблону: {code}",
                f"цена поставщика в строке {row}",
            )
    return result if result else None



def monitoring_transport_costs_parse(data_place: dict[str:str]) -> int | None:
    """
    Разбирает файл мониторинга с ценами на Транспортные услуги,
    записывает результат в scv файл.
    """
    src_file = data_place["file"]
    result_csv_file = data_place["result_file"]
    sheet_name = data_place["sheet_name"]
    #
    result = get_df_transport_costs_monitoring(src_file, sheet_name)
    df = pandas.DataFrame(result, columns=["code", "current_price"])
    df.to_csv(result_csv_file, sep=",", index=False)
    #
    # parquet_file = create_abspath_file(data_path, parquet_file_name)
    # df.to_parquet(parquet_file)