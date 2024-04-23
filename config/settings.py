from collections import namedtuple

data_path = r"C:\Users\kazak.ke\Documents\Задачи\5_Надя\Мониторинг"

SUPPLIER_PRICE_COLUMN_DELTA = 3
HEADER_HEIGHT = 3
RELATIVE_CODE_POSITION = 11

variations_delivery_value = ("с доставкой", "c доставкой")


CellPosition = namedtuple(typename="CellPosition", field_names=["row", "column"])
CellPosition.__annotations__ = {"row": int, "column": str}
