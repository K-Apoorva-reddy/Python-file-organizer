import os
import shutil
from datetime import datetime

folder_path = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar"]
}

moved_count = 0

log_file = "organizer_log.txt"

try:
    files = os.listdir(folder_path)

    with open(log_file, "a") as log:

        log.write(f"\n\n=== {datetime.now()} ===\n")

        for file in files:

            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):

                extension = os.path.splitext(file)[1].lower()

                for category, extensions in file_types.items():

                    if extension in extensions:

                        destination_folder = os.path.join(
                            folder_path,
                            category
                        )

                        os.makedirs(
                            destination_folder,
                            exist_ok=True
                        )

                        shutil.move(
                            file_path,
                            os.path.join(destination_folder, file)
                        )

                        print(f"Moved: {file} → {category}")

                        log.write(
                            f"Moved: {file} -> {category}\n"
                        )

                        moved_count += 1
                        break

    print("\nOrganization Completed Successfully!")
    print(f"Total Files Organized: {moved_count}")

except Exception as e:
    print("Error:", e)