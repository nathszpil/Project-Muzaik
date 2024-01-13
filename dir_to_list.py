import os


def list_files(directory):
    """
    Get a list of all files in the specified directory.

    Parameters:
    - directory (str): The path to the directory.

    Returns:
    - list: A list containing the names of all files in the directory.
    """
    files = []
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if the path is a file (not a directory)
        if os.path.isfile(filepath):
            files.append(filename)
    return files


# Example usage:
directory_path = "album_covers"
file_list = list_files(directory_path)

print("List of files in the directory:")
print(file_list)
