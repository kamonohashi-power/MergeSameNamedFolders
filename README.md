# Merge Same Named Folders

Say goodbye to nested folders (Matryoshka)!

This Python script automatically detects and merges subfolders with the same name into their parent directory. It moves all files while preserving metadata (timestamps and file attributes) and removes the empty subfolder.

## Features
- Merges folders with the same name into their parent directory
- Preserves file metadata (timestamps and attributes)
- Skips existing files to prevent overwriting
- Automatically removes empty nested folders

## Installation
No additional dependencies are required, as the script uses Python's built-in libraries.

## Usage
1. Run the script:
   ```sh
   python merge_folders.py
   ```
2. Enter the target folder path when prompted.

Alternatively, modify the script to set a default folder path.

## Example
Before:
```
Root/
├── AAA/
│   ├── AAA/
│   │   ├── file1.txt
│   │   ├── file2.txt
```
After:
```
Root/
├── AAA/
│   ├── file1.txt
│   ├── file2.txt
```

## License
This project is licensed under the MIT License.
