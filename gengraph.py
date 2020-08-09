
import argparse
import math

def replace_with_dict(s, d):
    for e in d:
        s = s.replace(e, str(d[e]))
    return s

def unit(x, y):
    n = math.sqrt(x*x + y*y)
    return x/n, y/n

def svg_head():
    return """
<svg width="SVG_WIDTH" height="SVG_HEIGHT" xmlns="http://www.w3.org/2000/svg" viewBox="VIEW_BOX_X VIEW_BOX_Y VIEW_BOX_WIDTH VIEW_BOX_HEIGHT"
    xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
        <path id="file" d="M  1,  1 l  0,  10 l  8,  0 l  0, -8 l -2, -2 l -6,  0 M  7,  1 l  0,  2 l  2,  0 " />
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
          <path d="M0,0 L0,6 L9,3 z" fill="#eef" />
        </marker>
    </defs>
"""

def svg_background(minx, miny, maxx, maxy):
    s = """
<rect x="X" y="Y" width="WIDTH" height="HEIGHT" style="stroke-width:0;stroke:rgb(0,0,0)" />
    """

    return replace_with_dict(s, {
        "X" : minx,
        "Y" : miny,
        "WIDTH" : maxx - minx,
        "HEIGHT" : maxy - miny
    })

def svg_file(file):
    s = """
    <use xlink:href="#file"
        stroke="#dde" stroke-linecap="round" stroke-width="0.2" fill="#111"
        transform="translate(FILE_X FILE_Y)" />

    <text x="TEXT_X" y="TEXT_Y" font-family="sans-serif" font-size="2px" text-anchor="middle" fill="#eef">NAME</text>
    """

    ext_elem = """
        <text x="EXT_X" y="EXT_Y" font-family="sans-serif" font-size="2.5px" font-weight="bold"
        text-anchor="middle" fill="#333">EXT_TEXT</text>
    """

    block = replace_with_dict(s, {
        "FILE_X" : file.x,
        "FILE_Y" : file.y,
        "NAME" : file.name,
        "TEXT_X" : file.x + 5,
        "TEXT_Y" : file.y + 13.1
        })

    ext = file.name.split(".")[-1]
    if len(ext) in [2,3]:
        block += replace_with_dict(ext_elem,
            {
                "EXT_X" : file.x + 5,
                "EXT_Y" : file.y + 7,
                "EXT_TEXT" : ext.upper(),
            })

    return block

def svg_arrow(back, front):
    s = """<line x1="X1" y1="Y1" x2="X2" y2="Y2" stroke="#eef" stroke-width="0.4" marker-end="url(#arrow)" />"""

    ux, uy = unit(front.x - back.x, front.y - back.y)

    x1 = back.x + 5     + ux * 4
    y1 = back.y + 14    + uy * 1
    x2 = front.x + 5    - ux * 4
    y2 = front.y + 0    - uy * 1

    return replace_with_dict(s, {"X1" : x1, "Y1" : y1,  "X2" : x2, "Y2" : y2})

def svg_tail():
    return """
</svg>
"""


class File:
    def __init__(self, p):
        self.name = p[0]
        self.x = float(p[1])
        self.y = float(p[2])

    def __repr__(self):
        return "[" + self.name + ": " + str(self.x) + ", " + str(self.y) + "]"


class Arrow:
    def __init__(self, p):
        self.back = p[0]
        self.front = p[1]

    def __repr__(self):
        return "[" + self.back + " -> " + self.front + "]"



def get_files_and_arrows_from_commandline(args):

    f = open(args.files, "r")
    lines = f.read()
    f.close()

    import re

    files = map(File, re.findall(r"(\S+): ([-\d\.]+), ([-\d\.]+)", lines))
    arrows = map(Arrow, re.findall(r"(\S+) -> (\S+)", lines))
    return files, arrows



parser = argparse.ArgumentParser()
parser.add_argument('--files', '-r', required=True)
parser.add_argument('--output', '-o', required=True)
args = parser.parse_args()

files, arrows = get_files_and_arrows_from_commandline(args)


svg_elements = []

svg_elements.append(svg_head())

file_map = {}
minx=0
maxx=0
miny=0
maxy=0

for f in files:
    minx = min(minx, f.x)
    maxx = max(maxx, f.x)
    miny = min(miny, f.y)
    maxy = max(maxy, f.y)
    file_map[f.name] = f

minx = minx - 5
miny = miny - 5
maxx = maxx + 15
maxy = maxy + 20

svg_elements.append(svg_background(minx, miny, maxx, maxy))

for f in files:
    svg_elements.append(svg_file(f))

for a in arrows:
    back_file = file_map[a.back]
    front_file = file_map[a.front]

    svg_elements.append(svg_arrow(back_file, front_file))


svg_elements.append(svg_tail())

scaleup = 6

final = replace_with_dict("\n".join(svg_elements),
    {
        "VIEW_BOX_X" : minx,
        "VIEW_BOX_Y" : miny - 5,
        "VIEW_BOX_WIDTH" : maxx-minx,
        "VIEW_BOX_HEIGHT" : maxy-miny + 20,
        "SVG_WIDTH" : scaleup * (maxx-minx),
        "SVG_HEIGHT" : scaleup * (maxy-miny + 20),
    })

out = open(args.output, "w")
out.write(final)
out.close()




