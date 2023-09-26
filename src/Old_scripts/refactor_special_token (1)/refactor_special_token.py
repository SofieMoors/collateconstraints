"""maak een lijst met alle woorden die een speciaal teken hebben
1 maak een map 'correct_unicodes'
2 vul het lijstje met replacements verder aan met de juiste codes
3 verander onderaan de directories zodat ze naar het juiste verwijzen
"""
import os, codecs


def make_list(directory, output_path_list, output_path_file):
    replacements = {'a': u'\u0101',
                    'e': u'\u0113',
                    'n': 'nn',
                    'o': u'\u014D',
                    'u': 'û',
                    'i': 'î',
                    'm': '^m',
                    'O': u'\u014C',
                    't': '^t'}  # <-- voeg hier de streepjes toe op de 2 letter (ik heb voorlopig hoedjes gezet)
                                # altijd 1 \ en dan een kleine u en geen plus en zet een u voor het '
    words_with_special_token = [] # start een lege lijst om de woorden met speciale tekens voorlopig in te zetten
    output_file = [] # start een lege lijst om de output lijnen voorlopig in te zetten
    for file in os.listdir(directory): # voor elk bestand in het mapje
        if file.endswith('.txt'): # als het bestand een txt bestand is
            print(file) #print de naam van dat bestand
            path = os.path.join(directory, file) # we hebben de volledige 'path' nodig om het te openen
            with open(path, 'r', encoding='utf-8') as f: # open het bestand
                input = f.readlines() # lees het bestand per lijn
            for line in input: # voor elke lijn in dat bestand
                new_line = ''
                for word in line.split(' '): # splits het op op elke spatie, zo krijg je de woorden
                    if '̄' in word and word not in words_with_special_token: # als het teken in het woord zit en we het woord nog niet eerder tegenkwamen
                        words_with_special_token.append(word) #voeg het woord toe aan onze lijst
                    while '̄' in word: # zolang dat we het teken vinden in het woord
                        word_split = word.split('̄') # splitsen we het woord op dat teken, bvb la-ghe = [la, ghe]
                        word = word_split[0][:-1] + replacements[word_split[0][-1]] + ''.join(word_split[1:])
                        # hou het voorste deel van het woord min de laatste letter (bvb l)
                        # zoek naar de unicode voor de letter met streepje op (bvb u'\u0101' voor a)
                        # voeg de rest van het woord toe (bvb ghe)
                        # --> = l\u0101ghe

                    new_line += word + ' ' # voeg het toe aan de lijn
                output_file.append(new_line) #voeg de nieuwe lijn toe aan de output
        with codecs.open(os.path.join(output_path_file, file), 'w', encoding='utf8') as output_f: # we maken een nieuw bestand met dezelfde naam (bvb A.txt) in de nieuwe folder (bvb correcte_unicode)
            for line in output_file:
                output_f.write(line) # schrijf de output naar een bestand
    with open(output_path_list, 'w', encoding='utf-8') as output_l: #open een bestand om de lijst op te slaan
        for i in words_with_special_token:
            output_l.write(i + '\n') # sla de lijst op met op elke regel 1 woord


if __name__ == '__main__':
    input_directory = r'C:\Users\u0144004\OneDrive - KU Leuven\PhD\sofie'
    output_path_list = r'C:\Users\u0144004\OneDrive - KU Leuven\PhD\words_with_special_token.txt'
    output_path_file = r'C:\Users\u0144004\OneDrive - KU Leuven\PhD\correct_unicodes'
    make_list(input_directory, output_path_list, output_path_file)