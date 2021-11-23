import pandas as pd
import argparse

def read_data(data_path):
    data = pd.read_csv(data_path)
    #display basic information about the dataset
    print('Dataset stats ->\n',data.describe())
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data Prep code')
    parser.add_argument('--data_path', type=str)
    args = parser.parse_args()
    #call the data prep function
    read_data(args.data_path)