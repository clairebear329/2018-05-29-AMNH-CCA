'''Here we store some sample ways to read in data and spit out the pieces that we want from the dataset.  Assume all of the data we are using has a header and columns, so that we can read it in using panda's read.csv method.'''


import pandas as pd
def read_my_csv(csvfile):
    '''Our csv files are space separated.  This function will read this in, and ret\
    urn the x and y axis we care about.'''
    data = pd.read_csv(csvfile, sep=' ')
    return data.xaxis, data.yaxis
    print("did it")

if __name__ == "__main__":
        print(read_my_csv('../Data/linear_data.dat'))
else:
        print("nope")
