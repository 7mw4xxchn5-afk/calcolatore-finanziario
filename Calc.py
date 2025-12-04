#Introduzione
z=input("Ciao! Cosa vuoi fare?\n\nA)Calcolare il prezzo di un'obbligazione\nB)Calcolare la Duration di un portafoglio finanziario\nC)Calcolare la rata di un mutuo\n\n")


# Prezzo Obbligazione

def prezzo_con_cedole():
    t = int(input("Tra quanti anni scade l'obbligazione? "))
    it = float(input("Inserire il TRES in %: "))
    ic = float(input("Inserire il tasso cedolare annuo in %: "))
    vn = float(input("Inserire il valore nominale: "))
    tipo = int(input("Numero di cedole all'anno: "))

    prezzo = 0.0
    cedola = ((ic / 100) * vn) / tipo

    for i in range(0, t):          
        for y in range(1, tipo + 1):  
            periodo = i + y / tipo
            prezzo += cedola / ((1 + it/100) ** periodo)

    prezzo += vn / ((1 + it/100) ** t)

    return prezzo


def prezzo_senza_cedole():
    t = int(input("Tra quanti anni scade l'obbligazione? "))
    vn = float(input("Inserire il valore nominale: "))
    i = float(input("Inserire il rendimento in %: "))

    prezzo = vn / ((1 + i/100) ** t)

    return prezzo


if z in ["A", "a"]:
    x = input("L'obbligazione paga cedole intermedie? (si/no): ").lower()

    if x in ["si", "sì", "sí", "s"]:
        prezzo = prezzo_con_cedole()   
        print("\nPrezzo obbligazione:", round(prezzo, 2))

    elif x in ["no", "n"]:
        prezzo = prezzo_senza_cedole() 
        print("\nPrezzo obbligazione:", round(prezzo, 2))

    else:
        print("Risposta non valida.")



#Duration di un portafoglio finanziario


def duration():
    y = input("L'obbligazione paga cedole intermedie? (si/no): ").lower()
    
    if y in ["si", "sì", "sí", "s"]:
        t = int(input("Tra quanti anni scade l'obbligazione? "))
        it = float(input("Inserire il TRES in %: "))
        ic = float(input("Inserire il tasso cedolare annuo in %: "))
        vn = float(input("Inserire il valore nominale: "))
        tipo = int(input("Numero di cedole all'anno: "))

        
        prezzo = 0.0
        cedola = ((ic / 100) * vn) / tipo

        for i in range(0, t):
            for s in range(1, tipo + 1):
                periodo = i + s / tipo
                prezzo += cedola / ((1 + it/100) ** periodo)

        prezzo += vn / ((1 + it/100) ** t)

        num_dur = 0.0
        for i in range(t):
            for s in range(1, tipo + 1):
                periodo = i + s / tipo
                cf_scontato = cedola / ((1 + it/100) ** periodo)
                num_dur += periodo * cf_scontato

        cf_rimborso = vn / ((1 + it/100) ** t)
        num_dur += t * cf_rimborso

        dur = num_dur / prezzo
    
        return prezzo, dur
    
    elif y in ['no', 'n']:
        t = int(input("Tra quanti anni scade l'obbligazione? "))
        vn = float(input("Inserire il valore nominale: "))
        i = float(input("Inserire il rendimento in %: "))

        prezzo = vn / ((1 + i/100) ** t)
        dur = t  

        return prezzo, dur

    else:
        print("Risposta non valida.")
        return None, None

        

if z in ['B', 'b']:
    x = int(input('Di quanti titoli è composto il tuo portafoglio? '))

    if x == 1:
        prezzo, dur = duration()

    elif x > 1:
        i = 0
        prezzi = []
        durations = []
        while i < x:
            prezzo, dur = duration()
            
            prezzi.append(prezzo)
            durations.append(dur)

            i = i + 1

        duration_tot = 0.0

        for v in range(x):
            duration_tot = duration_tot + (prezzi[v] / sum(prezzi)) * durations[v]

        print('\nLa Duration del tuo portafoglio è di', duration_tot, 'anni')


#Rata di un mutuo







