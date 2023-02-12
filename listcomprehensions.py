from string import ascii_lowercase
    #creare una lista con il quadrato di tutti i numeri da 1 a 100
quadrato = [pow(base, 2) for base in range(1, 101)]
print(quadrato)
    #creare una lista con tutti i numeri da 1 a 1000 che sono divisibili per 7
divisibile = [num for num in range(1, 1001) if num % 7 == 0]
print(divisibile)
    #creare un dizionario del tipo { 1: "dispari", 2: "pari", 3: "dispari" .... } per i numeri da 1 a 100
padi = {(key):("pari" if key % 2 == 0 else "dispari") for key in range(1, 101)}
print(padi)
    #contare il numero di spazi presenti in una stringa
stringa = input("inserire stringa con spazi")
spazi = [el for el in stringa if el == " "]
print(f"Spazi totali : {len(spazi)}")
    #un set di tutti i numeri presenti in una stringa --> es: da ‘In 1984 there were 13 instances of a protest with over 1000 people attending’ ottengo {1984, 13, 1000 }
stringa= input("Inserire una stringa che contiene numeri")
numeri = {num for num in stringa.split() if num.isdigit()}
print(numeri)

#Da una lista di frasi ottenere un dizionario di frasi cifrate col Cifrario di Cesare.
#La chiave da utilizzare per la cifratura corrisponde all'indice della frase originale all'interno della lista, ed è anche la chiave a cui associare il testo cifrato.
#In altri termini:
# [ "a", "b", "c" ] ----> {0: "a", 1: "c", 2: "e" }
stringa = input("Inserire la stringa da cifrare")
cifrato = {stringa.split().index(c):c.translate(str.maketrans(ascii_lowercase, ascii_lowercase[stringa.split().index(c):] + ascii_lowercase[:stringa.split().index(c)])) for c in stringa.split()}
print(cifrato)
#stringa.split().translate(str.maketrans(ascii_lowercase, ascii_lowercase[key:] + ascii_lowercase[:key]))

#cifrato = {}
#conta = 0
#output = ""
#for c in stringa.split():
#    output = ""
#    if c.isalpha():
#        ascii_code = ord(c) - ord('a')
#        new_code = (ascii_code + int(conta)) % 26
#        new_char = chr(new_code + ord('a'))
#       output += new_char
#    else:
#        output += c
#    cifrato.update({conta:output})
#    conta += 1
