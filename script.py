import base64
import requests

def encode_file(file_path):
    with open(file_path, "rb") as file:
        encoded_bytes = base64.standard_b64encode(file.read())
        encoded_string = encoded_bytes.decode("utf-8")
        return encoded_string

#set the full path of the file that you need to decode
file_path = ""

encoded_file = encode_file(file_path)

#define your credentials - don't use them directly into production
usertoken = ""
apptoken = ""
recordId = int("")
fieldId = ""
fileName = ""

api_url = ""

# Construct XML data
xml_data = f'''
<qdbapi>
    <usertoken>{usertoken}</usertoken>
    <apptoken>{apptoken}</apptoken>
    <rid>{recordId}</rid>
    <field fid="{fieldId}" filename="{fileName}">{encoded_file}</field>
</qdbapi>
'''

# Define headers
headers = {
    "Content-Type": "application/xml",
    "User-Agent": "Your User Agent",
    "QUICKBASE-ACTION": "API_UploadFile"
}

# Make API request
response = requests.post(api_url, data=xml_data, headers=headers)

# Print response from the endpoint
print("Response from the endpoint:")
print(response.text)
