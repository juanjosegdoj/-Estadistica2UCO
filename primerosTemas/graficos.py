import pandas as pd
import matplotlib.pyplot as plt

class Graficos:
    
    def __init__(self, archivo, colData, colAgrup):
        self.df = pd.read_csv(archivo)
        self.colData = colData
        self.colAgrup = colAgrup
        
    def drawCajasBigotes(self):
        geterGruop = []
        
        g = self.df.groupby(self.colAgrup)
        for datoUnico in self.df[self.colAgrup].unique():
            geterGruop.append(g.get_group(datoUnico)[self.colData].values)

        plt.boxplot(geterGruop)
        plt.show()

x = Graficos("pruebas de hipotesis.csv", 'muestra', 'bascula')
x.drawCajasBigotes()
