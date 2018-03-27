# -*- coding: utf-8-sig -*-
import sys
import os
import PyPDF2
import pandas as pd

param=sys.argv[1]
print 'Argument: %s' % param

base_dir='/home/inzpiral/Documents/PDF2XLSX/docs'
input_dir='{}/{}/{}'.format(base_dir, param, 'fixed')
output_dir='{}/{}/{}'.format(base_dir, param, 'output')
cols=[u'Nombre',u'Rut',u'Email',u'Tel. Fijo', u'Tel. Móvil']

# Create output directory if not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df = pd.DataFrame(columns=cols)
for f in os.listdir(input_dir):
     if f.endswith(".pdf"):
         print 'File: %s' % f
         page = 0
         fileReader = PyPDF2.PdfFileReader('{}/{}'.format(input_dir, f))
         pageObj = fileReader.getPage(page)
         pdf_text = pageObj.extractText().split('\n')
         basic_data = {
             u'Nombre': pdf_text[2].encode('utf-8').strip().capitalize(),
             u'Rut':  pdf_text[5].encode('utf-8').strip(),
             u'Email':  pdf_text[34].encode('utf-8').strip(),
             u'Tel. Fijo':  pdf_text[26].encode('utf-8').strip(),
             u'Tel. Móvil':  pdf_text[30].encode('utf-8').strip()
         }
         while (not u'Formación' in pdf_text or page > 100):
             page += 1
             fileReader = PyPDF2.PdfFileReader('{}/{}'.format(input_dir, f))
             pageObj = fileReader.getPage(page)
             pdf_text = pageObj.extractText().split('\n')

         formacion_index = pdf_text.index(u'Formación') + 1
         print 'Formación %s' % pdf_text[formacion_index].encode('utf-8').strip()         
         basic_data.update({ u'Formacion': pdf_text[formacion_index].encode('utf-8').strip()})
         df = df.append(basic_data, ignore_index=True) 

writer = pd.ExcelWriter('{}/{}.{}'.format(output_dir, param,'xlsx'))
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
exit()
