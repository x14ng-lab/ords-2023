import os
import pandas as pd
import zipfile
import requests
from io import BytesIO

def get_data(filename, link, redownload = False, **kwargs):
   """
   Retrieve data from a local file or download it from a provided link.

   Args:
   - filename (str): The name of the file to check or download.
   - link (str): The URL link to download the file if it's not available locally or redownload is True.
   - redownload (bool, optional): Flag to force redownload the data even if it exists locally. Defaults to False.
   - **kwargs: Additional keyword arguments passed to the pandas read function.

   Returns:
   - pd.DataFrame: A DataFrame containing the data from the specified file.
   """
   if filename not in os.listdir("Data"):
       redownload = True
   else:
      if redownload == False:
         print(f"Reading {filename} from local...")
         df = pd.read_csv(f"Data/{filename}")
    
   if redownload:
      print(f"Downloading data from '{link}'...")
      if link[-3:] != "csv":
         df = pd.read_excel(link, **kwargs)
      else:
         df = pd.read_csv(link, **kwargs)
      print("Downloaded")
      df.to_csv(f"Data/{filename}", index=False)
        
   return df

def get_data_zip(filename, link = '', redownload=False):
   """
   Retrieve data from a local file or download it from a ZIP archive at a provided URL.

   Args:
   - filename (str): The name of the file to check or download.
   - link (str, optional): The URL link to download the ZIP archive if the file is not available locally or redownload is True. Defaults to an empty string.
   - redownload (bool, optional): Flag to force redownload the data even if it exists locally. Defaults to False.

   Returns:
   - pd.DataFrame: A DataFrame containing the data from the extracted file.
   """
   found = False #Flag for indicating if it is found the required data
   if filename not in os.listdir("Data"):
      redownload = True
   else:
      if redownload == False:
         print(f"Reading {filename} from local...")
         df = pd.read_csv(f"Data/{filename}")
   
   if redownload:
      print(f"Downloading ZIP data from '{link}'...")
      response = requests.get(link)
      zip_file = zipfile.ZipFile(BytesIO(response.content))
      # Assuming the first file in the ZIP is the target data file (indeed it is!)
      data_file_name = zip_file.namelist()
      for data in data_file_name:
         if data.endswith('.csv') and data == filename:
            print(f'Downloading {data} file...')
            df = pd.read_csv(zip_file.open(data))
            found = True
            break;
      if found == False:
         raise ValueError(f'{filename} not found in {link}')
      else:      
         print("Downloaded")
         df.to_csv(f"Data/{filename}", index=False)

   return df

def get_local_csv(filename, reread,folder='', **kwargs):
   """
   Reads a CSV file from a specified local directory or updates it if necessary.

   Args:
   - filename (str): The name of the CSV file to be read.
   - reread (bool): Flag to determine whether to re-read and update the file from its specific folder.
   - folder (str, optional): The specific subfolder in 'Data' where the file might be located. Defaults to an empty string.
   - **kwargs: Additional keyword arguments passed to pandas read_csv function.

   Returns:
   - pd.DataFrame: A DataFrame containing the data from the CSV file.
   """
   if filename not in os.listdir("Data") and filename not in os.listdir("Data/AddressBook") and filename not in os.listdir("Data/BNF Code") and filename not in os.listdir("Data/Population"):
      raise ValueError("File NOT found!")
   else:
      if reread:
         print(f"Updating {filename} from local...")
         df = pd.read_csv(f"Data/{folder + '/'}{filename}")
         df.to_csv(f"Data/{filename}")
      else:
         if filename not in os.listdir("Data"):
            print(f"No existed file so it is updating {filename} from local...")
            df = pd.read_csv(f"Data/{folder + '/'}{filename}")
            df.to_csv(f"Data/{filename}")
         else:
            print(f"Reading {filename} from local...")
            df = pd.read_csv(f"Data/{filename}")

   return df