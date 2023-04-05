import csv

filename = 'realestate.csv'

with open (filename, encoding= 'utf-8-sig') as f:
    reader = csv.reader(f,delimiter=',')

    with open ('#9.csv', 'w') as new_file:
        writer = csv.writer(new_file) #csv.writer provides two methods for writing: writerow() and writerows()
        
        for row in reader:
            writer.writerow(row)
