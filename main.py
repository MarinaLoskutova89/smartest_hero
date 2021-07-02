import requests

api_url = "https://superheroapi.com/api/2619421814940190/search/"
superhero  = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
for hero in superhero:
  api_request = requests.get(api_url + hero['name'])
  hero['intelligence'] = int(api_request.json()['results'][0]['powerstats']['intelligence'])
smaterst_hero = sorted(superhero, key=lambda hero: hero['intelligence'])
print(smaterst_hero[-1]['name'])








