#! Python dictionary append

print ('#! Python dictionary append');

my_dict = {"Name": [], "Proffesion": [], "Age": []}

my_dict["Name"].append("Mahir Ahmed")
my_dict["Proffesion"].append("Developer")
my_dict["Age"].append(27)
print(my_dict)


## Delete python dicts
print('\n')
print ('## Delete python dicts with keys')
del my_dict['Proffesion']  # This will remove the element with your key.
print(my_dict)
