import sys
import os
from pypdf import PdfReader, PdfWriter

def usage():
    print("\nUsage:")
    print("  python delete_page.py <input_pdf> <page_to_delete>")
    print("\nExample:")
    print("  python delete_page.py source.pdf 4")
    sys.exit(1)

# -----------------------------
# Validate argument count
# -----------------------------
if len(sys.argv) != 3:
    print("ERROR: Wrong number of arguments.")
    usage()

input_pdf = sys.argv[1]
page_arg = sys.argv[2]

# -----------------------------
# Validate input PDF exists
# -----------------------------
if not os.path.isfile(input_pdf):
    print(f"ERROR: Input PDF does not exist: {input_pdf}")
    usage()

# -----------------------------
# Validate page number
# -----------------------------
if not page_arg.isdigit():
    print(f"ERROR: Page number must be a positive integer, got: {page_arg}")
    usage()

page_to_delete = int(page_arg) - 1 #ZERO based index

if page_to_delete < 0:
    print("ERROR: Page number cannot be negative.")
    usage()

# -----------------------------
# Load PDF and validate page range
# -----------------------------
reader = PdfReader(input_pdf)
total_pages = len(reader.pages)

if page_to_delete >= total_pages:
    print(f"ERROR: Page number {page_to_delete} is out of range.")
    print(f"PDF has only {total_pages} pages.")
    usage()

# -----------------------------
# Perform deletion
# -----------------------------
output_pdf = f"output_without_page_{page_to_delete+1}.pdf" #ZERO based index to counter
writer = PdfWriter()

for index, page in enumerate(reader.pages):
    if index != page_to_delete:
        writer.add_page(page)

with open(output_pdf, "wb") as f:
    writer.write(f)

print(f"\nSUCCESS: Page {page_to_delete+1} deleted.") #ZERO based index to counter
print(f"Output written to: {output_pdf}")
