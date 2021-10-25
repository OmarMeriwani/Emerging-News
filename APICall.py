import requests
import json
from rdflib import Graph

ACCESS_TOKEN = "cJ5773mhNpDCXNgP"

response = requests.get("http://newshunter.uib.no:5555/news?access_token="+ACCESS_TOKEN)
data = json.loads(response.content)
rdf_data = data["nh:Dataset"]
g = Graph().parse(data=rdf_data, format='turtle')


ttl = g.serialize(format='turtle', encoding='utf-8').decode('utf-8')
print(ttl)
g.serialize(destination="output.ttl", format = "turtle")