# Moves all .jpg files from one folder into a new folder
import os
import shutil

source = input("Which folder has the pictures? (Enter = current folder): ")
if source == "":
    source = "."

new_folder = os.path.join(source, "jpg_images")

# make the new folder if it isn't there yet
if not os.path.exists(new_folder):
    os.mkdir(new_folder)

count = 0

for file_name in os.listdir(source):

    # only look at .jpg files (lower() so .JPG works too)
    if file_name.lower().endswith(".jpg"):
        old_path = os.path.join(source, file_name)
        new_path = os.path.join(new_folder, file_name)

        # don't overwrite a file that is already there
        if os.path.exists(new_path):
            print("Skipped (already exists):", file_name)
        else:
            shutil.move(old_path, new_path)
            print("Moved:", file_name)
            count = count + 1

print("\nFinished. Moved", count, "file(s).")
