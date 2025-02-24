# File Type Indexer
A CLI tool to recursively count all files by type in a given folder.

Download this repository to a folder of your choice, e.g. your Downloads folder.

On macOS, open the Terminal app then type these commands:

```sh
cd Downloads
python file_type_indexer.py ~/Documents
```

This will scan your Documents folder and print out the file count by type in this format:

```sh
File Type, Count
.txt,12
.docx,53
.xlsx,42
```

If you would like to open the output in a spreadsheet, save it to a .csv file first:

```
python file_type_indexer.py ~/Documents > doc_index.csv
```

The CSV file will be created in the same folder that the script is located in. Open it with your preferred spreadsheet app.

**Hint**: External drives are found in the Volumes folder, so an example path would look like: `/Volumes/External_Drive_Name/sub_folder`