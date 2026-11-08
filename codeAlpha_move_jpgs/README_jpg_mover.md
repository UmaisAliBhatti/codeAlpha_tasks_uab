# Task 3: Task Automation with Python (JPG File Mover)

A small script that automates a repetitive job: moving all `.jpg` files from a folder into a new folder.

## How to Run

```
python move_jpgs_simple.py
```

Requires Python 3. No extra packages needed.

## How to Use

1. Run the script.
2. Enter the folder that contains your pictures, or press Enter to use the current folder.
3. The script creates a `jpg_images` folder inside it (if it does not exist yet).
4. Every `.jpg` file is moved into `jpg_images`.
5. A count of moved files is printed at the end.

## Example

Before:

```
photos/
    beach.jpg
    family.JPG
    notes.txt
```

After:

```
photos/
    notes.txt
    jpg_images/
        beach.jpg
        family.JPG
```

## Features

- Creates the destination folder automatically
- Matches `.jpg` regardless of case (`.JPG` works too)
- Skips a file if one with the same name is already in the destination, so nothing is overwritten
- Prints each file as it is moved

## Notes

- Only files directly inside the chosen folder are moved. Subfolders are not searched.
- Files are moved, not copied, so they no longer exist in the original location.

## Concepts Used

- `os` module (listing files, building paths, creating folders)
- `shutil` module (moving files)
- File handling and string methods (`endswith`, `lower`)

## Files

| File | Description |
|------|-------------|
| `move_jpgs_simple.py` | The automation script |
