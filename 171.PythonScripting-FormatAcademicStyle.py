###
# This script is a Python program that reads a plain text file.
# Input.txt.
# Formats its content according to specific requirements and saves it as a microsoft Word document.
# Output Docs.
# The formatting requirements are one inch margins line spacing set to 1.5 font size 12 times new Roman
# font and left aligned paragraphs.
# The program uses the Python Docs library to create and manipulate word documents.
###

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Cm

def format_paragraph(paragraph):
    # Set line spacing to 1.5
    paragraph_format = paragraph.paragraph_format
    paragraph_format.line_spacing = 1.5

    # Set font size to 12 and font family to Times New Roman
    for run in paragraph.runs:
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'

        # Set justification to left
        paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

def main():
    # Read input text
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Create a new Word document
    doc = docx.Document()

    # Set margins to 1 inch (2.54 cm) on all sides
    for section in doc.sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(2.54)
        section.right_margin = Cm(2.54)

    # Split input text into paragraphs
    paragraphs = text.split('\n')

    # Add paragraphs to the document and format them
    for paragraph in paragraphs:
        para = doc.add_paragraph(paragraph)
        format_paragraph(para)

    # Save the formatted document as 'output.docx'
    doc.save('output.docx')