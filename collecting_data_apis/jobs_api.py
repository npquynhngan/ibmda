import flask
from flask import request, jsonify
import requests
import re

# Download the jobs.json file using requests
jobs_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
jobs_response = requests.get(jobs_url)
if jobs_response.ok:
    with open("jobs.json", "wb") as file:
        file.write(jobs_response.content)
else:
    print("Failed to download jobs.json")


def get_data(key,value,current):
    results = list()
    pattern_dict = {
        'C': r'(C)',
        'C++': r'(C\+\+)',
        'Java': r'(Java)',
        'C#': r'(C\#)',
        'Python': r'(Python)',
        'Scala': r'(Scala)',
        'Oracle': r'(Oracle)',
        'SQL Server': r'(SQL Server)',
        'MySQL Server': r'(MySQL Server)',
        'PostgreSQL': r'(PostgreSQL)',
        'MongoDB': r'(MongoDB)',
        'JavaScript': r'(JavaScript)',
        'Los Angeles': r'(Los Angeles)',
        'New York': r'(New York)',
        'San Francisco': r'(San Francisco)',
        'Washington DC': r'(Washington DC)',
        'Seattle': r'(Seattle)',
        'Austin': r'(Austin)',
        'Detroit': r'(Detroit)'
    }
    for rec in current:
        print(rec[key])
        print(type(rec[key]))
        print(rec[key].find(value))
        #if rec[key].find(value) != -1:
        import re
        #reex_str = """(C)|(C\+\+)|(JavaScript)|(Java)|(C\#)|(Python)|(Scala)|(Oracle)|(SQL Server)|(MySQL Server)|(PostgreSQL)|(MongoDB)"""
        if re.search(pattern_dict[value],rec[key]) != None:
            results.append(rec)
    return results

app = flask.Flask(__name__)

import json
data = None
with open('jobs.json',encoding='utf-8') as f:
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    

@app.route('/', methods=['GET'])
def home():
    
    return '''<h1>Welcome to flask JOB search API</p>'''


@app.route('/data/all', methods=['GET'])
def api_all():
    return jsonify(data)


@app.route('/data', methods=['GET'])
def api_id():
    # Check if keys such as Job Title,KeySkills, Role Category and others  are provided as part of the URL.
    #  Assign the keys to the corresponding variables..
    # If no key is provided, display an error in the browser.
    res = None
    for req in request.args:
        
        if req == 'Job Title':
            key = 'Job Title'
        elif req == 'Job Experience Required' :
            key='Job Experience Required'
        elif req == 'Key Skills' :
            key='Key Skills'
            
        elif req == 'Role Category' :
            key='Role Category'
        elif req == 'Location' :
            key='Location'
        
        elif req == 'Functional Area' :
            key='Functional Area'
        
        elif req == 'Industry' :
            key='Industry'
        elif req == 'Role' :
            key='Role'
        elif req=="id":
             key="id"
        else:
            pass
    
        value = request.args[key]
        if (res==None):
            res = get_data(key,value,data)
        else:
            res = get_data(key,value,res)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(res)

app.run()