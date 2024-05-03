import os
import pathlib


from files_features.message import output_message_exit


def handle_location(data_path: str, data_file: str):
    """
    Создает абсолютные маршруты к файлу с данными и файлу с результатами
    :param data_path: Путь к файлу с данными
    :param data_file: Имя файла с данными
    :return: Полные маршруты к файлу с данными и результатами
    """
    src_file = os.path.abspath(os.path.join(data_path, data_file))
    output_file_name = f"{data_file.split('.')[0]}_groups.xlsx"
    output_path = os.path.join(os.getcwd(), "output")
    output_file = os.path.join(output_path, output_file_name)

    if not os.path.exists(src_file):
        output_message_exit("фал с данными не найден", f"{src_file!r}")
    if not os.path.isdir(output_path):
        output_message_exit("папка для вывода фала с результатом не найдена", f"{output_path!r}")
    return src_file, output_file


def construct_abs_file_name(path: str, file_name: str) -> str:
    """ Создает абсолютный маршрут к файлу. """
    if not os.path.isdir(path):
        output_message_exit("папка не найдена", f"{path!r}")
    return os.path.join(path, file_name)

def create_abspath_file(path: str=None, file_name: str=None) -> str | None:
    """ Создает абсолютный маршрут к файлу. Если путь не указан то берется место запуска."""
    if file_name:
        path = pathlib.Path(path).resolve() if path else pathlib.Path(__file__).parent.resolve()
        return pathlib.Path.joinpath(path, file_name).__str__()
    return None



def file_exists(path: str) -> bool:
    """ проверяет то что маршрут существует и это файл."""
    return pathlib.Path(path).is_file()


def generate_result_file_name(file_path: str, supplement: int, index: int) -> str:
    """Добавляет к имени файла номер дополнения и индекса."""
    file_path = pathlib.Path(file_path)
    # file_path = pathlib.Path(file_path).resolve()
    new_name = f"{file_path.stem}_{supplement}_{index}"
    return str(file_path.with_name(new_name).with_suffix(file_path.suffix))
