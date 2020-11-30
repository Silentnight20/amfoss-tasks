import base64
import os
from github import Github
from pprint import pprint

username = "amFoss"
g = Github()
user = g.get_user(username)
repo_set = []

for repo in user.get_repos():
    print(repo)
    repo_set.append(str(repo))
print("\n")

for x in range(len(repo_set)):
    repo_set[x] = repo_set[x].lstrip('Repository(full_name="').rstrip('")')
    command ="perceval git --json-line https://github.com/amfoss%s>> commits.json"%(repo_set[x])
    os.system(command)