import requests

url = "http://localhost:5000/predict_live"
r = requests.post(url, json=[[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]])
assert r.status_code == 200
print(r.json())