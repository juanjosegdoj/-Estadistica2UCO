from scipy.stats import f, t, norm
from math import fabs

def razonVarianza(desEst1, desEst2, n1, n2, confianza):
    print('-- razonVarianza --')
    UnoMenosAlfaDiv2 = 1 - confianza/2
    resultadoF_LI = f.ppf(UnoMenosAlfaDiv2, n2-1, n1-1)
    LI = (desEst1**2/desEst2**2)*resultadoF_LI
    
    AlfaDiv2 = confianza/2
    resultadoF_LS = f.ppf(AlfaDiv2, n2-1, n1-1)
    LS = (desEst1**2/desEst2**2)*resultadoF_LS
    
    print('LI: ', LI)
    print('LS: ', LS)

def diferenciaMediaPoblacional(n1, n2, s1, s2, media1, media2, confianza):
    
    print('-- diferenciaMediaPoblacional --')
    SP = (((n1-1)*s1**2 +(n2-1)*s2**2)/(n1+n2-2))**0.5
    LI = media1 - media2 - t.ppf(confianza/2, n1+n2-2)*SP*(1/n1 + 1/n2)**0.5
    LS = media1 - media2 + t.ppf(confianza/2, n1+n2-2)*SP*(1/n1 + 1/n2)**0.5

    print('LI: ', LI)
    print('LS: ', LS)
    
def diferenciaProporciones(p1, p2, n1, n2, alfa):
    LI = (p1 - p2) - norm.ppf(alfa/2) * ( p1*(1-p1)/n1 + p2*(1-p2)/n2 )**0.5
    LS = (p1 - p2) + norm.ppf(alfa/2) * ( p1*(1-p1)/n1 + p2*(1-p2)/n2 )**0.5
    
    print('LI: ', round(LI, 3))
    print('LS: ', round(LS, 3))

razonVarianza(
    desEst1 = 17.47,
    desEst2= 17.31,
    n1 = 7,
    n2 = 7,
    confianza = 0.95)

"""
diferenciaProporciones(p1 = 0.4, p2 = 0.1, n1= 10, n2=10, confianza = 0.05)
    
diferenciaMediaPoblacional(8, 8, 4, 4, 3, 4, 0.95)

"""
