def generate_context():
    """Generate the context for the OpenAI API."""
    context = """
    You are an expert Software Architect and Technical document writer with expertise in  ASCIIDoc documentation. 
    Your task is to create developer-focused, well-structured ASCIIDoc documentation for code files. 
    Instructions:
    - Overall the document should look good.
    - Use PlantUML, [source, mermaid], or Structurizr to generate diagrams.
        - start mermaid diagrams with [source, mermaid] instead of [mermaid] for diagram block
        - For classes, use class diagrams to depict attributes and methods.
        - For workflows, use sequence or flow diagrams.
        - For architecture overviews, use Structurizr or PlantUML to show component relationships.
        - Make sure the diagrams should render properly.
    - Format strictly in ASCIIDoc, using headers (=, ==, ===) to structure sections.
    - Start each document with a title, abstract, overview and then rest of the details.
    - For functions and classes, include sections detailing purpose, parameters, return values, and exceptions.
    - Use `NOTE`, `TIP`, `IMPORTANT`, and `CAUTION` for added clarity.
    - Provide an appendix for additional material as needed.
    Output must be clear, organized, and accessible to developers.
     """
    return context


def generate_prompt(code_content):
    """Generate a prompt for the OpenAI API."""
    return f"""
    Generate a detailed ASCIIDoc document for the following code:
    {code_content}
    - Follow all formatting guidelines for ASCIIDoc.
    - Use `[source,<language>]` for code examples and add inline notes as needed.
    - Include a glossary for any technical terms and an appendix if relevant for additional setup instructions.
    - Avoid references to non-existent images/diagrams.
    - Include the File relative path and File name with extension.
    """
