import subprocess
import datetime
import unicodedata

class PDFWriter:
    def __init__ (self, name, handle, bio, topThree, flaggedTweets):
        print "PDFWriter - intializing"
        self.name = name
        self.handle = handle
        self.bio = bio
        self.topThree = topThree
        self.flagged = flaggedTweets
        print "name: " + str(self.name)
        print "handle: " + str(self.handle)
        print "bio: " + str(self.bio)
        print "topThree: " + str(self.topThree)
        print "flagged: " + str(self.flagged)

    def latexUnicode(self, text):
        return self.latexFormat(unicodedata.normalize('NFKD', text).encode('ascii','ignore'))

    def latexFormat(self, text):
        return text.replace('&', '\\&').replace('#', '\\#')

    def generatePDF(self) :
        print "PDFWriter - generating PDF"
        lines = [ '\\documentclass[12pt]{article}', 
        '\\usepackage{graphicx}', 
        '\\usepackage{subfig}', 
        '\\usepackage[margin=0.5in,footskip=0.25in]{geometry}', 
        '\\begin{document}',
        '\\vskip 0.6in', 
        '\\begin{center}', 
        '\\huge \\textbf{TWITTER REPORT}\\\\',
        '\\small ' + str(datetime.date.today()) + '\\\\', 
        '\\end{center}', 
        '\\vskip 1.5in', 
        '\\begin{minipage}{0.5\\textwidth}', 
        '\\begin{center}', 
        '\\includegraphics[width=0.8\linewidth]{prof_pic.jpg}', 
        '\\end{center}', 
        '\\end{minipage}', 
        '\\hfill', 
        '\\begin{minipage}{0.5\\textwidth}\huge \\noindent ' +  self.latexFormat(self.name) + '\\\\',
        '\\large ' + self.latexFormat(self.handle) + '\\\\',
        '\\large ' + self.latexFormat(self.bio) + '\\\\',
        '\\end{minipage}',
        '\\vskip 4.0in',
        '\\noindent \\textbf{Disclaimer:}\\\\',
        "\\small The information provided in this report often is overly generalized and may not fully capture the Twitter user's character. It should be taken with a grain of salt. It is advised to use the information provided within this report as a quick means of getting an objective summary of the user's Twitter profile.",
        '\\newpage',
        '\\begin{center}',
        '\\textbf{Word Distribution}\\\\',
        '\\bigbreak',
        '\\smallbreak',
        '\\includegraphics[width=0.6 \\textwidth]{word_cloud.png}\\\\',
        '\\bigbreak',
        '\\includegraphics[width=0.8 \\textwidth]{tweets_by_time.png}',
        '\\newpage',
        '\\includegraphics[width=0.8\\textwidth]{topic_bar.png}\\\\',
        '\\end{center}',
        '\\textbf{Sample Tweets}\\\\',
        '\\bigbreak',
        '\\noindent \\large \\textit{' + self.latexFormat(self.topThree[0][0]) + '}\\\\',
        self.latexUnicode(self.topThree[0][1]) +'\\\\',
        '\\smallbreak',
        '\\noindent \\large \\textit{' + self.latexFormat(self.topThree[1][0]) + '}\\\\',
        self.latexUnicode(self.topThree[1][1]) +'\\\\',
        '\\smallbreak',
        '\\noindent \\large \\textit{' + self.latexFormat(self.topThree[2][0]) + '}\\\\',
        self.latexUnicode(self.topThree[2][1]) +'\\\\',
        '\\smallbreak',
        '\\noindent \\textbf{Questionable Tweets:}\\\\',
        self.latexUnicode(self.flagged[0]) + '\\\\',
        '\\newpage',
        '\\begin{center}',
        '\\includegraphics[width=1.0\\textwidth]{sentiment_over_time.png}',
        '\\bigbreak',
        '\\includegraphics[width=0.8 \\textwidth]{sentiment_pie_chart.png}\\\\',
        '\\end{center}',
        '\\end{document}']

        with open('PlayerSummary.tex', 'w+') as f:
             for line in lines:
                 f.write(line + "\n")

        cmd = ['pdflatex', '-interaction', 'nonstopmode', 'PlayerSummary.tex']
        proc = subprocess.Popen(cmd, shell=True)
        proc.communicate()
        subprocess.Popen(["PlayerSummary.pdf"],shell=True)

