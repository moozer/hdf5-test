import datetime

smadatafile = "SmaData_20160907.dat"
header_lines_count = 25

def read_data_line( string ):
    # a data line looks lik this
    #7/9/2016 09:20:00  total=36556.891 Kwh current=720 Watts togo=0 i=11 crc=215927136
    datestr, datastr = line.split('  ')

    date = datetime.datetime.strptime(datestr, "%d/%m/%Y %H:%M:%S")
    data = datastr.split(' ')

    total = data[0].split('=')[1]
    current = data[2].split('=')[1]
    togo = data[4].split('=')[1]
    i = data[5].split('=')[1]
    crc = data[6].split('=')[1].strip()

    return { 'date': date, 'total_kWh': float(total), 'current_W': int(current),
             'togo': int(togo), 'i': int(i), 'crc': int(crc)}


if __name__ == "__main__":
    line_count = 0

    print "Date\ttotal kWh\tcurrent W\ttogo\ti\tcrc"
    with open( smadatafile, "r") as f:
        for line in f:
            line_count += 1

            if line_count < header_lines_count:
                continue

            parsed_data = read_data_line( line )
            print "%(date)s\t%(total_kWh).3f\t%(current_W)d\t%(togo)d\t%(i)d\t%(crc)d"%parsed_data
