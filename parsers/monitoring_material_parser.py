from icecream import ic
from config import (
    SourceData,
    anchors,
    SUPPLIER_PRICE_COLUMN_DELTA,
    HEADER_HEIGHT,
    RELATIVE_CODE_POSITION,
    variations_delivery_value
)
from files_features import output_message_exit
from public import clear_code, is_quote_code, get_float, clear_string


def get_data_material_monitoring(file_path: str, file_name: str, sheet_name: str) -> list[tuple[str, float]] | None:
    """
    Получить данные из файла мониторинга.
    Возвращает список кортежей (шифр, 'отпускная цена поставщика')
    Находит якорную колонку. Высчитывает столбец в котором записаны цены поставщика.
    Высчитывает строку с которой будет искать шифры расценок.
    Считывает шифр расценки и цену поставщика.
    """
    result = []
    data = SourceData(file_path, file_name, sheet_name)
    anchor_position = data.find_cell_with_cleaning(anchors["base_column_value"].lower())
    if anchor_position:
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
                        f"Не соответствует шаблону: {supplier_price}",
                        f"цена поставщика в строке {row}",
                    )
            else:
                output_message_exit(
                    f"Не соответствует шифру расценки: {code!r}", f"шифр в строке {row}"
                    )
        return result if result else None