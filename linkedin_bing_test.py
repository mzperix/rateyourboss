import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import csv

names = ['Peter Burgner']
companies = ['BMW']

YOUR_API_KEY = '857d82f08f7a4e35884e0b7180a21292'

linkedin = []

for name, company in zip(names, companies): # zip to loop over names and companies simultaneously
    
    query = name + company
    
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
                    linkedin.append([name, company, result['displayUrl']])
                    break
                    
    except Exception as e:
        print(e)
        continue
        
# Writing the results to a CSV file
with open('linkedin.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in linkedin:
        writer.writerow(row)
                
print('Number of LinkedIn profiles found:')
print(len(linkedin))
print(linkedin)