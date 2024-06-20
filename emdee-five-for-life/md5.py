import requests
import hashlib
import re

url = "http://94.237.49.212:48958/"

session = requests.session()
response = session.get(url)
match = re.search(r"<h3 align='center'>+.*?</h3>", response.text)
matched_text = re.search(r"'>.*<", match[0])
hashed_value = re.search(r"[^|'|>|<]...................", matched_text[0])

hashed_md5 = hashlib.md5(hashed_value[0].encode('utf-8')).hexdigest()

print("Sending MD5: {}".format(hashed_md5))
data = {'hash': hashed_md5}
response = session.post(url=url, data=data)

print(response.text)
