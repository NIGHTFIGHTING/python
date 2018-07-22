#-*- coding: utf-8 -*-

class Home:
    def __intit__(self, new_area, new_info, new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area

    def __str(self):
        return ("area=%d, left_area=%d, info=%s , addr=%s"%(self.area, self.left_area, self.info, self.addr)) 

    def add_item(self,item):
        self.left_area -= item.area



class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return ("name=%s ,area=%d"%(self.name, self.area))


#fangzi = Home(129, "three wuzi", "liuchengyuan")
fangzi = Home()
