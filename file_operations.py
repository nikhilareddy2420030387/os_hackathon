# file_operations.py

def write_to_file():
    try:
        file = open("test.txt", "w")
        file.write("Hello OS Lab\n")
        file.write("System Call Trace Experiment\n")
        print("Data written to file successfully.")
        file.close()
    except Exception as e:
        print("Error while writing:", e)


def read_from_file():
    try:
        file = open("test.txt", "r")
        content = file.read()
        print("Reading data from file...")
        print("File Content:\n", content)
        file.close()
    except Exception as e:
        print("Error while reading:", e)


def main():
    print("----- File Operations Started -----")
    write_to_file()
    read_from_file()
    print("----- File Operations Completed -----")


if __name__ == "__main__":
    main()