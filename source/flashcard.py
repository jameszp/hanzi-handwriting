import os
from decimal import *


def write_tex(hanzi_list):
    f = open('flashcard/hanzi_flashcard.tex', 'w')
    f.write('\\documentclass[letterpaper]{article}\n')
    f.write('\\usepackage{geometry}\n')
    f.write('\\geometry{letterpaper, margin=0in}\n')
    f.write('\\pagenumbering{gobble}\n')
    f.write('\\usepackage{tikz}\n')
    f.write('\\setlength{\\parindent}{0pt}\n')
    f.write('\\setlength{\\fboxsep}{0pt}\n\n')

    f.write('% \\title{Hanzi Flashcards}\n')
    f.write('% \\author{James Peterson}\n')
    f.write('% \\date{June 2021}\n\n')

    f.write('\\begin{document}\n')

    pos = 0
    for hanzi in hanzi_list:
        exit_code, s = write_character(hanzi, pos)
        if not exit_code:
            if pos == 0:
                f.write('\t\\newpage\n')
                f.write('\t\\begin{tikzpicture}[every node/.style={inner sep=0,outer sep=0}, yscale=-1]\n')
                f.write('\t\t\\node(O) at (0,0){};\n')

            f.write(s)

            if pos == 2:
                f.write('\t\\end{tikzpicture}\n')

            pos = (pos + 1) % 3
    if not pos == 0:
        f.write('\t\\end{tikzpicture}\n')

    f.write('\\end{document}\n')
    f.close()


def write_character(hanzi, pos):
    s = ''
    vertical_offset = Decimal(pos) * Decimal(3.5) + Decimal(0.5)

    if pos == 0:
        comment = '\t\t% first'
    elif pos == 1:
        comment = '\t\t% second'
    elif pos == 2:
        comment = '\t\t% third'
    else:
        print("Incorrect position: {}".format(pos))
        return 1, ''

    pinyin = ", ".join(hanzi.pinyin)

    definition = hanzi.definition
    if hanzi.definition is None:
        definition = ''

    if not os.path.exists(hanzi.svg_file_name_flashcard()):
        print("SVG does not exist: {}".format(hanzi.svg_file_name_flashcard()))
        return 1, ''

    s += comment + '\n'

    # svg
    s += '\t\t\\node[anchor=north west] at (0.5in,{y}in) {{\\includegraphics[width=3in, height=3in]{{{pdf}}}}};\n'.format(y=vertical_offset, pdf=hanzi.pdf_file_name())

    # svg box
    s += '\t\t\\draw (0.5in,{y1}in) -- (0.5in, {y2}in);\n'.format(y1=vertical_offset, y2=vertical_offset + Decimal(3))
    s += '\t\t\\draw (0.5in,{y1}in) -- (3.5in, {y2}in);\n'.format(y1=vertical_offset, y2=vertical_offset)
    s += '\t\t\\draw (3.5in,{y1}in) -- (3.5in, {y2}in);\n'.format(y1=vertical_offset, y2=vertical_offset + Decimal(3))
    s += '\t\t\\draw (0.5in,{y1}in) -- (3.5in, {y2}in);\n\n'.format(y1=vertical_offset + Decimal(3), y2=vertical_offset + Decimal(3))

    # pinyin
    s += '\t\t\\node[anchor=north west] at (3.75in,{y1}in) {{\n'.format(y1=vertical_offset)
    s += '\t\t\t\\begin{minipage}[c][0.75in][b]{4.25in}\n'
    s += '\t\t\t\\Huge {pinyin}\n'.format(pinyin=pinyin)
    s += '\t\t\t\\end{minipage}\n'
    s += '\t\t};\n\n'

    # definition
    s += '\t\t\\node[anchor=north west] at (3.75in,{y1}in) {{\n'.format(y1=vertical_offset + Decimal(0.75))
    s += '\t\t\t\\begin{minipage}[c][2.25in][c]{4.25in}\n'
    s += '\t\t\t\\Huge {definition}\n'.format(definition=definition)
    s += '\t\t\t\\end{minipage}\n'
    s += '\t\t};\n\n'

    return 0, s
