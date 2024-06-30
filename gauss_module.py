import math

class GaussDistribution:
    '''
        This class consists of:
        a. An attribute: Input data. Currently, it only supports tuple, set, or list
        b. Methods:
           1. Make mean function: Intended as a function to make average of data given
           2. Make standard deviation function: Intended to return deviation of each data given
    '''
    def __init__(self, data):
        '''
            This function will initialize GaussDistribution class as an object,
            if it is assigned within a variable and given data
        '''
        # To initialize a class, data as input needed
        self.data = data
        # Initialized mean value
        self.mean = 0 
        # Initialized standard deviation value
        self.stdev = 0 
    
    def make_mean(self):
        '''
            To update mean value of data given, try to call this function.
            It has no args needed, as this will process data from __init__ function input.
            This will return two scenario:
            a. It will raise an exception if the data is non-existent.
            b. It will return updated mean value if the data exists, even only 1 data point. 
        '''
        try:
            self.mean = sum(self.data) / len(self.data)
            return self.mean
        except ZeroDivisionError:
            return "Cannot return mean of an empy set data"
    
    def make_stdev(self):
        '''
            To update standard deviation value of data given, try to call this function.
            Same case as make_mean(), this function has no args needed.
            Hence, make sure to input the data well, as it not supports .csv-type data yet
            This will return two scenario:
            a. It will raise an exception if the data is non-existent.
            b. It will return updated standard deviation value if the data exists, even only 1 data point. 
        '''
        try:
            # squared variable store a sequence of squared data points deviation
            # and it is stored as a list
            squared = [(x-self.mean)**2 for x in self.data]
            # the updated self.stdev value will store root-squared average deviation of data
            self.stdev = math.sqrt((sum(squared))/len(squared))
            return self.stdev  
        except ZeroDivisionError:
            return "Cannot return standard deviation of an empy set data"
    
    def __repr__(self):
        '''
            This representation function will appear as you call previous two functions.
            To use this function, just do this:
                print(your_gauss_object_variable)
        '''
        return f''' Mean: {self.mean}, Standard deviation: {self.stdev}'''
    
# Test Case
if __name__ == "__main__":
    # Try a set data type as an input
    data_input = {9, 10, 12}
    # Instantiate an object and use data_input as a value to pass to data arg
    gaussdist = GaussDistribution(data=data_input)
    # Update self.mean() value with this function
    # and store the value within a variable
    gauss_mean = gaussdist.make_mean()
    print("Mean:", gauss_mean)

    gauss_stdev = gaussdist.make_stdev()
    print("Standard Deviation:", gauss_stdev)
