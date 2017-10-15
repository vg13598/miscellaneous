"""
FInds all the pictures in a folder and turns them to a pdf. I know I have a version where the size is kept. Use of latex
"""

import glob, os

for filename in os.listdir("."):
    new_filename=filename.replace(' ','_')
    os.rename(filename, new_filename)
image_files=[]
for file in glob.glob("*.jpg"):
    print(file)
    image_files.append(file)
for file in glob.glob("*.bmp"):
    print(file)
    image_files.append(file)
for file in glob.glob("*.jpeg"):
    print(file)
    image_files.append(file)
for file in glob.glob("*.png"):
    print(file)
    image_files.append(file)
             

print(image_files)

print(sorted(image_files))

print('------------------------------------------------')
print('---------------Converting images----------------')
print('------------------------------------------------')

text_file = open("Output.tex", "w")

text_file.write(r"""\documentclass[a4paper,12pt]{article}
\usepackage{incgraph,tikz}

\begin{document}
""")

for name in image_files:

    text_file.write(r"""\incgraph[documentpaper]
      [width=\paperwidth,height=\paperheight]{"""+name+"""}
    """)
    text_file.write(r"""


    """)



text_file.write(r"""\end{document}""")

text_file.close()

os.system("pdflatex Output.tex")

os.remove('Output.tex')
os.remove('Output.aux')
os.remove('Output.log')

os.system('start "" /max "Output.pdf"')


