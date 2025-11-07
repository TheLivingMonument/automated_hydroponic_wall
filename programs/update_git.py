with open("/home/pia-polimi/Desktop/dataHarvesting/data/main_dataset.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    file.close()

l2w = lines[-43200:]

with open("/home/pia-polimi/TheLivingMonument.github.io/data/livingMonumentData.txt", 'w', encoding='utf-8') as file:
    for line in l2w:
        file.write(line)
    file.close()     
