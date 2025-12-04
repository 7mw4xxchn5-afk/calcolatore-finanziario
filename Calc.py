#Introduction
z = input("Hello! What would you like to do?\n\nA)Calculate the price of a bond\nB)Calculate the Duration of a financial portfolio\nC)Calculate the monthly mortgage payment\n\n")


# Bond Price

def prezzo_con_cedole():
    t = int(input("In how many years does the bond mature? "))
    it = float(input("Enter the Yield to Maturity (YTM) in %: "))
    ic = float(input("Enter the annual coupon rate in %: "))
    vn = float(input("Enter the face value: "))
    tipo = int(input("Enter the number of coupon payments per year: "))

    prezzo = 0.0
    cedola = ((ic / 100) * vn) / tipo

    for i in range(0, t):          
        for y in range(1, tipo + 1):  
            periodo = i + y / tipo
            prezzo += cedola / ((1 + it/100) ** periodo)

    prezzo += vn / ((1 + it/100) ** t)

    return prezzo


def prezzo_senza_cedole():
    t = int(input("In how many years does the bond mature? "))
    vn = float(input("Enter the face value: "))
    i = float(input("Enter the yield in %: "))

    prezzo = vn / ((1 + i/100) ** t)

    return prezzo


if z in ["A", "a"]:
    x = input("Does the bond pay coupons? (yes/no): ").lower()

    if x in ["yes", "y"]:
        prezzo = prezzo_con_cedole()   
        print("\nBond price:", round(prezzo, 2))

    elif x in ["no", "n"]:
        prezzo = prezzo_senza_cedole() 
        print("\nBond price:", round(prezzo, 2))

    else:
        print("Invalid answer.")



# Duration of a financial portfolio

def duration():
    y = input("Does the bond pay coupons? (yes/no): ").lower()
    
    if y in ["yes", "y"]:
        t = int(input("In how many years does the bond mature? "))
        it = float(input("Enter the Yield to Maturity (YTM) in %: "))
        ic = float(input("Enter the annual coupon rate in %: "))
        vn = float(input("Enter the face value: "))
        tipo = int(input("Number of coupon payments per year: "))

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
        t = int(input("In how many years does the bond mature? "))
        vn = float(input("Enter the face value: "))
        i = float(input("Enter the yield in %: "))

        prezzo = vn / ((1 + i/100) ** t)
        dur = t  

        return prezzo, dur

    else:
        print("Invalid answer.")
        return None, None

        

if z in ['B', 'b']:
    x = int(input('How many securities does your portfolio contain? '))

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

        print('\nThe Duration of your portfolio is', duration_tot, 'years')



# Mortgage payment

if z in ['C','c']:
    C = float(input('Enter the loan amount: '))
    i = float(input('Enter the periodic interest rate (monthly) in %: '))
    n = int(input('Enter the total number of months: '))

    i = i / 100   

    rata = C * (i * (1 + i)**n) / ((1 + i)**n - 1)

    print('Your monthly payment is', str(round(rata, 2)) + '€')

    x = input('Do you want to calculate the total interest paid? ').lower()

    if x in ["yes", "y"]:
        quota = rata * n - C
        print('Total interest paid:', str(round(quota, 2)) + '€')
    else:
        pass
