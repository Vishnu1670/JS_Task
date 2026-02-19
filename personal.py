import json

def get_details():
    user_detais = {
        "Personal info" : {
            "name": input("Enter the name: "),
            "age": int(input("Enter the age: ")),
            "number": int(input("Enter the number: "))
        },
        "local info" : {
            "street": input("Enter the street: "),
            "city" : input("Enter the city: "),
            "State" : input("Enter the state: "),
            "pincode": int(input("Enter the pincode: "))
        },
        "International info" : {
            "country": input("Enter the country: "),
            "State" : input("Enter the state: "),
            "pincode":int(input("Enter the pincode: "))
        }
        
    }
    get_info = json.dumps(user_detais)
    return get_info

def send_dict(get_info):
    user_dict = json.loads(get_info)
    return user_dict

ask_data = get_details()
print("JSON DATA :")
print(ask_data)
 
show_data = send_dict(ask_data)
print("\nDictionary Data:")
print(show_data)