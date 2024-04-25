import pathlib


p = r"C:\Users\kazak.ke\result.csv"

# def generate_result_file_name(abs_file: str, supplement: int, index: int) -> str:
#     file_path = Path(abs_file)
#     filename = file_path.name
#     body = file_path.stem
#     extension = file_path.suffix
#     #
#     x = Path(f"{body}_{supplement}_{index}").with_suffix(extension)
#     return x

def generate_result_file_name(file_path: str, supplement: int, index: int) -> str:
    """Добавляет к имени файла номер дополнения и индекса."""
    file_path = pathlib.Path(file_path).resolve()
    new_name = f"{file_path.stem}_{supplement}_{index}"
    return str(file_path.with_name(new_name).with_suffix(file_path.suffix))

# def generate_result_file_name(abs_file: str, supplement: int, index: int) -> str:
#     """Добавляет к имени файла номер дополнения и индекса."""
#     file_path = Path(abs_file).resolve()
#     new_file_name = Path(f"{file_path.stem}_{supplement}_{index}").with_suffix(
#         file_path.suffix
#     )
#     x = file_path.parent.joinpath(new_file_name)
#     return str(x)


if __name__ == "__main__":
    a = generate_result_file_name(p, 71, 210)

    print("\n",a)