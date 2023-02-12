# Assumendo che Python non abbia i set built-in nel linguaggio, creare una classe che permetta di replicarne le principali funzionalità e ne mantenga le caratteristiche salienti.
# - deve garantire che ogni elemento del mio set sia unico
# - devo poter aggiungere elementi ad un mio set con un metodo add
# - devo poterli rimuovere con un metodo remove
# - devo poter verificare se un elemento è presente nel mio set con un metodo contains (Bonus: far funzionare la keyword in con la propria classe) MAGIC METHODS
# - devo rendere il mio set iterabile (devo poterlo utilizzare in un ciclo for --> for el in mio_set )
# - devo poter creare il mio set partendo da una lista, stringa o altri oggetti iterabili

class s3t:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"[{self.value}]"

    def maremma(self):
        print("le stelle sono tante milioni di milione la stella di " + self.value + " vuol dire qualità")
        print(f"le stelle sono tante milioni di milione la stella di {self.value} vuol dire qualità")

    def __add__(self, value):
        self.value = value


p = []
p.append(s3t("ciao"))

#p.__add__("antonio")

print(p)
