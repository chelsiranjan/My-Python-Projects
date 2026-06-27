import os
import shutil
#import time

ROOT_FOLDER = r'C:\Users\Chelsi\Documents'

FILE_TYPES = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.jfif': 'Images',
    '.pdf': 'PDFs',
    '.mp3': 'Audio',
    '.webm': 'Videos',
    '.mp4': 'Videos',
    '.txt': 'TextFiles',
    '.zip': 'Archives',
    '.sql': 'SQL',
    '.py': 'Python',
    '.csv': 'CSVfiles',
    '.pbix': 'PowerBI',
    '.xlsx': 'Excel',
    '.xls': 'Excel',
    '.json': 'JSONfiles',
    '.exe': 'Setup',
    '.html': 'HtmlFiles',
    '.ipynb': 'Jupyter'}

while True:
    print('Checking folders...')

    for root, dirs, files in os.walk(ROOT_FOLDER):

        # skip organizer folders
        dirs[:] = [d for d in dirs if d not in FILE_TYPES.values()]

        for file in files:

            file_path = os.path.join(root, file)

            extension = os.path.splitext(file)[1].lower()

            if extension not in FILE_TYPES:
                continue

            category = FILE_TYPES[extension]

            # category folder inside current folder
            destination_folder = os.path.join(root, category)
            os.makedirs(destination_folder, exist_ok=True)

            destination_file = os.path.join(destination_folder, file)

            try:
                # duplicate names
                if os.path.exists(destination_file):
                    name, ext = os.path.splitext(file)
                    counter = 1

                    while os.path.exists(destination_file):
                        destination_file = os.path.join(
                            destination_folder,
                            f"{name}_{counter}{ext}")
                        counter += 1

                shutil.move(file_path, destination_file)

                print(f'Moved: {file} -> {destination_folder}')

            except Exception as e:
                print(f'Error moving {file}: {e}')

    #time.sleep(5)
