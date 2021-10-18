headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    news_ticker += headline + ' ' #hice un append y lo hice mal

    if len(news_ticker) >= 140: # no puse len
        news_ticker = news_ticker[:140] #NO ENTIENDO ESTA PARTE (¿está limitandolo a exactamente 140 caracteres? Modificando asi el "news_ticker" de fuera del loop?)
        break




print(news_ticker)

#format and append method are not used in strings


#PRIME NUMBERS: Números que no tienen factores, es decir, que divididos por esos factores el residuo no da = 0.

num = 9 #REPASAR BIEN: LA PSOICION DE LOS FOR IF ELSE....

for i in range(2,num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

num = 9 #REPASAR BIEN: LA PSOICION DE LOS FOR IF ELSE....

is_prime = True

for i in range(2,num):
    if num % i == 0:
        is_prime = False
        break

if is_prime: print("is prime")
else: print("is NOT prime")




for i in range(0,7):
    for j in range(0,7-i):
        print(" ", end="")
    for k in range(0,2*i+1):
        print("0", end="")
    print("")

pyramid_width = 7
for i in range(0,pyramid_width):
    for j in range(0,pyramid_width-i):
        print(" ", end="")
    for k in range(0,2*i+1):
        print("0", end="")
    print("")
