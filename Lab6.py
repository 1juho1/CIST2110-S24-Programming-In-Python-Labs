# Lab6
# Author: Justin Hoang

"""_summary_
This lab is designed to get you familiar with Python virtual environments as well as import statments to use external libraries.
"""

# 1. Create a virtual environment called "venv" in the current directory. (Type command here in comments)
#python3pip -m venv env

# 2. Activate the virtual environment. (Type command here in comments)
#source env/bin/activate
# 3. Install the requests library. (Type command here in comments)
#pip install requests

# 4. import requests library here
import requests
# 5. Use the requests library to make a GET request to https://api.github.com/events
response = requests.get("https://api.github.com/events")

# 6. Print out the status code of the response.
print("Status Code:", response.status_code)

# 7. Print out the content of the response.
print("Response Content:", response.text)
# 8. Print out the headers of the response.
print("Response Headers:", response.headers)

# 9. Deactivate the virtual environment. (Type command here in comments)
#deactivate
#
