import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import csv

YOUR_API_KEY = '857d82f08f7a4e35884e0b7180a21292'

def search_linkedin_urls(name, company):    

    query = name+company+' linkedin'
    linkedin = ()
    try:
        headers = {'Ocp-Apim-Subscription-Key': YOUR_API_KEY }
        params = urllib.parse.urlencode({'q': query,'count': '2'}) # returns top 2 (German) results
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v7.0/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        json_file = json.loads(data)
        conn.close()

        print(json_file)

        for result in json_file['webPages']['value']:
            title = result['name']
            if name.lower() in title.lower(): # checks if the name appears in the title
                if 'linkedin.com/in/' in result['displayUrl']: # checks if the search result URL is a LI profile
                    linkedin += ([name, company, result['displayUrl']],)
                    break
                    
    except Exception as e:
        print(e)
            
    print('Number of LinkedIn profiles found:')
    print(len(linkedin))
    print(linkedin)
    return linkedin