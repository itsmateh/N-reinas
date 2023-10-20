# Maximo del tablero
maxTab = 8
tab = [-1] * maxTab

# Contador de combinaciones
contador = 1

# Grafico del tablero en consola
def tablero():
    global contador
    print("")
    print("Combinacion: ", contador )
    contador +=1
    print("================================================================================================")
    fila = 0
    while fila < 8:
        col = 0
        while col < 8:
            if tab[col] == fila:
                print(" R ", end=" ")
            else:
                print(" . ", end=" ")
            col += 1
        print()
        fila += 1


# Algoritmo de manera recursiva N reinas
def colocarReina(reina, max):
    tab[reina] = 0
    while tab[reina] < max:
        ok = True
        ind = 0
        while ind < reina and ok:
            if tab[ind] == tab[reina] or abs(ind - reina) == abs(tab[ind] - tab[reina]):
                ok = False
            ind += 1
        if ok:
            if reina == max-1:
                tablero()
            else:
                colocarReina(reina + 1,max)
        tab[reina] += 1

# Prog. Principal 
colocarReina(0,8)
