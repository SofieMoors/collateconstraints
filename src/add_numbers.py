import re
from copy import deepcopy
# input: txt, af en toe nummer

#nummer aan elke lijn toevoegen


def add_numbers(text_file, output_text_file):
    with open(text_file, 'r', encoding='utf-8') as input_file: # open het bestand
        input = input_file.readlines() # lees het in, maak een lijst met 1 item = 1 lijn in de txt
        output = deepcopy(input) # niets aanpassen aan de input, maar aan de output

    last_line = 0
    for index, line in enumerate(input): # ga door elke lijn, en tel ook op welke lijn je zit (= index)
        if not re.match(r'^&', line) and not re.match(r'\s*\n', line): # lijnen met & en lege lijnen negeren
            if re.match(r'^[0-9]', line):
                try:
                    last_line = int(re.sub(' .*$', '', line)) # herken het nummer als er eentje staat, dat wordt nu het
                                                                # nummer van de laatste lijn
                    line_number = str(last_line).zfill(3)
                    line_no_number = re.sub('^[0-9]* ', '', line)
                    output[index] = f'{line_number} {line_no_number}'
                except: # de lijn-nummer gewoon +1 doen als de 'try' niet lukt (dus als het nummer niet herkend wordt)
                    last_line += 1
            if not re.match(r'^[0-9]', line): #als er geen nummer aan de start van de regel staat
                last_line += 1 # 1 meer dan de laatste lijn
                line_number = str(last_line).zfill(3)
                output[index] = f'{line_number} {line}'
    with open(output_text_file, 'w', encoding='utf-8') as output_file:
        for line in output:
            output_file.write(line)


if __name__ == '__main__':
    input_text_file = r'C:\Users\u0144004\OneDrive - KU Leuven\PhD\TxT_A.txt'
    output_text_file = r'C:\Users\u0144004\OneDrive - KU Leuven\PhD\TxT_A_processed.txt'
    add_numbers(input_text_file, output_text_file)

