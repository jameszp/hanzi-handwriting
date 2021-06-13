import re


def process_worksheet(hanzi):
    svg = open(hanzi.svg_file_name_original_still(), 'r').read()

    # make lines clear
    svg = re.sub(r'<g stroke="lightgray"', '<g stroke="lightgray" stroke-opacity="0"', svg)

    # change color to black
    svg = re.sub(r'\.stroke1.*fill: #.{6};}', '.stroke {fill: #000000;}', svg, flags=re.DOTALL)

    # replace all numbered strokes with one stroke
    svg = re.sub(r'stroke[0-9]+', 'stroke', svg)

    # change stroke width
    svg = re.sub(r'stroke-width: 4px;', 'stroke-width: 1px;', svg)

    # change font size
    svg = re.sub(r'font-size: 50px;', 'font-size: 100px;', svg)

    output = open(hanzi.svg_file_name_worksheet(), 'w')
    output.write(svg)
    output.close()


def process_flashcard(hanzi):
    svg = open(hanzi.svg_file_name_original_still(), 'r').read()

    # make lines clear
    svg = re.sub(r'<g stroke="lightgray"', '<g stroke="lightgray" stroke-opacity="0"', svg)

    # change color to black
    svg = re.sub(r'\.stroke1.*fill: #.{6};}', '.stroke {fill: #000000;}', svg, flags=re.DOTALL)

    # replace all numbered strokes with one stroke
    svg = re.sub(r'stroke[0-9]+', 'stroke', svg)

    # change stroke width
    svg = re.sub(r'stroke-width: 4px;', 'stroke-width: 3px;', svg)

    # change font size
    svg = re.sub(r'font-size: 50px;', 'font-size: 75px;', svg)

    output = open(hanzi.svg_file_name_flashcard(), 'w')
    output.write(svg)
    output.close()
