import pandas as pd
import argparse
from google.cloud import storage
import os
import io

def gcp_csv_to_df(bucket_name, source_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_file_name)
    data = blob.download_as_string()
    df = pd.read_csv(io.BytesIO(data))
    print(f'Pulled down file from bucket {bucket_name}, file name: {source_file_name}')
    return df

def read_data(data_path):
    data = gcp_csv_to_df(data_path,'train.csv')
    #display basic information about the dataset
    print('Dataset stats ->\n',data.describe())
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data Prep code')
    parser.add_argument('--data_path', type=str)
    args = parser.parse_args()
    #call the data prep function
    read_data(args.data_path)