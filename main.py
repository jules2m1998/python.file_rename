import pathlib
import re
import os


def replace_files_name_episode_number(directory: str):
    """
    Replace the file by episode number
    :return:
    """
    files = pathlib.Path(directory).glob('*')
    for file in files:
        file_name = file.name
        match = re.search(r"\w+\d{2,}?", file_name)
        if match:
            episode = match.group(0)
            extension = file.suffix
            new_path = file.parent / str(episode + extension)
            if not os.path.exists(new_path):
                os.rename(file, file.parent / str(episode + extension))
                print(f'{file.parent / str(episode + extension)} renommé')
    print("Done")


if __name__ == '__main__':
    directory = input("Entrez le chemin du dossier: ")
    replace_files_name_episode_number(directory)