import csv
#with open('baseballdatabank-master/core/People.csv') as csv_file
f = open('../Teams.sql', 'w')
f.write('insert into Teams')
csv_reader = csv.reader(open('../baseballdatabank-master/core/Teams.csv'), delimiter=',')
line_count = 0
row_count = sum(1 for row in csv_reader)
csv_reader = csv.reader(open('../baseballdatabank-master/core/Teams.csv'), delimiter=',')

for line_num, row in enumerate(csv_reader):

    if row_count-1!=line_num:
        ending = ','
    else:
        ending = ';'
        
    if line_num == 0:
        f.write(' values')
    else:

        
        f.write("\n(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)%s"%(\
            f"{row[0]}",\
            "'"+row[1].replace("'","''")+"'",\
            "'"+row[2].replace("'","''")+"'" if not ''== row[2] else "null",\
            "'"+row[4].replace("'","''")+"'" if not '' == row[4] else "null",\
            f"{row[5]}" if not '' == row[5] else "null",\
            f"{row[6]}" if not ''== row[6] else "null",\
            "'"+row[7].replace("'","''")+"'" if not ''== row[7] else "null",\
            f"{row[8]}" if not ''== row[8] else "null",\
            f"{row[9]}" if not ''== row[9] else "null",\
            "'"+row[10].replace("'","''")+"'" if not ''== row[10] else "null",\
            "'"+row[11].replace("'","''")+"'" if not ''== row[11] else "null",\
            "'"+row[12].replace("'","''")+"'" if not ''== row[12] else "null",\
            "'"+row[13].replace("'","''")+"'" if not ''== row[13] else "null",\
            f"{row[14]}" if not ''== row[14] else "null",\
            f"{row[15]}" if not ''== row[15] else "null",\
            f"{row[16]}" if not ''== row[16] else "null",\
            f"{row[17]}" if not ''== row[17] else "null",\
            f"{row[18]}" if not ''== row[18] else "null",\
            f"{row[19]}" if not ''== row[19] else "null",\
            f"{row[20]}" if not ''== row[20] else "null",\
            f"{row[21]}" if not ''== row[21] else "null",\
            f"{row[22]}" if not ''== row[22] else "null",\
            f"{row[23]}" if not ''== row[23] else "null",\
            "'"+row[24].replace("'","''")+"'" if not ''== row[24] else "null",\
            "'"+row[25].replace("'","''")+"'" if not ''== row[25] else "null",\
            f"{row[26]}" if not ''== row[26] else "null",\
            f"{row[27]}" if not ''== row[27] else "null",\
            str(float(row[28])) if not ''== row[28] else "null",\
            f"{row[29]}" if not ''== row[29] else "null",\
            f"{row[30]}" if not ''== row[30] else "null",\
            f"{row[31]}" if not ''== row[31] else "null",\
            f"{row[32]}" if not ''== row[32] else "null",\
            f"{row[33]}" if not ''== row[33] else "null",\
            f"{row[34]}" if not ''== row[34] else "null",\
            f"{row[35]}" if not ''== row[35] else "null",\
            f"{row[36]}" if not ''== row[36] else "null",\
            f"{row[37]}" if not ''== row[37] else "null",\
            "'"+row[38].replace("'","''")+"'" if not ''== row[38] else "null",\
            str(float(row[39])) if not ''== row[39] else "null",\
            "'"+row[40].replace("'","''")+"'" if not ''== row[40] else "null",\
            "'"+row[41].replace("'","''")+"'" if not ''== row[41] else "null",\
            "'"+row[42].replace("'","''")+"'" if not ''== row[42] else "null",\
            f"{row[43]}" if not ''== row[43] else "null",\
            f"{row[44]}" if not ''== row[44] else "null",\
            "'"+row[45].replace("'","''")+"'" if not ''== row[45] else "null",\
            "'"+row[47].replace("'","''")+"'" if not ''== row[47] else "null",\
            ending))
print(f'Processed {line_num} lines.')
f.close()
