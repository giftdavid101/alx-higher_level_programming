#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argNo = len(sys.argv) - 1

    if argNo == 0:
        print(f"{argNo} arguments")
    else:
        print(f"{argNo} arguments")
        index = 0
        for item in sys.argv:
            print(f"{index} {item}")
            index += 1
