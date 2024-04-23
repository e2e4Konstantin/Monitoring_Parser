import string
import re
# from fastnumbers import isfloat, isint, try_float,  try_int


# from config.excel_config import SourceData

_re_compiled_patterns = {
    'subsection_groups': re.compile(r"(^\d+\.\d+-\d+-)(\d+)\s*"),
    'wildcard': re.compile(r"[\t\n\r\f\v\s+]+"),
    'code_valid_chars': re.compile(r"[^\d+.-]+"),
    'digits': re.compile(r"[^\d+]+"),
    'digits_dots': re.compile(r"[^\d+.]+"),
    'quote_code': re.compile(r"\d+\.\d+(-\d+){2}"),
}

def generate_column_names(num_columns: int) -> tuple[str, ...] | None:
    """
    Возвращает кортеж с именами колонок, которые соответствуют буквенным именам колонок в excel.
    Указанной длинны.
    """
    if num_columns <= 0:
        raise ValueError(f"num_columns <= 0: {num_columns}")
    columns = list(string.ascii_uppercase)
    if len(columns) >= num_columns:
        return tuple(columns[:num_columns])
    gen = columns
    for char in columns:
        gen_next = tuple(char + c for c in columns)
        gen = (*gen, *gen_next)
        if len(gen) >= num_columns:
            return tuple(gen[:num_columns])
    return None


def clear_string(src_text: str | None) -> str | None:
    """Очищает строку от спецсимволов, двойных пробелов.
    """
    if src_text is None:
        return None
    if isinstance(src_text, str):
        return re.sub(r"\s+", " ", re.sub("^\s+|\n|\r|\t|\v|\f|\s+$", " ", src_text))


def get_float(text: str) -> float | None:
    """Конвертирует строку в число с плавающей точкой.."""
    text = text.replace(",", ".", 1).strip()
    try:
        return float(text)
    except ValueError:
        return None


def get_integer(string: str) -> int | None:
    """Конвертирует строку в целое число."""
    try:
        return int(string)
    except ValueError:
        return None

def clear_code(source: str = None) -> str | None:
    """Удаляет из строки все символы кроме (чисел, '.', '-')"""
    return re.sub(_re_compiled_patterns["code_valid_chars"], r"", source)

def is_quote_code(code: str) -> bool:
    """Проверяет, совпадает ли код с шаблоном расценки."""
    return _re_compiled_patterns["quote_code"].match(code) is not None



if __name__ == "__main__":
    # x = generate_column_names(13)
    # print(x)

    r = is_quote_code("1.1-1-2204")
    print(r)