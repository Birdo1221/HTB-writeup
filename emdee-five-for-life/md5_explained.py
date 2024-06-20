import requests
import hashlib
import re

# Define the URL to target
url = "http://94.237.49.212:48958/"

# Initialize a session for persistent connection
session = requests.session()

# Send GET request to retrieve initial HTML content
response = session.get(url)

# Extract the <h3> tag content from the HTML response
match = re.search(r"<h3 align='center'>+.*?</h3>", response.text)

# Extract the text between '>' and '<' from the matched <h3> tag
matched_text = re.search(r"'>.*<", match[0])

# Extract the hashed value (adjust the regex pattern as per actual HTML structure)
hashed_value = re.search(r"[^|'|>|<]...................", matched_text[0])

# Calculate the MD5 hash of the extracted value
hashed_md5 = hashlib.md5(hashed_value[0].encode('utf-8')).hexdigest()

# Print the MD5 hash value being sent
print("Sending MD5: {}".format(hashed_md5))

# Prepare POST data with the hashed MD5 value
data = {'hash': hashed_md5}

# Send POST request with the hashed MD5 value
response = session.post(url=url, data=data)

# Print the response text from the server
print(response.text)
