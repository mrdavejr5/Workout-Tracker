import datetime
import requests
import os

NUTRITION_ENDPOINT = str(os.environ["NUTRITION_ENDPOINT"])
SHEETY_ENDPOINT = str(os.environ["SHEETY_ENDPOINT"])
X_APP_ID= str(os.environ["X_APP_ID"])
X_APP_KEY= str(os.environ["X_APP_KEY"])
SHEETY_AUTH= str(os.environ["SHEETY_AUTH"])

header = {
"x-app-id":X_APP_ID,
"x-app-key":X_APP_KEY,
"x-remote-user-id": "0",
}
sheety_header = {
     "Content-Type": "application/json",
     "Authorization": SHEETY_AUTH,
}
print("What workout did you do today?")
workout_response = input()

exercise_params ={
     "query": workout_response,
     "gender":"male",
     "weight_kg":79.3,
     "height_cm":180.0,
     "age":27,
}


response = requests.post(NUTRITION_ENDPOINT, json= exercise_params, headers= header)
print(response)
exercises = response.json()["exercises"][0]

workout = {
     "workout":{
          "date": datetime.datetime.now().strftime("%x"),
          "time": datetime.datetime.now().strftime("%X"),
          "exercise":exercises["name"].title(),
          "duration": exercises["duration_min"],
          "calories": exercises["nf_calories"],
     }
}

sheet_response = requests.post(SHEETY_ENDPOINT, json= workout, headers=sheety_header)


