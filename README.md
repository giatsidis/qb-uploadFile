# Quickbase XML API_UploadFile python script

## How to run the script

##### 1. Download the latest version of python: https://www.python.org/downloads/
##### 2. Make sure that you add Python to the PATH
##### 3. For upload you need to add the details directly to the script and run it from the terminal. To download the file just run the script from terminal and follow the steps.

## Script Flow

### 1. Encodes a file to base64 format
### 2. Generates the XML body of the request
### 3. Makes a POST request to upload the file on an existing record to Quickbase


## Update
### Added dl_script

#### I added a script that downloads the file attachment from a Quickbase table.
#### Same proccess in reverse, makes a GET request to download the file and then decodes and saves it.


#####  Documentations 
###### 1. https://helpv2.quickbase.com/hc/en-us/articles/4418287669652
###### 2. https://developer.quickbase.com/operation/downloadFile
