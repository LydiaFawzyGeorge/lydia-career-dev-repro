import csv

class read_file:
    def read_csv_file(colnum):
        ifile = open('LoginData.csv', 'rb')
        reader = csv.reader(ifile)

        rownum = 0

        for row in reader:
        # Save header row.
            if rownum == 0:
               header = row
        else:
             colnum = 0
        for col in row:
            if col==colnum:
               print  ('HELOOOOOZ'+row[colnum])


        ifile.close()