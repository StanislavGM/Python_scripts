import requests
import json
"""
r = requests.post('http://10.50.173.103:3000', ) #auth=('nvxfrost@gmail.com', 'Fr0stxt2011!')

print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.text)
print(r.json())

token = ""
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'Accept': 'application/json'}
grafana_url_post = "http://192.168.191.16:3000/"
token = ""
r = requests.get(url=grafana_url_post+'/api/folders/pkbg_Zs4z', headers=headers)
print(r.json())
"""

def import_dashboard():
    grafana_url_post = "http://192.168.191.16:3000/"
    token = ""
    files = {'file': open('chart.json', 'r', )}
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'Accept': 'application/json'}
    r = requests.post(url=grafana_url_post+'api/dashboards/db', files=files, headers=headers)
    print(r.url)
    print(" this is the response ")
    print(r.status_code)
    if r.status_code == "200":
        print("imported")
        print(r.content)
        print(r.json)
    else:
        print('error')
    return "Success"

import_dashboard()

'''
def get_upload_dashboard(dashboard, overwrite=False, message="Updated by grafanlib"):
    dashboard = import_dashboard.req
    print("dashboard_json_updated”,dashboard_json_updated")
    return json.dumps(
        {
            "dashboard_json": dashboard,
            "overwrite": overwrite,
            "message": message
        }, sort_keys=True, indent=2)
'''