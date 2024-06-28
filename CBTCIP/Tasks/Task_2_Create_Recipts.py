from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Data for the table
DATA = [
    ["Date", "Name", "Subscription", "Price (Rs.)"],
    ["16/11/2020", "Full Stack Development with Python Django - Live",
     "Lifetime", "10,999.00/-"],
    ["16/11/2020", " Classes: Live Session", "6 months", "9,999.00/-"],
    ["Sub Total", "", "", "20,00.00/-"],
    ["Discount", "", "", "-1,000.00/-"],
    ["Total", "", "", "15,998.00/-"],
]

# Create a PDF document
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

# Standard stylesheet
styles = getSampleStyleSheet()

# Title style
title_style = styles["Heading1"]
title_style.alignment = 1

# Title paragraph
title = Paragraph("Nidhi_Infotech", title_style)

# Table style
style = TableStyle([
    ("BOX", (0, 0), (-1, -1), 1, colors.black),  # Border for all cells
    ("GRID", (0, 0), (4, 4), 1, colors.black),  # Grid lines
    ("BACKGROUND", (0, 0), (3, 0), colors.gray),  # Gray header background
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # White header text
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center alignment in all cells
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),  # Alternate row background
])

# Create the table
table = Table(DATA, style=style)

# Build the PDF document
pdf.build([title, table])

print("Receipt generated successfully: receipt.pdf")
