import csv

def check_csv(name,year,month,day,attendance):
    with open('Employee.csv', 'r+', newline='') as db:
        reader = csv.reader(db)
        writer = csv.writer(db)

        try:
            heading = next(reader)
        except StopIteration:
            heading = []
            
        db.seek(0)
        for row in reader:
            heading = row
            break
        if heading == ['Name','Year','Month','Day','Attendance']:
            db.seek(0,2)
        else:
            writer.writerow(['Name','Year','Month','Day','Attendance'])
            db.seek(0,2)

        writer.writerow([name,year,month,day,attendance])

if __name__ == '__main__':
    check_csv(['Anurag','2024','January','1','A'])

            
