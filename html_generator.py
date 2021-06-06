import glob
from dominate import document
from dominate.tags import *

html_files = glob.glob('html/*.html')

with document(title='AMAZON CATEGORIES') as doc:
    h1('Amazon Categories')
    for file in html_files:
        div(li(a(file.title(), href='%s' % file)))


with open('index.html', 'w') as f:
    f.write(doc.render())