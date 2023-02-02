#Calcular el indice de masa corporal (IMC)


def imc(estatura,peso):
    return peso / estatura ** 2

peso = float(input('Escriba su peso(Kg):'))
estatura = float(input('Escriba su Estatura(M)'))

indice = imc(estatura, peso)

print('Su IMC es:',round(indice, 2))
