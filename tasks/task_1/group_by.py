def group_by(group_by_key: str, city_data, col_to_add: list[str] = []):
    return_obj = {}
    for data in city_data:
        inner_obj = []
        obj = {}
        for key, val in data.items():
            if key != group_by_key:
                if col_to_add is None or len(col_to_add) == 0:
                    obj[key] = val
                elif key in col_to_add:
                    obj[key] = val
        inner_obj.append(obj)

        group_by_val = data[group_by_key]
        if return_obj.__contains__(group_by_val):
            return_obj[group_by_val].append(obj)
        else:
            return_obj[group_by_val] = []
            return_obj[group_by_val].append(obj)

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

    new_obj = group_by("country", city_data, ["city"])
    print(new_obj)

main()