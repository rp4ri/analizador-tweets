# coding: cp1252

# main, run all python scripts in folder scripts using for f in *.py; do python "$f"; done
def main():
    import os
    for f in os.listdir("scripts"):
        if f.endswith(".py"):
            print(f)
            os.system("python scripts/" + f)
    print("All scripts executed")
if __name__ == "__main__":
    main()