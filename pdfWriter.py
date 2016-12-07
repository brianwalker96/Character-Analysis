import subprocess 

class pdfWriter:
    def __init__ (self, name, handle, bio, topThree):
        self.name = name
        self.handle = handle
        self.bio = bio
        self.topThree = topThree

    def generatePDF(self) :
        lines = [
        "\\documentclass[12pt]{article}",
        "\\usepackage{graphicx}",
        "\\begin{document}",
        "\\includegraphics[scale=0.5]{prof-pic.jpg}\\\\",
        "\\huge \\noindent " + self.name +"\\\\",
        "\\large " + self.handle + "\\\\",
        "\\small " + self.bio + "\\\\",
        "\\huge \\textbf{Words}\\\\",
        "\\includegraphics[scale=.4, trim=0.5cm 0.5cm 0.5cm 0.5cm,clip]{wordcloud.png}\\\\",
        "\\huge \\textbf{Time}\\\\",
        "\\includegraphics[scale=.4, trim=0.5cm 0.5cm 0.5cm 0.5cm,clip]{byTime.png}\\\\",
        "\\large " + self.topThree[0][0].replace("&", "\\&") + " : \\small " + self.topThree[0][1] + "\\\\",
        "\\large " + self.topThree[1][0].replace("&", "\\&") + " : \\small " + self.topThree[1][1] + "\\\\",
        "\\large " + self.topThree[2][0].replace("&", "\\&") + " : \\small " + self.topThree[2][1] + "\\\\",
        "\\end{document}"
        ]
        with open('PlayerSummary.tex', 'w+') as f:
            for line in lines:
                f.write(line + "\n")

        cmd = ['pdflatex', '-interaction', 'nonstopmode', 'PlayerSummary.tex']
        proc = subprocess.Popen(cmd)
        proc.communicate()
        subprocess.Popen(["PlayerSummary.pdf"],shell=True)



