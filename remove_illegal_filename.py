import os
import sys
import re


def remove_illegal(old_file_path, pre_path):

    clean_file_path = old_file_path[len(pre_path) :]
    if os.name == "nt":
        clean_file_path = (
            clean_file_path[1:] if clean_file_path[0] is "\\" else clean_file_path
        )
    else:
        clean_file_path = (
            clean_file_path[1:] if clean_file_path[0] is "/" else clean_file_path
        )

    ## remove extension
    clean_file_path = os.path.splitext(clean_file_path)[0]

    ## regex to rename
    new_filename = re.sub("[^\w\d\s\.@-]", "", clean_file_path)
    new_filename = re.sub("\s+", "", new_filename)
    # new_filename = re.sub(r"[\/:\"*?<>|]+", "", new_filename)
    new_filename.strip()

    if os.name == "nt":
        new_file_path = pre_path + "\\" + new_filename + ".epub"
    else:
        new_file_path = pre_path + "/" + new_filename + ".epub"
    i = 1
    while os.path.exists(new_file_path):
        if os.name == "nt":
            if i >= 10:
                new_file_path = pre_path + "\\" + new_filename[:-1] + str(i) + ".epub"
            else:
                new_file_path = pre_path + "\\" + new_filename + str(i) + ".epub"
        else:
            if i >= 10:
                new_file_path = pre_path + "/" + new_filename[:-1] + str(i) + ".epub"
            else:
                new_file_path = pre_path + "/" + new_filename + str(i) + ".epub"
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
        remove_illegal(file, sys.argv[1])

