import requests
import os

url = "https://api.github.com/search/repositories?q=github%20project"
response = requests.get(url)
data = response.json()

for repo in data["items"]:
    print(f"Repository: {repo['name']}")
    if "stars" in repo:
        stars_count = repo["stargazers_count"]
        print(f"Stars count: {stars_count}")

