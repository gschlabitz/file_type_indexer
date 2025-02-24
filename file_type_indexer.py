import os
import argparse

def count_file_types(path):
    file_types = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_ext = os.path.splitext(file)[1]
            if file_ext not in file_types:
                file_types[file_ext] = 1
            else:
                file_types[file_ext] += 1
    return file_types

def print_csv(file_types):
    print("File Type,Count")
    for file_ext, count in file_types.items():
        print(f"{file_ext},{count}")

def main():
    parser = argparse.ArgumentParser(description="File type indexer")
    parser.add_argument("path", help="Absolute path to scan for files and count them by type.")
    args = parser.parse_args()
    file_types = count_file_types(args.path)
    print_csv(file_types)

if __name__ == "__main__":
    main()