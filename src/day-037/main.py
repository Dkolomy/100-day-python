import requests
from datetime import datetime

TODAY = datetime.now().strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "1234567890"
USERNAME = "dkolomy"
GRAPH_ID = "graph1"

# Create a new user
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(pixela_endpoint, json=user_params) # Create a new user
# print(response.text)

# Create a graph definition for reading
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(graph_endpoint, json=graph_config, headers=headers) # Create a graph definition
# print(response.text)

# Create a pixel for reading
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": TODAY,
    "quantity": "10",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(pixel_endpoint, json=pixel_config, headers=headers) # Create a pixel for reading
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
update_config = {
    "quantity": "10",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
response = requests.put(update_endpoint, json=update_config, headers=headers) # Update a pixel for reading
print(response.text)

# Delete a pixel for reading
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
headers = {
    "X-USER-TOKEN": TOKEN,
}
response = requests.delete(delete_endpoint, headers=headers) # Delete a pixel for reading
print(response.text)