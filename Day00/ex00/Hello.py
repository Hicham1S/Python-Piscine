ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# modify ft_list
word = "World!"
ft_list.remove("tata!")
ft_list.append(word)

# modify ft_tuple
ft_tuple = (ft_tuple[0], "Lebanon!")

# modify ft_set
city = "Beirut!"
ft_set.remove("tutu!")
ft_set.add(city)

# modify ft_dic
campus = "42Beirut!"
ft_dict["Hello"] = campus

# printing
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
