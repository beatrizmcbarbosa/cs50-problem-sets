from fpdf import FPDF


def main():
    user = input("Name: ")
    print(convert(user))

def convert(name):
    # Create page, format and orientation
    pdf = FPDF()
    pdf.add_page(orientation="portrait", format="A4")

    # Add image
    pdf.image("shirtificate/shirtificate.png", x=10, y=70, h=200, w=190)

    # Add text on top
    pdf.set_font("helvetica", size=40)
    pdf.cell(0, 30, f"CS50 Shirtificate", align="C")

    # Add text in the middle
    pdf.set_font("helvetica", size=25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-180, 220, f"{name} took CS50", align="C")

    # Output pdf
    pdf.output("shirtificate/shirtificate.pdf")


if __name__ == "__main__":
    main()
