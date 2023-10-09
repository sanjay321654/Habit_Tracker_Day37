import requests
from datetime import datetime


TOKEN = "x#$(HSTUU(E5f65"
USERNAME = "sanjay20102002"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

login_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


login_response = requests.post(url=pixela_endpoint, json=login_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


today = datetime.now()

endpoint_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

data_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers you walked today: "),
}

data_response = requests.post(url=endpoint_pixel, json=data_pixel, headers=headers)
print(data_response.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
params_put = {
    "quantity": "30.22"
}

# put_response = requests.put(url=put_endpoint, json=params_put, headers=headers)
# print(put_response)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)

