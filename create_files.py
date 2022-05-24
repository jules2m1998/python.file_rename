from uuid import uuid4
import random


def create_files(count: int = 100):
    f"""
    Create files
    :param count: {int}
    :return: 
    """
    for i in range(count):
        larg = random.randint(3, 4)
        replace_start = 'One Piece (VF) - One piece - '
        replace_end = ' VF - 0603 - Voiranime'
        fill = str(i).zfill(larg)
        file_name = f"test/{replace_start} {fill} {replace_end}.txt"
        with open(file_name, "w") as f:
            f.write(f"{str(uuid4()) * 1000}")
            print(file_name)
    print('end')


if __name__ == "__main__":
    create_files()

