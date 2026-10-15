import requests
body = {
    "age": 94,
    "sex": 1,
    "cp": 4,
    "trestbps": 100,
    "chol": 255,
    "fbs": 0,
    "restecg": 0,
    "thalach": 98,
    "exang": 1,
    "oldpeak": 1.8,
    "slope": 1,
    "ca": 2,
    "thal": 2
    }
#response = requests.post(url = 'http://127.0.0.1:8000/score', json = body)
response = requests.post(url = 'https://fastapi-ml-latest-s3gs.onrender.com/score', json = body)
print (response.json())

# ffoutput: {'score': 0.866490130600765}
