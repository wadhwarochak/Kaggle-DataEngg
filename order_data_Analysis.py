import kagglehub
import zipfile
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("ankitbansal06/retail-orders")
project_path = "D:\Rochak\MyRepositories\Kaggle-DataEngg"
print("Path to dataset files:", path)

'''
#extract file from zip file
Below code to be used, if downloading extracting from zipped file
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file
'''

#read data from the file and handle null values

file_path = project_path + "\\" + "orders.csv"

df = pd.read_csv(file_path,na_values=['Not Available','unknown'])
df['Ship Mode'].unique()

# done till 10 mins