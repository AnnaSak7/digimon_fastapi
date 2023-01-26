import csv

with open('digimon.csv', mode='r') as csvfile:
    data = csvfile.read()

rows = data.split('\n')

# Create a dictionary
digimonData ={}

for row in rows:
    info = row.split(',')
    digimon = {}
    # Separate out the data
    number = info[0]
    digimon['number'] = int(info[0])
    digimon['digimon'] = info[1]
    digimon['stage'] = info[2]
    digimon['type'] = info[3]
    digimon['attribute'] = info[4]
    digimon['memory'] = int(info[5])
    digimon['equipSlots'] = int(info[6])
    digimon['lv50HP'] = int(info[7])
    digimon['lv50SP'] = int(info[8])
    digimon['lv50Atk'] = int(info[9])
    digimon['lv50Def'] = int(info[10])
    digimon['lv50Int'] = int(info[11])
    digimon['lv50Spd'] = int(info[12])
    
    # Populate the dictionary
    digimonData[number] = digimon

    