import csv

def generaPlantillaCSV(nombre,cabecera=['nombre','apellido'],primerRow={'nombre':'Pedro','apellido':'Pascal'},delimiterP=';'):
    with open(nombre, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = cabecera
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter=delimiterP)
        writer.writeheader()
        writer.writerow(primerRow)

def CSVToDict(ruta,delimiterP=';'):
    input_file = csv.DictReader(open(ruta),delimiter=delimiterP)
    lista = []
    for row in input_file:
        lista.append(row)
    return lista

def FirstRowCSV(ruta):
    dictobj = csv.DictReader(open(ruta)).next() 
    return dictobj

if __name__ == "__main__":
    generaPlantillaCSV(".")