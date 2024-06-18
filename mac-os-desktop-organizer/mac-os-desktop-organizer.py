import os
import shutil

def rename_if_duplicate(dest_path, filename):
    """
    Renames the file if there is a duplicate by appending a number to the filename.
    """
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    # Generate a new filename until no duplicate is found
    while os.path.exists(os.path.join(dest_path, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1

    return new_filename

# Get list of root level items on desktop
desktop_items = os.listdir(os.path.expanduser('~/Desktop'))

# Create a dictionary of file extensions and folders to save those file types in
folders = {
    'Images': ['.jpg', '.png', '.jpeg', '.gif', '.webp', '.bmp', '.tiff', '.svg'],
    'Documents': ['.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf', '.odt'],
    'Audio': ['.wav', '.mp3', '.aac', '.flac', '.ogg'],
    'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.mkv', '.flv'],
    'Scripts': ['.py', '.sh', '.bat', '.js', '.php', '.rb', '.pl']
}

# Loop through each item on the desktop
for item in desktop_items:
    item_path = os.path.join(os.path.expanduser('~/Desktop'), item)
    # Get item's extension
    _, file_extension = os.path.splitext(item_path)
    # Loop through each folder in the folders dictionary
    for folder_name, extensions in folders.items():
        # Check if file extension is in the list of extensions
        if file_extension.lower() in extensions:
            # Create path to the folder
            folder_path = os.path.join(os.path.expanduser('~/Desktop'), folder_name)
            # Check if folder exists
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # Rename file if there is a duplicate
            new_filename = rename_if_duplicate(folder_path, item)
            new_item_path = os.path.join(folder_path, new_filename)

            # Move the item into the folder with the new name
            shutil.move(item_path, new_item_path)
            # Break out of the loop
            break