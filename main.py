import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx*")

for filepaths in filepaths:
    df = pd.read_excel(filepaths,sheet_name="Sheet 1")
    pdf = FPDF (orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepaths).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")