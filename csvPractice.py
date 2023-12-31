import csv

#with open(r'\\172.16.22.101\\Users\\POS\\Documents\\Scripts\\PriceTierChanger2\\PriceTiering.csv') as csv_file:
#with open(r'\\BJRI-FILE-004\\Departments\\IS\\Restaurant Systems\\Scripts\\PriceTiering.csv') as csv_file:
with open(r'\\bjri-jump-001\\Menu_Team\\Scripts\\PriceTiering.csv') as csv_file:


    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')