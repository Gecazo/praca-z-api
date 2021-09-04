import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")
response_dict = r.json()

print(response_dict.keys())

repo_dicts = response_dict['items']
print(f"Liczba zwroconych repozytoriow: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKlucze: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)