import os
import time
from write_index import write_index
from config_loader import load_config
from src.asciidoc_writer import ensure_docs_dir_exists, save_asciidoc
from src.doc_generator import generate_context, generate_prompt
from src.git_utils import get_docs_location, read_code_file, clone_repository
from src.openai_client import init_openai_client, call_openai_api


def main():
    # Load config
    config = load_config('../config/azure_config.json')

    # Initialize OpenAI Client
    client = init_openai_client(config)

    # Git clone and locate documentation
    # git_url = os.environ.get("GIT_REPO_URL")
    # if not git_url:
    #     git_url = input("Enter the git repository URL: ")
    git_url = 'https://github.com/arunavnag/TestJavaProject.git'
    local_repo_path = os.path.join(os.path.dirname(__file__), '../repo/local_repo')
    ensure_docs_dir_exists(local_repo_path)
    clone_repository(git_url, local_repo_path)
    local_repo_path = '..\\repo\\local_repo'
    DOCS_DIR = get_docs_location(local_repo_path)
    ensure_docs_dir_exists(DOCS_DIR)

    # Generate AsciiDocs for each code file
    for root, dirs, files in os.walk(local_repo_path):
        # Skip hidden directories (e.g., those starting with '.')
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            file_path = os.path.join(root, file)

            # Ignore unwanted files based on extensions or names
            if file.startswith('.') or file in ('README.md', 'LICENSE'):
                continue

            # Check if the file has one of the desired extensions
            if file.endswith(tuple(config['coding_extensions'])):
                code_content = read_code_file(file_path)

                context = generate_context()
                prompt = generate_prompt(code_content)
                asciidoc_content = call_openai_api(client, context, prompt)

                file_name = os.path.splitext(os.path.basename(file_path))[0]
                save_asciidoc(asciidoc_content, file_name, DOCS_DIR)
                time.sleep(6)

    write_index(DOCS_DIR)

if __name__ == "__main__":
    main()


# 'https://github.com/arunavnag/TestJavaProject.git'