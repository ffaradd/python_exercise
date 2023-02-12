from string import ascii_lowercase

#   c'e vo certi tipi di cervello
text = "f'h yr fhuwl wlsl gl fhuyhoor"
for key in range(1, 27):
    rotated = ascii_lowercase[-key:] + ascii_lowercase[:-key]
    table = str.maketrans(ascii_lowercase, rotated)
    print(f"{text.translate(table)} CHIAVE : {key}")
