student = [
    {"name": "a", "id": "1", "age": 2},
    {"name": "b", "id": "10", "age": 3},
    {"name": "c", "id": "100", "age": 4}
]

def check_age(age):
    return age > 20

def get_data(ds, index, key):
    return ds[index][key]

print(get_data(student, 2, "name"))

print(type(student))