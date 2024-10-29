import os

def write_index(asciidoc_dir):
    # List all AsciiDoc files in the directory
    asciidoc_files = [f for f in os.listdir(asciidoc_dir) if f.endswith('.adoc')]

    # Create the index.adoc file
    with open(os.path.join(asciidoc_dir, 'index.adoc'), 'w') as index_file:
        # Write the AsciiDoc header
        index_file.write('= Index File\n')  # Change this to your desired title
        index_file.write(':toc: macro\n\n')  # Add a table of contents if needed
        index_file.write('== List of AsciiDoc Files\n\n')

        # Write links to each AsciiDoc file
        for asciidoc_file in asciidoc_files:
            # Generate the link format for each file
            index_file.write(f'* link:{asciidoc_file}[{os.path.splitext(asciidoc_file)[0]}]\n')

    print(f'Index file created at: {os.path.join(asciidoc_dir, "index.adoc")}')


