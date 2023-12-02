from fpdf import FPDF, Align, YPos

name = input('Name: ')

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font('helvetica', 'B', 24)
pdf.cell(40, 10, "CS50 Shirtificate" , align = 'X', center = True)
pdf.image('shirtificate.png',x = Align.C, y = 100, h = 150.0)
pdf.set_text_color(r=255,b=255,g=255)
pdf.set_y(150)
pdf.cell(40, 10, f"{name} took CS50"  , align = 'X', center = True)

pdf.output("shirtificate.pdf")
