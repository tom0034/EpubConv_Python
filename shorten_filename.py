import os
import sys


def shorten_filename(old_file_path, pre_path):

    clean_file_path = old_file_path[len(pre_path) :]
    clean_file_path = (
        clean_file_path[1:] if clean_file_path[0] is "\\" else clean_file_path
    )

    if len(clean_file_path) < 18:
        return
    new_filename = clean_file_path[:18]

    new_file_path = pre_path + "\\" + new_filename + ".epub"
    i = 1
    while os.path.exists(new_file_path):
        if i >= 10:
            new_file_path = pre_path + "\\" + new_filename[:-1] + str(i) + ".epub"
        else:
            new_file_path = pre_path + "\\" + new_filename + str(i) + ".epub"
        i += 1

    try:
        os.rename(old_file_path, new_file_path)
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except:
        print("error!")


if __name__ == "__main__":
    files = [
        os.path.join(sys.argv[1], f)
        for f in os.listdir(sys.argv[1])
        if os.path.isfile(os.path.join(sys.argv[1], f))
    ]

    for file in files:
        shorten_filename(file, sys.argv[1])

