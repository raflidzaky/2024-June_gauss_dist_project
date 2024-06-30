# This module is intended to make gauss distribution behavior, given data 
# Put the data as csv
import pandas as pd
import math
import time

class GaussDistribution:
    def __init__(self, data):
        self.data = data
        self.mean = 0
        self.stdev = 0
    
    def make_mean(self):
        try:
            self.mean = sum(self.data) / len(self.data)
            return self.mean
        except ZeroDivisionError:
            return "Cannot return mean of an empy set data"
    
    def make_stdev(self):
        try:
            squared = [(x-self.mean)**2 for x in self.data]
            self.stdev = math.sqrt((sum(squared))/len(squared))
            return self.stdev  
        except ZeroDivisionError:
            return "Cannot return standard deviation of an empy set data"
    
    def __repr__(self):
        return f''' Mean: {self.mean}, Standard deviation: {self.stdev}'''
