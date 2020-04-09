
import requests
from git import Repo

owner = 'guillaumefe'
repository = 'update-readme-with-project-action'
commit = 'automatic website update from projects'

def git_push(repository):
    try:
        repo = Repo()
        repo.git.add(update=True)
        repo.index.commit(commit)
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e:
        print('Some error occured while pushing the code')
        print(e)


# Get project list
response = requests.get(f'https://api.github.com/repos/{owner}/{repository}/projects')

# Write file
with open('test/post_example.md', 'w') as file:
    for entry in response:
        file.write(str(entry))

# Update website
git_push(repository)

print('done')
