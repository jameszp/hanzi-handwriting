import os
from decimal import *


def write_tex(hanzi_list):
    f = open('worksheet/hanzi_worksheet.tex', 'w')
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

            if pos == 3:
                f.write('\t\\end{tikzpicture}\n')

            pos = (pos + 1) % 4
    if not pos == 0:
        f.write('\t\\end{tikzpicture}\n')

    f.write('\\end{document}\n')
    f.close()


def write_character(hanzi, pos):
    s = ''
    vertical_offset = Decimal(pos) * Decimal(2.5) + Decimal(0.5)

    if pos == 0:
        comment = '\t\t% first'
    elif pos == 1:
        comment = '\t\t% second'
    elif pos == 2:
        comment = '\t\t% third'
    elif pos == 3:
        comment = '\t\t% fourth'
    else:
        print("Incorrect position: {}".format(pos))
        return 1, ''

    pinyin = ", ".join(hanzi.pinyin)

    definition = hanzi.definition
    if hanzi.definition is None:
        definition = ''

    if not os.path.exists(hanzi.svg_file_name_worksheet()):
        print("SVG does not exist: {}".format(hanzi.svg_file_name_worksheet()))
        return 1, ''

    # information
    s += comment + '\n'
    s += '\t\t\\node[anchor=north west] at (0.5in, {y}in) {{\\parbox[c][0.45in][b]{{1in}}{{{pinyin}}}}};\n'.format(y=vertical_offset, pinyin=pinyin)
    s += '\t\t\\node[anchor=north west] at (1.5in, {y}in) {{\\parbox[c][0.45in][b]{{6.5in}}{{{definition}}}}};\n'.format(y=vertical_offset, definition=definition)
    s += '\t\t\\node[anchor=north west] at (0.5in,{y}in) {{\\includegraphics[width=1in, height=1in]{{{pdf}}}}};\n'.format(y=vertical_offset + Decimal(0.5), pdf=hanzi.pdf_file_name())

    # horizontal lines
    s += '\t\t% horizontal lines\n'
    s += '\t\t\\draw (0.5in,{y1}in) -- (8in, {y2}in);\n'.format(y1=vertical_offset + Decimal(0.5), y2=vertical_offset + Decimal(0.5))
    s += '\t\t\\draw (1.5in,{y1}in) -- (8in, {y2}in);\n'.format(y1=vertical_offset + Decimal(1), y2=vertical_offset + Decimal(1))

    for i in range(3, 6):
        s += '\t\t\\draw (0.5in,{y1}in) -- (8in, {y2}in);\n'.format(y1=vertical_offset + Decimal(0.5) * Decimal(i), y2=vertical_offset + Decimal(0.5) * Decimal(i))

    # vertical lines
    s += '\t\t% vertical lines\n'
    s += '\t\t\\draw (0.5in,{y1}in) -- (0.5in, {y2}in);\n'.format(y1=vertical_offset + Decimal(0.5), y2=vertical_offset + Decimal(2.5))
    s += '\t\t\\draw (1in,{y1}in) -- (1in, {y2}in);\n'.format(y1=vertical_offset + Decimal(1.5), y2=vertical_offset + Decimal(2.5))

    for i in range(3, 17):
        s += '\t\t\\draw ({x1}in,{y1}in) -- ({x2}in, {y2}in);\n'.format(x1=Decimal(0.5) * Decimal(i), x2=Decimal(0.5) * Decimal(i), y1=vertical_offset + Decimal(0.5),
                                                                        y2=vertical_offset + Decimal(2.5))

    return 0, s
