from enum import Enum

class Columns(Enum):
    COUNTRY = "country"
    CITY = "city"
    STATE = "state"

def get_columns_vals(columns: Columns, city_data):
    return_obj = []
    for data in city_data:
        match(columns):
            case Columns.COUNTRY:
                return_obj.append(data[Columns.COUNTRY.value])
            case Columns.CITY:
                return_obj.append(data[Columns.CITY.value])
            case Columns.STATE:
                return_obj.append(data[Columns.STATE.value])
    return return_obj

def main():
    city_data = [
        {"country": "Pakistan", "city": "Lahore", "state": "Punjab"},
        {"country": "Pakistan", "city": "Karachi", "state": "Sindh"},
        {"country": "Pakistan", "city": "Peshawar", "state": "KPK"},
        {"country": "Pakistan", "city": "Okara", "state": "Punjab"},
        {"country": "India", "city": "Delhi", "state": "Delhi"},
        {"country": "India", "city": "Mumbai", "state": "Maharashtra"},
        {"country": "India", "city": "Kolkata", "state": "West Bengal"},
        {"country": "USA", "city": "New York", "state": "New York"},
        {"country": "UK", "city": "Manchester", "state": "England"},
        {"country": "UK", "city": "London", "state": "England"}
    ]

    new_obj = get_columns_vals(Columns.COUNTRY, city_data)
    print(new_obj)

main()