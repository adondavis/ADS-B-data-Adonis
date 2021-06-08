import pandas
import pandas as pds
import csv

class Airplane:

    def __init__(self, hexid):
        self.hexid = hexid  # airplane identification from pi
        self.clock = []  # data every second
        self.ident = []  # airplane identification
        self.alt = []  # altitude
        self.position = []  # position
        # bself.alt_gnss = []
        self.speed = []  # speed
        # self.track = []
        # self.nav_qnh = []
        self.emergency = []  # if emergency status active

    # getter and setter setup
    

    def set_hexid(self, v):
        self.hexid.append = v

    def get_hexid(self):
        return self.hexid

    def set_clock(self, v):
        self.clock.append(v)

    def get_clock(self):
        return self.clock

    def set_ident(self, v):
        self.ident.append(v)

    def get_ident(self):
        return self.ident

    def set_alt(self, v):
        self.alt.append(v)

    def get_alt(self):
        return self.alt

    def set_position(self, v):
        self.position.append(v)

    def get_position(self):
        return self.position

    def set_speed(self, v):
        self.speed.append(v)

    def get_speed(self):
        return self.speed

    def set_emergency(self, v):
        self.emergency.append(v)

    def get_emergency(self):
        return self.emergency
