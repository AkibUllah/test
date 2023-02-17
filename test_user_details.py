import requests

def test_for_post_method():
    data = {
                "address": "wewe",
                "ageInYears": 12,
                "creditScore": 12.33,
                "firstName": "test1",
                "secondName": "str"
            }
    url = 'http://127.0.0.1:5000/user_details'

    response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
    assert response

def test_for_get_method():
    url = 'http://127.0.0.1:5000/user_details'

    response = requests.get(url, headers={'Content-Type': 'application/json'})
    assert response