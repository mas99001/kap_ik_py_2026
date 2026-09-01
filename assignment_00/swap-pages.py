from pypdf import PdfReader, PdfWriter

input_pdf = "input.pdf"
output_pdf = "DAP-06-09.pdf"

reader = PdfReader(input_pdf)
writer = PdfWriter()

# Total pages
n = len(reader.pages)

# Build new order:
# 0–11 (pages 1–12)
# 14–15 (pages 15–16)
# 12–13 (pages 13–14)
new_order = list(range(0, 12)) + [14, 15] + [12, 13]

# Add pages in new order
for idx in new_order:
    writer.add_page(reader.pages[idx])

with open(output_pdf, "wb") as f:
    writer.write(f)
