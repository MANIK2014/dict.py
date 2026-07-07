
test_dict = {"CodingaL": 3, "is": 2, "best": 2, "for": 2, "codingal": 1}

print("The dictionary is:", test_dict)


user_value = int(input("Enter the value you want to check the frequency of: "))


frequency = list(test_dict.values()).count(user_value)


print(f"The frequency of {user_value} in the dictionary is: {frequency}")


