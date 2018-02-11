import pdfkit
import sass


class PDFCreator:
    def __init__(self):
        self.compile_sass()

    def compile_sass(self):
        compiled_css = sass.compile(filename="sass/resume.scss")
        with open("css/resume.css", "w") as css_file:
            for line in compiled_css:
                css_file.write(line)

            css_file.close()

    def generate_pdf(self):
        pdfkit.from_file("resume.html", "pdfs/resume.pdf")


def main():
    PDFCreator().generate_pdf()

if __name__ == '__main__':
    main()