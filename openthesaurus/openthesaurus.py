import urllib.parse
import urllib.request
import json
import sys

def get_synonyms(term):
    api_url = 'http://www.openthesaurus.de/synonyme/search'
    params = urllib.parse.urlencode({'q': term, 'format': 'application/json'})
    response = urllib.request.urlopen(api_url + '?' + params)
    data = json.loads(response.read())
    synonyms = [o["term"] for o in data["synsets"][0]["terms"]]
    return synonyms


if __name__ == "__main__":
	alfred_input = sys.argv[1]
	synonyms = get_synonyms(alfred_input)
	items = [{"title": k} for k in synonyms]
	response = json.dumps({"items": items})
	print(response)