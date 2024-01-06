import csv

def read_csv():
    with open('Employee.csv','r') as db:
        record = csv.reader(db)
        heading = next(record)
        print(f"The heading is {heading}")
        for row in record:
            if row[2] == 'January' and row[3] < '32':
                print(row)

if __name__ == '__main__':
    read_csv()
