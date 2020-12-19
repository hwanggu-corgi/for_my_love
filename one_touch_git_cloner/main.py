import sys
import subprocess

name = "Corgi"
email = [
    "guhyungm7@gmail.com",
    "hwanggumedia@gmail.com",
]


def main(args):
    clone_amt = 0
    unique_amt = 0

    if len(args) != 3:
        print ("앱 사용법♥♥: python3 main.py <Clone amount> <Unique clone amount>")
        return

    try:
        clone_amt = int(args[1])
        unique_amt = int(args[2])
    except:
        print ("여보♥♥ 우리 넘버만 넣어주세요♥♥: python3 main.py 10 2")
        return

    # get arguments of number of unique clones and number of normal clones
    for i in range(clone_amt):
        # clone
        subprocess.run(["rm", "-rf", "cloned_folder"])
        subprocess.run(["git", "clone", "https://github.com/hwanggu-corgi/resume_personal_statement", "cloned_folder"])

    # print message

    for i in range(unique_amt):
        subprocess.run(["rm", "-rf", "cloned_folder"])
        subprocess.run(["", "-rf", "cloned_folder"])
        subprocess.run(["git", "clone", "https://github.com/hwanggu-corgi/resume_personal_statement", "cloned_folder"])

        # clone
    print("Clone successful♥♥")

if __name__ == "__main__":
    args = sys.argv
    print(args)
    main(args)