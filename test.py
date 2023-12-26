import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(type(response))
print(response.status_code)
pull_details = (response.json())

# for i in range(len(pull_details)):
#     print(pull_details[i]["user"]["login"])
#     print("===========================end=======================")
pr_creator = {}
for pull in pull_details:
    puller = pull["user"]["login"]
    if puller in pr_creator:
        pr_creator[puller] += 1
    else:
        pr_creator[puller] = 1
for puller, count in pr_creator.items():
    print(f"{puller}: {count} PRs")