'''
Azure Blob storage for text files
Developed By: Rahul Ramawat
Verison: 1.0
'''

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob storage sample")
    # environment variable into account.
    #connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    #Replace the connection string with your storage account 
    connect_str = "*******"
    # Quick start code goes here
    #  create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    # unique name for container
    container_name = "blobstor1" + str(uuid.uuid4())

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    local_path = "C://AzureData//txtData"  # please give the appropriate path
    #local_file_name = "urls_pos" + str(uuid.uuid4()) + ".txt"
    local_file_name = "urls_pos.txt"
    #os.rename(r'C://AzureData//txtData//*.txt',r'C://AzureData//txtData//%local_file_name.txt')
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file if testing for blob storage 
    '''
    file = open(upload_file_path, 'w')
    file.write("Testing!")
    file.close()
    '''

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)
    
    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

   
    #deleting the blob container

    # Clean up
    #print("\nPress the Enter key to begin clean up")
    #input()

    #print("Deleting blob container...")
    #container_client.delete_container()

except Exception as ex:
    print('Exception:')
    print(ex)

