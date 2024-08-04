from fpdf import FPDF


def main():
    user = input("Name: ")
    print(convert(user))


def convert(name):
    # Create page, format and orientation
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    # Add image
    pdf.image("shirtificate/shirtificate.png", x=20, y=60)
    # Set text font and font size
    pdf.set_font("helvetica", size=12)
    # Add text in the middle
    pdf.cell(text=f"{name} took CS50")
    # Add text on top
    pdf.cell(text="CS50 Shirtificate")
    # Output pdf
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
