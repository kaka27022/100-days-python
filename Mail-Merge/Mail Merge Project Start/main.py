#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Tinha como usar "./Input/Names/invited_names.txt"
with open("/home/kaka/Curso python/Dia 24/Mail-Merge/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    # readlines -> Retorna o arquivo como uma lista
    all_the_names_n = names.readlines()

# rstrip -> tira um certo caracter de uma palavra
all_the_names = [palavra.rstrip('\n') for palavra in all_the_names_n]

with open("/home/kaka/Curso python/Dia 24/Mail-Merge/Mail Merge Project Start/Input/Letters/starting_letter.txt") as arquivo_carta:
    carta = arquivo_carta.read()

for name in all_the_names:
    with open(f"/home/kaka/Curso python/Dia 24/Mail-Merge/Mail Merge Project Start/Output/ReadyToSend/final_letters{name}.txt", "w") as arquivo:
        # replace -> Substitui certa string por outra
        carta_atualizada = carta.replace("[name]", name)
        arquivo.write(carta_atualizada)


