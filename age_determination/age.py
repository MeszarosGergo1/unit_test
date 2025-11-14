def categorise_byage(age):
    if 0 < age <=9:
        return "child"
    elif 10 <= age <= 18:
        return "teenager"
    elif 18 < age <= 64:
        return "adult"
    elif 65 <= age <= 120:
        return "golden age"
    else:
        return f"invalid age: {age}"