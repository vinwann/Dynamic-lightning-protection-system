import os
import shutil
import time
from google.cloud import storage
file_path = r'G:\phase 3'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(file_path,'serene-snowfall-414405-5220794367c6.json')
csv_files = [file for file in os.listdir(file_path) if file.endswith('.csv')]

storage_client = storage.Client()
bucket_name = 'ieee9bus'
# Create a new bucket
bucket = storage_client.bucket(bucket_name)
# bucket.storage_class = 'COLDLINE'  # Archive | Nearline | Standard
bucket.location = 'ASIA'  # Taiwan
#my_bucket = storage_client.create_bucket(bucket_name)  # Pass the bucket name directly

#print(vars(my_bucket))

def download(blob_name,file_path,bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        #blob.upload_from_filename(file_path)
        with open(file_path,'wb') as f:
            storage_client.download_blob_to_file(blob,f)
        return True
    except Exception as e:
        print(e)
        return False
    
def upload_to_bucket(blob_name,file_path,bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False
count = 0    
while count < len(csv_files):

    status = upload_to_bucket('phase 3/'+csv_files[count],os.path.join(file_path,csv_files[count]),bucket_name)
    
    if status:
        print(csv_files[count]+" done")
        source_path = os.path.join(file_path,csv_files[count])
        destination_path = os.path.join(file_path,'uploaded')
        destination_path = os.path.join(destination_path,csv_files[count])
        shutil.move(source_path, destination_path)
        count += 1
    else:
        print("Connection failed trying in another 30 seconds")
        time.sleep(30)





#download('L_4_5_117_3.csv',os.path.join(os.getcwd(),'file_1.csv'),bucket_name)