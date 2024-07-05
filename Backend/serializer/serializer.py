def convert_customer_details(customer):
    return {
        "id": str(customer["_id"]),
        "cust_id": customer["cust_id"],
        "first_name": customer["first_name"],
        "last_name": customer["last_name"],
        "email": customer["email"],
        "dob": customer["dob"],
        "gender": customer["gender"],
        "password": customer["password"],
        "address": customer["address"]
    }

def convert_all_customer_details(customers):
    return [convert_customer_details(customer) for customer in customers]
