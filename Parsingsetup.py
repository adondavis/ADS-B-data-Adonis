import pandas
import pandas as pds
import csv

class Airplane:

    def __init__(self, hexid):
        self.hexid = hexid #airplane identification from pi
        self.clock = [] #data every second
        self.indent = [] #airplane identification
        self.alt = [] #altitiude
        self.position = [] #position
        #self.alt_gnss = []
        self.speed = [] #speed
        #self.track = []
        #self.nav_qnh = []
        self.emergency = [] #if emergnecy status active

    #getter and setter
    

    def set_hexid(self, v):
        self.hexid = v

    def get_hexid(self):
        return self.hexid

    def set_indent(self, v):
        self.indent = v

    def get_indent(self):
        return self.indent

    def set_alt(self, v):
        self.alt.append = v

    def get_alt(self):
        return self.alt

    def set_position(self, v):
        self.position.append = v

    def get_position(self):
        return self.position

    def set_speed(self, v):
        self.speed.append = v

    def get_speed(self):
        return self.speed

    def set_emergency(self, v):
        self.emergency = v

    def get_emergency(self):
        return self.emergency
