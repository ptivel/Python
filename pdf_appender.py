import arcpy

# Set the workspace.
arcpy.env.workspace = r"C:\files"

# List all of the pdf files in the output folder.
# pdfList is a Python List returned from the ListFiles function.
pdfList = arcpy.ListFiles("*.pdf")
pdfPath = r"C:\files\Application.pdf"
pdfDoc = arcpy.mapping.PDFDocumentCreate(pdfPath)
# Iterate through the fields and print the name of each
# field to the Interactive Window.
for pdf in pdfList:
    print pdf



pdfDoc.appendPages(r"C:\files\one.pdf")
pdfDoc.appendPages(r"C:\files\two.pdf")
pdfDoc.appendPages(r"C:\files\three.pdf")
pdfDoc.appendPages(r"C:\files\four.pdf")
pdfDoc.appendPages(r"C:\files\five.pdf")

#Commit changes and delete variable reference
pdfDoc.saveAndClose()
del pdfDoc
