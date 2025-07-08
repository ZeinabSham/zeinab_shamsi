patients = [
    {
        'name': 'Alice',
        'age': 30,
        'weight': 60,
        'dosages': [
            {'time': '08:00', 'dose': 10},
            {'time': '12:00', 'dose': 40}
        ]
    },
    {
        'name': 'Bob',
        'age': 16,
        'weight': 40,
        'dosages': [
            {'time': '08:00', 'dose': 5},
            {'time': '12:00', 'dose': -5}
        ]
    }
]

for patient in patients:
    age = patient['age']
    weight = patient['weight']
    name = patient['name']
    
    for dose in patient['dosages']:
        dose_value = dose['dose']
        time = dose['time']
        
        target = dose_value / weight

        print(f"{name} at {time} => dose per kg: {target}")

        if target <= 0:
            print("invalid number of dosage")
        elif age >= 18:
            if 0.1 <= target <= 0.5:
                print("within range")
            else:
                print("outside range")
        else:
            if 0.05 <= target <= 0.3:
                print("within range")
            else:
                print("outside range")
