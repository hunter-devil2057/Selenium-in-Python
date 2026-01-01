my_dic = {'id': 'e156', 'name': 'Allen', 'age': 34, 'salary': 15000}

print(my_dic.keys())
print(my_dic.values())
data = my_dic.items()
for item in data:
    print(item)

my_dic.pop("id")
print(my_dic.get("age"))