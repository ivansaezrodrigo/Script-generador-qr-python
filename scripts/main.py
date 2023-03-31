from Qr import *
from Csv import *
from Carpetas import *

rutaCSV = '../QRLista.csv'
nombreCSV= 'QRLista.csv'
ubicacionQRs = '../QRS'

if(nombreCSV in Carpetas.lista_elementos('..')):
    Carpetas.crear_carpeta(ubicacionQRs)
    rows = CSVToDict(rutaCSV)

    if(len(rows) != 0):
        for row in rows:
            qr = Qr(row['versionQR'],row['box_sizeQR'],row['borderQR'])
            qr.stringToQr(row['cadena'],ubicacionQRs,row['color'],row['colorFondo'])
        print('[✓] QRs exportados con éxito.')
    else:
        print('[!] El CSV está vacío.')

else:
    fieldnames = ['cadena','versionQR','box_sizeQR','borderQR','color','colorFondo']
    primera = {'cadena':'REF00EJEMPLO','versionQR':'1','box_sizeQR':'10','borderQR':'2','color':'black','colorFondo':'white'}
    generaPlantillaCSV(rutaCSV,fieldnames,primera)
    print('[✓] "QRLista.csv" generado, por favor complételo.')
    print('Instrucciones apertura: Abra Excel > Archivo > Abrir > QRLista.csv\n')
    print('Instrucciones guardado: Archivo > Exportar > Cambiar el tipo de archivo > CSV (delimitado por comas) (*.csv)')
    print('Sobreescriba el anterior CSV ')

