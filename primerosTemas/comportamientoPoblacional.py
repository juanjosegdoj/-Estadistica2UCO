import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2, t, norm

# grupo = df.groupby(columnaAgrupacion)

# Comportamiento poblacional
class comportamientoPoblacional:
    numDecimales = 2
    
    def __init__(self, archivoCSV, columnaDatos, columnaAgrupacion, confianza):
        
        self.df = pd.read_csv(archivoCSV)
        self.columnaDatos = columnaDatos
        self.columnaAgrupacion = columnaAgrupacion
        self.confianza = confianza
        

    def varianzaPoblacional(self):
        print('Varianza poblacional')
        # Cargando datos y especificaciones
        alfa = 1 - self.confianza


        # Agrupando información
        gruposDeDatos = []
        for datoUnico in self.df[self.columnaAgrupacion].unique():
            grupo = self.df[self.columnaDatos][self.df[self.columnaAgrupacion]== datoUnico]
            gruposDeDatos.append((datoUnico, grupo))


        # Aplicando formula de mediaPoblacional
        for grupo in gruposDeDatos:
            
            cantidad = grupo[1].count()
            varianza = grupo[1].std()**2

            chiCuadradaLI = chi2.ppf(alfa/2, cantidad -1)
            chiCuadradaLS = chi2.ppf(1 - alfa/2, cantidad -1)
            
            LI = (cantidad-1)*varianza/chiCuadradaLI
            LS = (cantidad-1)*varianza/chiCuadradaLS

            print(self.columnaAgrupacion,': ',grupo[0])
            print(self.columnaAgrupacion,': ',grupo[0])
            print('LI: ',round(LI, self.numDecimales))
            print('LS: ',round(LS, self.numDecimales))
        

    def mediaPoblacional(self):
        print('Media poblacional')

        # Agrupando información
        gruposDeDatos = []
        for datoUnico in self.df[self.columnaAgrupacion].unique():
            grupo = self.df[self.columnaDatos][self.df[self.columnaAgrupacion]== datoUnico]
            gruposDeDatos.append((datoUnico, grupo))

        
        # Aplicando formula de mediaPoblacional
        for grupo in gruposDeDatos:
            media = grupo[1].mean()
            cantidad = grupo[1].count()
            desvEstandar = grupo[1].std()
            tdeStudent = t.ppf((1 - self.confianza)/2, cantidad -1)
            LI = media - (tdeStudent * (desvEstandar/cantidad**0.5))
            LS = media + (tdeStudent * (desvEstandar/cantidad**0.5))

            # Redondeando 
            LI = round(LI, self.numDecimales)
            LS = round(LS, self.numDecimales)
            
            print('LI: ', LI)
            print('LS: ', LS)

        print("""El {}% de las {} {} tendrán
              una media poblacional comprendida entre {} y {}""".format(self.confianza*100, gruposDeDatos[0][0], gruposDeDatos[1][0], LI, LS))

def proporcionPoblacional(p, confianza, n):
    print('Proporción poblacional')
    LI = p - norm.ppf(confianza/2)*(p*(1-p)/n)**0.5
    LS = p + norm.ppf(confianza/2)*(p*(1-p)/n)**0.5
    
    LI = round(LI, 5)
    LS = round(LS, 5)
    
    print('LI: ', LI)
    print('LS: ', LS)

    
proporcionPoblacional(15/500, 0.90, 500)


#objPobla = comportamientoPoblacional("centralesTelefonicas.csv", columnaDatos='Tiempo' ,columnaAgrupacion='Central',confianza=0.95)
#objPobla.mediaPoblacional()


