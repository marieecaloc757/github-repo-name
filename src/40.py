import requests
import os

url = "https://api.github.com/repos/school-project-name/Adescription-of-my-GitHub-repo-for-my-school-project/"
response = requests.get(url)
data = response.json()

if data["code"] == 200:
    name = data["name"]
else:
    print("Failed to retrieve the description. Please check your URL and GitHub token.")
    exit()
print(f"GitHub repository: {name}")
