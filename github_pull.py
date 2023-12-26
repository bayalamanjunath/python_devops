import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(type(response))
print(response.status_code)
list_users = (response.json())

for i in range(len(list_users)):
    print(i)
    print(list_users[i]["user"]["login"])