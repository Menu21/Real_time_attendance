from firebaseconfig.firebase_init import initialize_firebase

# Initialize Firebase and get the reference

ref = initialize_firebase()



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
