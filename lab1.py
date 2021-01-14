import requests
import os

# virtualenv 

# step 4
print(requests.__version__)


# curl

# step 5
google = requests.get('https://www.google.com/')
print(google)

# step 10
lab1 = requests.get("https://raw.githubusercontent.com/PPPeterZhou/CMPUT404/main/lab1.py")
print(lab1.text)