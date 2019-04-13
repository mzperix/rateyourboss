from flask import Flask, render_template, session, request, redirect, url_for
#from wtforms import Form, TextField
import random
import json
from linkedin_search import search_linkedin_urls
import scrape 
import parameters

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = parameters.key

with open('db2.json') as json_file:  
    db = json.load(json_file)

@app.route('/profile/<profile_id>')
def profile(profile_id):
    if profile_id in db['people']:
        response = db['people'][profile_id]
    else:
        response = {}
    return json.dumps(response)

def empty_profile():
    return db['people']['__empty__'].copy()

def create_profile(profile_id, name, linkedin_url, company=""):
    if not (profile_id in db['people']):
        data = empty_profile()
        data['name'] = name
        data['linkedin_url'] = linkedin_url
        data['company'] = company
        db['people'][profile_id] = data
    with open('db2.json','w') as json_file:  
        json.dump(db, json_file)
    return data

@app.route('/search/<query>')
def search(query):
    search_results = search_linkedin_urls(query, '')
    formatted_results = []
    for res in search_results:
        name = res[0]
        linkedin_url = res[2]
        profile_id = linkedin_url.split('/in/')[-1]
        formatted_results.append({'name': name, 
            'photo_url': res[1], 
            'linkedin_url': linkedin_url, 
            'profile_url': 'http://localhost:3000/profile/'+profile_id})
        if not profile_id in db['people']:
            create_profile(profile_id, name, linkedin_url)
    return json.dumps(formatted_results)

def get_id_by_name(name):
    return hash(name)

@app.route('/relevant_results/<linkedin_url>')
def scrape_relevant_results(linkedin_url):
    results = scrape.get_relevant_people(linkedin_url)
    return json.dumps(results)

if __name__ == '__main__':
    #app.debug = True
    #scrape.login_driver()
    app.run(host = '0.0.0.0', port=5005)