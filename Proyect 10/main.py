import requests
import datetime

APP_ID = "ec6412ab"
API_KEY = "0507b8d811d68258b3e7beb75855acae"
EXERSICE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT_KG = 110
HEIGHT_CM = 183
AGE = 19

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

activity = input("What exercise did you do? ")
a = {
    "query": activity,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
data = requests.post(url=EXERSICE_END_POINT, headers=headers, json=a)
for i in range(0, len(data.json()['exercises'])):
    exercise_name = data.json()['exercises'][i]["name"]
    duration = data.json()['exercises'][i]['duration_min']
    calories = data.json()['exercises'][i]['nf_calories']
    workout = {
        "workout":
            {
                "date": datetime.datetime.now().strftime("%Y/%d/%m"),
                "time": datetime.datetime.now().strftime("%H:%M:%S"),
                "exercise": exercise_name.title(),
                "duration": duration,
                "calories": calories,
            }
    }
    print(workout)