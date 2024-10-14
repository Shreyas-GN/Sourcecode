import os
import shutil

# Define the directory to organize and the target folders
DIRECTORY_TO_ORGANIZE = 'path/to/your/directory'  # Change this to your directory path
TARGET_FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.gz', '.rar']
}

def create_target_folders():
    """Create target folders if they don't exist."""
    for folder in TARGET_FOLDERS.keys():
        folder_path = os.path.join(DIRECTORY_TO_ORGANIZE, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files():
    """Organize files into corresponding folders based on their extensions."""
    for filename in os.listdir(DIRECTORY_TO_ORGANIZE):
        file_path = os.path.join(DIRECTORY_TO_ORGANIZE, filename)

        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()

            # Move the file to the corresponding folder
            moved = False
            for folder, extensions in TARGET_FOLDERS.items():
                if file_extension in extensions:
                    target_folder_path = os.path.join(DIRECTORY_TO_ORGANIZE, folder)
                    shutil.move(file_path, target_folder_path)
                    print(f'Moved: {filename} -> {folder}')
                    moved = True
                    break

            if not moved:
                print(f'No matching folder for: {filename}')

if __name__ == '__main__':
    create_target_folders()
    organize_files()
    print('File organization completed.')
