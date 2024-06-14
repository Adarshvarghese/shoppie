def convert_customer_details(customer)-> dict:
    return {
 "id":str(customer["_id"]),
 "cust_id":(customer["cust_id"]),
"name":customer["name"],
"email":customer["email"],
"dob":customer["dob"],
"gender":customer["gender"],
"password":customer["password"],
"address":customer["address"]
    }

def convert_all_customer_details(customers)-> dict:
    return [convert_customer_details(customer) for customer in customers]