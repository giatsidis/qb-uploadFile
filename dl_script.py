import requests
import base64

# Define API credentials and file details
realm_hostname = input("Enter your realm hostname: ")
user_token = input("Paste your User Token: ")
file_fid = int(input("Enter FID: "))
record_id = int(input("Enter Record ID: "))
table_id = input("Enter Table ID: ")
version_number = int(input("Enter Version Number(Place 0 if there is no version): "))


file_name = input("Type the name of the file: ")
file_type = input("Type the type of the file(e.g png): ")

# Define headers
headers = {
    "User-Agent": "Your User Agent"
}

# Construct API URL
api_url = f"https://api.quickbase.com/v1/files/{table_id}/{record_id}/{file_fid}/{version_number}"

# Add API and user tokens to headers
headers["QB-Realm-Hostname"] = f"{realm_hostname}"
headers["Authorization"] = f"QB-USER-TOKEN {user_token}"

# Make API request to download the file
response = requests.get(api_url, headers=headers)

# Check response status code
if response.status_code == 200:
    # Decode the base64-encoded file
    decoded_content = base64.b64decode(response.content)

    # Save the decoded file

    filename = f"{file_name}.{file_type}"
    with open(filename, "wb") as file:
        file.write(decoded_content)
    print("File decoded and saved successfully.")
else:
    print("File download failed:", response.text)