#%% Load Librairies
from azure.storage.blob import BlobClient
import pandas as pd

from functools import reduce



#%% Define parameters
connectionString = "DefaultEndpointsProtocol=https;AccountName=azuredatafactoryproject;AccountKey=2G2UAqzkLulfRlJQTJNk82QUTOQrmBMIPtaCpqF45tXpFDH/bHsdxG2Qq0jJ7UAnKfMMMpGqOLpR+ASt6thmpQ==;EndpointSuffix=core.windows.net"
containerName = "output"
outputBlobName = "STOCKS.csv"

# Establish connection with a blob storage account
blob = BlobClient.from_connection_string(conn_str=connectionString, container_name=containerName, blob_name=outputBlobName)

#%% Load STOCKS dataset from the task node

amazon = pd.read_csv('AMAZON.csv')
apple = pd.read_csv('APPLE.csv')
microsoft = pd.read_csv('MICROSOFT.csv')
google = pd.read_csv('GOOGLE.csv')
facebook = pd.read_csv('FACEBOOK.csv')
tesla = pd.read_csv('TESLA.csv')
zoom = pd.read_csv('ZOOM.csv')

df = reduce(lambda left, right : pd.merge(left, right,on=['Date'], how='outer'), [amazon,apple,microsoft,google,facebook,tesla,zoom])

# Take a subset of the records 
#df = df[['Date','High','Low','Open','Close','Volume','Adj Close', 'company_name']]

# Save the subset of the STOCKS dataframe locally in the task node 
df.to_csv(outputBlobName, index=False)

with open(outputBlobName, "rb") as data:
    blob.upload_blob(data)
# %%
