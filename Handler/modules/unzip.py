import zipfile
import os


def extract_archive(archive_path, destination_path):
    with zipfile.ZipFile(archive_path, "r") as zip_ref:
        zip_ref.extractall(destination_path)


def remove_favicon_file(destination_path):
    favicon_path = os.path.join(destination_path, "favicon.ico")
    if os.path.exists(favicon_path):
        os.remove(favicon_path)


def get_directory_summary(directory):
    file_count = 0
    folder_count = 0
    total_size = 0

    for root, dirs, files in os.walk(directory):
        file_count += len(files)
        folder_count += len(dirs)
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))

    return file_count, folder_count, total_size


def print_archive_summary(directory):
    file_count, folder_count, total_size = get_directory_summary(directory)
    total_size_mb = total_size / (1024 * 1024)

    print(f"Сводка об обработанном архиве:")
    print(f"Количество файлов: {file_count}")
    print(f"Количество папок: {folder_count}")
    print(f"Общий размер (в байтах): {total_size}")
    print(f"Общий размер (в мегабайтах): {total_size_mb:.2f} MB")


def main():
    print("Программа разорхиватора")
    archive_path = input("Введите путь до архива: ")
    destination_path = input("Введите путь до папки сохранения: ")

    # Проверяем существование архива и папки сохранения
    if not os.path.exists(archive_path):
        print(f"Ошибка: Архив '{archive_path}' не существует.")
        return
    if not os.path.exists(destination_path):
        print(f"Ошибка: Папка сохранения '{destination_path}' не существует.")
        return

    # Создаем папку FILES внутри указанной папки назначения
    destination_path = os.path.join(destination_path, "FILES")
    os.makedirs(destination_path, exist_ok=True)

    try:
        extract_archive(archive_path, destination_path)
        print("Архив успешно разархивирован.")
        remove_favicon_file(destination_path)
        print("Файл favicon.ico удален.")

        print_archive_summary(destination_path)
    except Exception as e:
        print(f"Произошла ошибка при разархивации: {str(e)}")


if __name__ == "__main__":
    main()
