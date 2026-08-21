import sys
import os
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors


# ------------------------------------------------------------
# Create a centered, wrapped title page for each PDF
# ------------------------------------------------------------
def create_title_page(text, temp_path, font_size=10):
    c = canvas.Canvas(temp_path, pagesize=letter)
    width, height = letter

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Helvetica-Bold"
    style.fontSize = font_size
    style.leading = font_size + 4
    style.textColor = colors.blue
    style.alignment = TA_CENTER

    para = Paragraph(text, style)
    max_width = width * 0.8

    w, h = para.wrap(max_width, height)
    x = (width - w) / 2
    y = (height + h) / 2

    para.drawOn(c, x, y)
    c.save()


# ------------------------------------------------------------
# Create a Table of Contents page WITH PAGE NUMBERS
# ------------------------------------------------------------
def create_toc_page(toc_items, page_map, temp_path, font_size=10):
    c = canvas.Canvas(temp_path, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(width / 2, height - 80, "Table of Contents")

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Helvetica"
    style.fontSize = font_size
    style.leading = font_size + 4
    style.textColor = colors.blueviolet
    style.alignment = TA_LEFT

    y = height - 140
    max_width = width * 0.85

    for item in toc_items:
        toc_line = f"{item}  ..........  Page {page_map[item] + 1}"

        para = Paragraph(toc_line, style)
        w, h = para.wrap(max_width, height)
        para.drawOn(c, 50, y - h)

        y -= (h + 10)

    c.save()


# ------------------------------------------------------------
# Main merge function with TOC + title pages + bookmarks
# ------------------------------------------------------------
def merge_pdfs_with_toc(folder_path, output_filename="Output_XX.pdf"):
    print("Source: "+ folder_path)
    print("Destination: "+ output_filename)
    merger = PdfWriter()

    pdf_files = sorted(
        f for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf") and f != output_filename
    )

    if not pdf_files:
        print("No PDF files found.")
        return

    toc_items = []
    page_map = {}  # filename → starting page number

    toc_pdf_path = os.path.join(folder_path, "_toc_temp.pdf")
    title_pdf_path = os.path.join(folder_path, "_title_temp.pdf")

    # ------------------------------------------------------------
    # FIRST PASS — calculate page numbers BEFORE creating TOC
    # ------------------------------------------------------------
    current_page = 1  # TOC will be page 1

    for pdf in pdf_files:
        toc_items.append(pdf)
        file_path = os.path.join(folder_path, pdf)

        # Title page = 1 page
        pdf_reader = PdfReader(file_path)
        num_pages = 1 + len(pdf_reader.pages)

        page_map[pdf] = current_page
        current_page += num_pages

    # ------------------------------------------------------------
    # Create TOC page with page numbers
    # ------------------------------------------------------------
    create_toc_page(toc_items, page_map, toc_pdf_path)
    toc_reader = PdfReader(toc_pdf_path)
    merger.append(toc_reader)

    # ------------------------------------------------------------
    # SECOND PASS — merge PDFs with title pages
    # ------------------------------------------------------------
    for pdf in pdf_files:
        file_path = os.path.join(folder_path, pdf)
        print(f"Adding: {pdf}")

        # Create title page
        create_title_page(pdf, title_pdf_path, font_size=14)
        title_reader = PdfReader(title_pdf_path)
        pdf_reader = PdfReader(file_path)

        # Add bookmark pointing to title page
        merger.add_outline_item(pdf, len(merger.pages))

        # Append title page
        merger.append(title_reader)

        # Append actual PDF
        merger.append(pdf_reader)

    # ------------------------------------------------------------
    # Save final output
    # ------------------------------------------------------------
    output_path = os.path.join(folder_path, output_filename)
    merger.write(output_path)
    merger.close()

    # Cleanup
    os.remove(toc_pdf_path)
    os.remove(title_pdf_path)

    print(f"\nMerged {len(pdf_files)} PDFs with TOC (page numbers) → {output_path}")


# ------------------------------------------------------------
# Usage
# ------------------------------------------------------------
#if __name__ == "__main__":
    #my_pdf_folder = r"D:\MSDN.TPM\A.4.K\AI-PYT-GIT\KAP-IK\KAP-AIML\my-pdf-merge\doc_10"
    #merge_pdfs_with_toc(my_pdf_folder)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python merge.py <doc_folder_name>")
        sys.exit(1)

    doc_namei = sys.argv[1]   # e.g., "doc_10"
    doc_namei = sys.argv[1]   # e.g., "doc_10"
    print("Directory input is :", doc_namei)

    # Warn if spaces exist
    if " " in doc_namei:
        print("ERROR: Spaces are not allowed in the folder name:", doc_namei)
        sys.exit(1)   # stop the script

    print("Directory input is : " + doc_namei)
    doc_name = doc_namei.replace(".", "").replace("\\", "")
    print("Directory to be used: "+ doc_name)
    base_dir = os.getcwd()   # dynamic base directory
    my_pdf_folder = os.path.join(base_dir, doc_name)

    if os.path.isdir(my_pdf_folder):
        print("WORKING on THE FOLDER: ", my_pdf_folder)
        merge_pdfs_with_toc(my_pdf_folder, my_pdf_folder + ".pdf")
    else:
        print("Folder does NOT exist:", my_pdf_folder)
