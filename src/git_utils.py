import os
import subprocess


def clone_repository(git_url, local_path):
    """Clone a git repository to a local path if the directory is empty."""
    if os.path.isdir(local_path) and os.listdir(local_path):
        print(f"Directory '{local_path}' already exists and is not empty.")
    else:
        subprocess.run(["git", "clone", git_url, local_path], check=True)
        print(f"Cloned repository to '{local_path}'.")



def get_docs_location(local_repo_path):
    """Retrieve the documentation directory location from documentation.md."""
    doc_file_path = os.path.join(local_repo_path, 'documentation.md')
    if os.path.isfile(doc_file_path):
        with open(doc_file_path, 'r') as doc_file:
            doc_path = doc_file.read().strip()
        document_path = os.path.join(local_repo_path, doc_path.split("=")[-1].replace("""""", ""))
        return document_path
    else:
        raise FileNotFoundError(f"'documentation.md' not found in '{local_repo_path}'")


def read_code_file(file_path):
    """Read the code file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as code_file:
            return code_file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' does not exist. Please check the path.")
    except PermissionError:
        raise PermissionError(f"Permission denied while accessing '{file_path}'.")
    except Exception as e:
        raise IOError(f"An unexpected error occurred while reading '{file_path}': {e}")
