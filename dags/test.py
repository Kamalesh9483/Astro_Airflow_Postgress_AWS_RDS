dictvar={
    "results": [
        {
            "gender": "male",
            "name": {
                "title": "Monsieur",
                "first": "Dan",
                "last": "Leroy"
            },
            "location": {
                "street": {
                    "number": 1998,
                    "name": "Rue Gasparin"
                },
                "city": "Dürrenroth",
                "state": "Zug",
                "country": "Switzerland",
                "postcode": 6008,
                "coordinates": {
                    "latitude": "-57.4017",
                    "longitude": "-104.8645"
                },
                "timezone": {
                    "offset": "-10:00",
                    "description": "Hawaii"
                }
            },
            "email": "dan.leroy@example.com",
            "login": {
                "uuid": "2913e3f8-aa5b-4a96-b9a1-09768676b9ec",
                "username": "redbird134",
                "password": "maurice",
                "salt": "OOwUPMyQ",
                "md5": "40fb9231fce624e2a84318110cfc847e",
                "sha1": "6f0b5c67cc968698e5b7311e84009175bdfbc3ad",
                "sha256": "e169841eef3ab49902fdad6336640ff29777226791563149852c2ad2bca6c1c8"
            },
            "dob": {
                "date": "1978-05-27T18:40:08.906Z",
                "age": 46
            },
            "registered": {
                "date": "2011-08-08T06:24:43.042Z",
                "age": 13
            },
            "phone": "077 447 69 77",
            "cell": "075 847 96 25",
            "id": {
                "name": "AVS",
                "value": "756.2764.8824.04"
            },
            "picture": {
                "large": "https://randomuser.me/api/portraits/men/39.jpg",
                "medium": "https://randomuser.me/api/portraits/med/men/39.jpg",
                "thumbnail": "https://randomuser.me/api/portraits/thumb/men/39.jpg"
            },
            "nat": "CH"
        }
    ],
    "info": {
        "seed": "04aeb2117a63fff7",
        "results": 1,
        "page": 1,
        "version": "1.4"
    }
}

# Extracting required information
first_name = dictvar['results'][0]['name']['first']
last_name = dictvar['results'][0]['name']['last']
city = dictvar['results'][0]['location']['city']
age = dictvar['results'][0]['dob']['age']

# Print the extracted values
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"City: {city}")
print(f"Age: {age}")