import csv
from csv import reader

# accesses data from Parsingsetup and imports the "Airplane" class
from Parsingsetup import Airplane

# globals
s_airplane = []  # seen
r_airplane = []  # registered

CSV_FILE = "data_Fri 04 Jun 2021 12:00:00 am.csv"


def read(filename):  # describing what you call with a read function
    # reads file and separates with delimiter by tab
    with open(filename) as file_open:
        data_file = reader(file_open, delimiter='\t')  # could say csv.reader(blah)

        for line in data_file:
            parse_data(line)  # function

        file_open.close()


def parse_data(line):  # line is now a list

    if "hexid" in line and "clock" in line and "ident" in line and "alt" in line and "position" in line and "speed" in\
            line and "emergency" in line:
        # grabs the index +1 because the title is the index +0
        index_hex = line.index("hexid") + 1
        index_clock = line.index("clock") + 1
        index_ident = line.index("ident") + 1
        index_alt = line.index("alt") + 1
        index_position = line.index("position") + 1
        index_speed = line.index("speed") + 1
        index_emergency = line.index("emergency") + 1

        # if hexid not found in s_airplane then add to new_airplane. will always run the first time
        if line[index_hex] not in s_airplane:  # line[index_hex] uses line as a list
            s_airplane.append(line[index_hex])  # .append(changes) s_airplane by adding [index_hex] to it
            new_airplane = Airplane(line[index_hex])  # feeds the class "Airplane" a hexid, specifically index_hex
            r_airplane.append(new_airplane)  # adding new_airplane to r_airplane

            new_airplane.set_alt(line[index_alt].split(' ')[0])
            new_airplane.set_clock(line[index_clock])
            new_airplane.set_ident(ident_helper(line[index_ident]).split(' ')[0])
            new_airplane.set_lat(lat_long_helper(line[index_position]).split(' ')[0])
            new_airplane.set_long(lat_long_helper(line[index_position]).split(' ')[1])
            new_airplane.set_speed(line[index_speed].split(' ')[0])
            new_airplane.set_emergency(line[index_emergency].split(' ')[0])

        # for repeating hexid's
        else:
            index_hex = line.index("hexid") + 1
            index_r_airplane = 0

            for plane in r_airplane:
                # if a plane in r_airplane is equal to line[index_hex] this means a repeat
                if plane.get_hexid() == line[index_hex]:
                    index_r_airplane = r_airplane.index(plane)

            # saves new data into r_airplane for repeat
            # feeds data to setters

            r_airplane[index_r_airplane].set_alt(line[index_alt].split(' ')[0])
            r_airplane[index_r_airplane].set_clock(line[index_clock])
            r_airplane[index_r_airplane].set_ident(ident_helper(line[index_ident].split(' ')[0]))
            r_airplane[index_r_airplane].set_lat(lat_long_helper(line[index_position]).split(' ')[0])
            r_airplane[index_r_airplane].set_long(lat_long_helper(line[index_position]).split(' ')[1])
            r_airplane[index_r_airplane].set_speed(line[index_speed].split(' ')[0])
            r_airplane[index_r_airplane].set_emergency(line[index_emergency].split(' ')[0])


def lat_long_helper(coordinates):
    start = coordinates.find("{") + 1
    end = coordinates.find("}")
    tmp_string = coordinates[start:end]
    return tmp_string


def ident_helper(string):
    start = string.find("{") + 1
    end = string.find("}")
    tmp_string = string[start:end]
    return tmp_string

read(CSV_FILE)

'''
list_length = len(r_airplane)
a = 0
while a < list_length:
    print("Hexid: " + str(r_airplane[a].get_hexid()))
    print("Clock: " + str(r_airplane[a].get_clock()))
    print("Identification: " + str(r_airplane[a].get_ident()))
    print("Altitude: " + str(r_airplane[a].get_alt()))
    print("Latitude: " + str(r_airplane[a].get_lat()))
    print("Longitude: " + str(r_airplane[a].get_long()))
    print("Speed(mph): " + str(r_airplane[a].get_speed()))
    print("Emergency Status: " + str(r_airplane[a].get_emergency()))
    print("\n")
    a = a + 1
'''




