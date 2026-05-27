from pypdf import PdfReader

r = PdfReader("W8.pdf")
lines = []
for i, page in enumerate(r.pages):
    text = page.extract_text() or ""
    lines.append(f"=== PAGE {i + 1} ===\n{text}")
open("w8_extract.txt", "w", encoding="utf-8").write("\n\n".join(lines))
