import subprocess 

class pdfWriter:
    def __init__ (self, name, handle, bio):
        self.name = name
        self.handle = handle
        self.bio = bio

    def generatePDF(self) :
        lines = [
        "\\documentclass[12pt]{article}",
        "\\usepackage{graphicx}",
        "\\begin{document}",
        "\\huge \\noindent " + self.name +"\\\\",
        "\\large " + self.handle + "\\\\",
        "\\small " + self.bio + "\\\\",
        "\\huge \\textbf{Words}\\\\",
        "\\includegraphics[scale=.4, trim={0, 0, 0, 0}]{wordcloud.png}\\\\",
        "\\huge \\textbf{Time}\\\\",
        "\\includegraphics[scale=.4, trim={0, 0, 0, 0}]{byTime.png}",
        "\\end{document}"
        ]
        with open('PlayerSummary.tex', 'w+') as f:
            for line in lines:
                f.write(line + "\n")

        cmd = ['pdflatex', '-interaction', 'nonstopmode', 'PlayerSummary.tex']
        proc = subprocess.Popen(cmd)
        proc.communicate()
        subprocess.Popen(["PlayerSummary.pdf"],shell=True)



