#main.py
import fileinput # biblioteka datnju ievadisanai

with fileinput.FileInput(files=('admin.txt', 'viesis.txt')) as datne:
 for idx, line in enumerate(datne):
  if datne.isfirstline() == True:
    print('=== Lasa datni === ', datne.filename())
    print(idx, line,end='' )
