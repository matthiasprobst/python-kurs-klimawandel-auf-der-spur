# pip install markdown-pdf

from markdown_pdf import MarkdownPdf, Section


def generate_resources_pdf():
    """
    Generates a PDF from the Markdown file containing resources.
    """
    with open("../kursmaterial/Ressourcen.md", "r", encoding="utf-8") as f:
        content = f.read()

    pdf = MarkdownPdf(toc_level=2, optimize=True)
    pdf.add_section(Section(content))

    pdf.save("../kursmaterial/Ressourcen.pdf")
    print("PDF generated successfully.")


if __name__ == "__main__":
    generate_resources_pdf()
