from icecream import ic
import pandas

from config import (
    SourceData,
    anchors,
    SUPPLIER_PRICE_COLUMN_DELTA,
    HEADER_HEIGHT,
    RELATIVE_CODE_POSITION,
    variations_delivery_value
)
from files_features import create_abspath_file, output_message_exit
from public import clear_code, is_quote_code, get_float, clear_string



def get_df_material_monitoring(excel_file: str, sheet_name: str) -> list[tuple[str, float]] | None:
    """
    Получить данные из файла мониторинга.
    Возвращает список кортежей (шифр, 'отпускная цена поставщика')
    Находит якорную колонку. Высчитывает столбец в котором записаны цены поставщика.
    Высчитывает строку с которой будет искать шифры расценок.
    Считывает шифр расценки и цену поставщика.
    """
    result = []
    data = SourceData(excel_file, sheet_name)
    anchor_position = data.find_cell_with_cleaning(
        anchors["materials_base_column_value"].lower()
    )
    if not anchor_position:
        output_message_exit(
            "Не найдена 'якорная'ячейка", f"файл: {excel_file!r} таблица: {sheet_name!r}"
        )
        return None
    column_number = data.cols_index[anchor_position.column] + SUPPLIER_PRICE_COLUMN_DELTA
    start_row = data.look_number_below(anchor_position.row + HEADER_HEIGHT, column_number)
    for row in range(start_row, data.row_max + 1):
        code = clear_code(
            data.get_cell_value_by_index(row, column_number - RELATIVE_CODE_POSITION)
        )
        if not code:
            continue
        if is_quote_code(code):
            raw_value = data.get_cell_value_by_index(row, column_number)
            supplier_price = get_float(raw_value)
            if supplier_price and isinstance(supplier_price, float) and supplier_price > 0:
                raw_delivery = clear_string(data.get_cell_value_by_index(row, column_number + 6))
                delivery = raw_delivery.lower() in variations_delivery_value
                material_name = clear_string(data.get_cell_value_by_index(row, column_number - 7))
                result.append(
                    (code, supplier_price, delivery, material_name)
                )
            else:
                output_message_exit(
                    f"Шифр не соответствует шаблону: {supplier_price}",
                    f"цена поставщика в строке {row}",
                )
        else:
            output_message_exit(
                f"Не соответствует шифру расценки: {code!r}", f"шифр в строке {row}"
                )
    return result if result else None


def monitoring_materials_parse(data_place: dict[str:str]) -> int | None:
    """ Разбирает файл мониторинга с ценами на материалы, записывает результат в scv файл. """
    src_file = data_place["materials_src_file"]
    result_csv_file = data_place["material_results_file"]
    #
    result = get_df_material_monitoring(src_file, data_place["materials_sheet_name"])
    df = pandas.DataFrame(
        result, columns=["code", "supplier_price", "delivery", "title"]
    )
    df.to_csv(result_csv_file, sep=",", index=False)
    #
    # parquet_file = create_abspath_file(data_path, parquet_file_name)
    # df.to_parquet(parquet_file)