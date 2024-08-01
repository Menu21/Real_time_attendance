import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("attendance/Research/serviceaccountkey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendancerealtime-e2d62-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Janardan Prasad",
            "major": "Maths",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Abhishek singh",
            "major": "Economics",
            "starting_year": 2023,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Neha Singh",
            "major": "Physics",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "678945":
        {
            "name": "Menka Bharti",
            "major": "DataScience",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
