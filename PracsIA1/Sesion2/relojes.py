class Relojes(Problem):
    "Problema de los relojes"

    def __init__(self):
        self.initial = (0,0) #en el estado inicial una de las partes de cada reloj esta llena

    def actions(self,estado):
        reloj_7=estado[0]
        reloj_11=estado[1]
        #accs es una lista que inicializamos vacía, comprobaremos las precondiciones y añadiremos en esta lista las acciones aplicables al estado.
        accs=list() 
        if reloj_7 == 0:
            accs.append("girar reloj de 7")
        if reloj_11 ==0 :
            accs.append("girar reloj de 11")
        if reloj_7==0 and reloj_11==0:
            accs.append("girar ambos relojes")
        return accs
        # se devuelve en accs todas las acciones aplicables

    def result(self,estado,accion):
    # aplica una acción a un estado (esta función se llamará desde el algoritmo de búsqueda)
        r7=estado[0]
        r11=estado[1]
        if accion=="girar reloj de 7":
            return (r7-r11,0) if r11<7 else (0,r11-7)
        elif accion=="girar reloj de 11":
            return (0,r11-r7) 
        elif accion=="girar ambos relojes":
            return (0,4)

    def goal_test(self,estado):
        return estado[0]==3 or estado[0]==4 or estado[1]==3 or estado[1]==8