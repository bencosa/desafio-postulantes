import csv
import json
from operator import delitem
import requests

req = requests.get('https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.csv?_=1650680016201%27')
url_content = req.content
csvfile = open('instituciones.csv', 'wb')
csvfile.write(url_content)
csvfile.close()

with open('instituciones.csv', encoding="utf8") as File:
    reader =csv.reader(File, delimiter=';')
    data =[]
    for col in reader:
        data.append(
            {
                'id':col[0],
                'razon social':col[1],
                'pais':col[2],
                'dr inscripcion':col[3],
                'resolucion inscripcion':col[4],
                'fecha inscripcion':col[5],
                'vigencia hasta':col[6],
                'dr actualización':col[7],
                'resolución actualización':col[8],
                'fecha actualización':col[9],
                'estado':col[10]
            }
        )

jsonfile = open('instituciones.json', 'w', encoding="utf8")
with open('report.txt','w', encoding="utf8") as f:
    for l in data:
        op=str(l)
        f.write(op)
        f.write('\n')

report = open('report.txt', 'r',encoding="utf8")
com=[]
for res in report:
    final = eval(res)
    com.append(final)
com.pop(0)
json.dump(com, jsonfile, indent=4, ensure_ascii=False)
jsonfile.write('\n')
