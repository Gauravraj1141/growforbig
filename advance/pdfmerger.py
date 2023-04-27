import os, PyPDF2

pdffiles = []

for filename in os.listdir('.'):
    if filename.endswith(".pdf"):
        if filename != 'merged.pdf':
            pdffiles.append(filename)

pdffiles.sort(key=str.lower)

pdfMerge = PyPDF2.PdfMerger()

for filename in pdffiles:
    with open(filename,'rb') as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        pdfMerge.append(pdfReader)

pdfMerge.write('newmerged.pdf')

