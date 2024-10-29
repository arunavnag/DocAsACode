import os


def ensure_docs_dir_exists(directory):
    """Ensure the Docs/ directory exists, create it if not."""
    os.makedirs(directory, exist_ok=True)


def save_asciidoc(content, file_name, docs_dir):
    """Save the generated AsciiDoc content into a file."""
    output_file_path = os.path.join(docs_dir, f"{file_name}.adoc")
    with open(output_file_path, 'w', encoding='utf-8') as asciidoc_file:
        asciidoc_file.write(content)
    print(f"AsciiDoc generated successfully! Saved to: {output_file_path}")
