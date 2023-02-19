#%%
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import pandas as pd
from functools import reduce
import os
import glob
connect_str = "DefaultEndpointsProtocol=https;AccountName=azuredatafactoryproject;AccountKey=2G2UAqzkLulfRlJQTJNk82QUTOQrmBMIPtaCpqF45tXpFDH/bHsdxG2Qq0jJ7UAnKfMMMpGqOLpR+ASt6thmpQ==;EndpointSuffix=core.windows.net"
container_name = "input"

def upload_file(source, dest):
    print(f'Uploading {source} to {dest}')
    with open(source, 'rb') as data:
      container_client_output.upload_blob(name=dest, data=data)

def download(source, dest):
    '''
    Download the directory to a path on the local filesystem
    '''
    print("\nListing blobs...")
    blob_list = container_client_input.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)
        blob_client = container_client_input.get_blob_client(blob.name)
        with open(blob.name, "wb") as my_blob:
            download_stream = blob_client.download_blob()
            my_blob.write(download_stream.readall())

def clean_up(source, paths, down_files, upload_files):
    for path in paths:
        print(f'Cleaning up {path}')
        os.remove(path)
        
    for file in upload_files:
            print(f'Cleaning up {file}')
            os.remove(file)

    for file in down_files:
            print(f'Cleaning up {file}')
            os.remove(file)
            #os.rmdir(source)

    print("Deleting blob container...")
    container_client_input.delete_container()
    print("Deleting the local source and downloaded files...")
    print("Done")   


#%%
try:
    dest = '' 
    source='input'
    service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client_input = service_client.get_container_client(container_name)
    container_client_output = service_client.get_container_client("output")
    import pandas as pd
    import time

    #download from blob
    t1=time.time()

    # Read from input container    
    download("input",'')
 
    amazon = pd.read_csv('AMAZON.csv')
    apple = pd.read_csv('APPLE.csv')
    microsoft = pd.read_csv('MICROSOFT.csv')
    google = pd.read_csv('GOOGLE.csv')
    facebook = pd.read_csv('FACEBOOK.csv')
    tesla = pd.read_csv('TESLA.csv')
    zoom = pd.read_csv('ZOOM.csv')

    df = pd.concat([amazon,apple,microsoft,google,facebook,tesla,zoom], ignore_index=True)
    df.to_csv('STOCKS.csv', index=False)

    dest = "output"
    prefix = '' if dest == '' else dest + '/'

    for root, dirs, files in os.walk(source):
        dir_part = os.path.relpath(root, source)
        dir_part = '' if dir_part == '.' else dir_part + '/'
        file_path = 'STOCKS.csv'#os.path.join(root, "STOCKS.csv")
        blob_path = "STOCKS.csv"
        upload_file(file_path, blob_path)

    #clean_up(source, paths, down_files, upload_files)
    #print(glob.glob('downloads/**', recursive=True))


except Exception as ex:
    print('Exception:', ex)
