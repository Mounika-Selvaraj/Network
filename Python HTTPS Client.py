import requests

# Disable SSL warnings (only for testing with self-signed certificates)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://localhost"
response = requests.get(url, verify=False)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
