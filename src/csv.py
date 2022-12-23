import csv

with open('10_02_us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')  #   this reader is not a list but it is iterable
    for row in reader:
        print(row)

#   CSV FILE is not parsed correctly because of tab separated values hence delimiter arguement




#   we are calling next to skip the headers of the csv files

with open('10_02_us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    next(reader)
    for row in reader:
        print(row)

#   same thing except list slicing syntax

with open('10_02_us.csv', 'r') as f:
    reader = list(csv.reader(f, delimiter='\t'))
    for row in reader[1:]:
        print(row)


#   if you do not want the csv as a header but as used as a key for a list of dicitonaries

with open('10_02_us.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        print(row)


#   Filtering Data

primes = []
for number in range(2, 99999):
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            break
    else:
        primes.append(number)

with open('10_02_us.csv', 'r') as f:
    data = list(csv.DictReader(f, delimiter='\t'))

data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']
len(data)

#   writing to a csv file for all the results

with open('10_02_ma_prime.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow([row['place name'], row['county']])
