import os
import shutil

print("Merge Same Named Folders")
print("Say goodbye to nested folders (Matryoshka)")
print()

def copy_with_metadata(src, dest):
    shutil.copy2(src, dest)
    st = os.stat(src)
    os.chmod(dest, st.st_mode)

def merge_same_named_folders(root_folder):
    for parent, dirs, _ in os.walk(root_folder, topdown=False):
        for folder in dirs:
            subfolder_path = os.path.join(parent, folder, folder)
            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                parent_folder_path = os.path.join(parent, folder)

                for item in os.listdir(subfolder_path):
                    src = os.path.join(subfolder_path, item)
                    dest = os.path.join(parent_folder_path, item)

                    if os.path.exists(dest):
                        print(f"Skip: {dest} already exists")
                    else:
                        if os.path.isdir(src):
                            shutil.copytree(src, dest, copy_function=shutil.copy2)
                        else:
                            copy_with_metadata(src, dest)
                        print(f"Copy: {src} → {dest}")

                shutil.rmtree(subfolder_path)
                print(f"Delete: {subfolder_path}")

if __name__ == "__main__":
    target_folder = input("Enter the folder path (including subfolders): ")
    if os.path.exists(target_folder) and os.path.isdir(target_folder):
        merge_same_named_folders(target_folder)
        print("Processing completed!")
    else:
        print("The specified folder does not exist.")
