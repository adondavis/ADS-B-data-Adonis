import pandas
import pandas as pds
import csv

from Parsingsetup import Airplane

# globals
s_airplane = []  # seen
r_airplane = []  # registered

CSV_FILE = "data_Fri 04 Jun 2021 12:00:00 am.csv"

def read(filename):
    # reads file and separates with delimiter by tab
    with open(filename) as file_open:
        data_file = csv.reader(file_open, delimiter='\t')

        for line in data_file:
            parse_data(line)

        file_open.close()


def parse_data(line):

    if "hexid" in line and "clock" in line and "ident" in line and "alt" in line and "position" in line and "speed" in\
            line and "emergency" in line:
        # grabs the index +1 because the title is the index +0
        index_hex = line.index("hexid") + 1
        index_clock = line.index("clock") + 1
        index_ident = line.index("ident") +1
        index_alt = line.index("alt") + 1
        index_position = line.index("position") + 1
        index_speed = line.index("speed") + 1
        index_emergency = line.index("emergency") + 1

        # if hexid not found in s_airplane then add to new_airplane
        if line[index_hex] not in s_airplane:
            s_airplane.append(line[index_hex])  # changes index_hex
            new_airplane = Airplane(line[index_hex])  # sets new_airplane as an object
            r_airplane.append(new_airplane)  # adding new_airplane to r_airplane

            # Grabs def from Parsingsetup.py and appends new values
            new_airplane.set_clock(line[index_clock])
            new_airplane.set_ident(line[index_ident])
            new_airplane.set_alt(line[index_alt])
            new_airplane.set_position(line[index_position])
            new_airplane.set_speed(line[index_speed])
            new_airplane.set_emergency(line[index_emergency])

        # for repeating hexid's
        else:
            index_hex = line.index("hexid") + 1
            index_r_airplane = 0

            for p_lane in r_airplane:
                # if getHexid is equal to line[index_hex] this means a repeat
                if p_lane.get_hexid() == line[index_hex]:
                    index_r_airplane = r_airplane.index(p_lane)

            # saves new data into r_airplane for repeat

            r_airplane[index_r_airplane].set_clock(line[index_clock])
            r_airplane[index_r_airplane].set_ident(line[index_ident])
            r_airplane[index_r_airplane].set_alt(line[index_alt])
            r_airplane[index_r_airplane].set_position(line[index_position])
            r_airplane[index_r_airplane].set_speed(line[index_speed])
            r_airplane[index_r_airplane].set_emergency(line[index_emergency])

read(CSV_FILE)
# checks length. I believe representing the number of planes
print(len(r_airplane))
# gives all data for a singular plane based off index value "[]"
a = 13
print("Hexid: " + str(r_airplane[a].get_hexid()))
print("Clock: " + str(r_airplane[a].get_clock()))
print("Identification: " + str(r_airplane[a].get_ident()))
print("Altitude: " + str(r_airplane[a].get_alt()))
print("Position(Lat., Log.): " + str(r_airplane[a].get_position()))
print("Speed(mph): " + str(r_airplane[a].get_speed()))
print("Emergency Status: " + str(r_airplane[a].get_emergency()))





