import requests
import os

# virtualenv 

# step 4
print(requests.__version__)


# curl

# step 1
url = "http://google.com/"

cmd = "curl " + url
print("\nCommand:", cmd, "\n")
os.system(cmd)

# step 2
cmd = "curl -i " + url
print("\nCommand:", cmd, "\n")
os.system(cmd)
res = requests.get(url)
print(res.status_code)

# step 3
cmd = "curl -iL " + url
print("\nCommand:", cmd, "\n")
os.system(cmd)

# step 4
url = "https://www.google.com/teapot"

cmd = "curl -i " + url
print("\nCommand:", cmd, "\n")
os.system(cmd)
res = requests.get(url)
print(res.status_code)

cmd = "curl -iL " + url
print("\nCommand:", cmd, "\n")
os.system(cmd)
res = requests.get(url)
print(res.status_code)

cmd = "curl " + url
print("\nCommand:", cmd, "\n")
os.system(cmd)

# step 5
url = "http://google.com/"
res = requests.get(url)

# step 6

url = "https://webdocs.cs.ualberta.ca/~hindle1/1.py"
cmd = "curl -i " + url
print("\nCommand:", cmd, "\n")
os.system(cmd)

# step 7
cmd = 'curl -i -X POST -d "X=Y" ' + url 
print("\nCommand:", cmd, "\n")
os.system(cmd)

