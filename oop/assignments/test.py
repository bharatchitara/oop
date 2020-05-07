# # wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# #  
# # for i,j in wardrobe.items():
# #     for k in j:
# #         #for k in wardrobe.keys():
# #         print("{} {}".format(j,i))
# #              
# #             
# #          
# #         
#         
# # def email_list(domains):
# #     emails = []
# #     for dom,users in domains.items():
# #         for user in users:
# #             emails.append(user+"@"+dom)
# #     return(emails)
# # 
# # print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
# 
# 
# # 
# # def groups_per_user(group_dictionary):
# #     user_groups = {}
# #     for group, users in group_dictionary.items():
# #         for user in users:
# #             if user not in user_groups:
# #                 user_groups[user] = []
# #             user_groups[user].append(group)
# #     return user_groups
# # 
# # print(groups_per_user({"local": ["admin", "userA"],
# #         "public":  ["admin", "userB"],
# #         "administrator": ["admin"] }))
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# def add_prices(basket):
#     # Initialize the variable that will be used for the calculation
#     total = 0
#     # Iterate through the dictionary items
#     for item,price in  basket.items():
#         x= price
#         # Add each price to the total calculation
#         # Hint: how do you access the values of
#         # dictionary items?
#         total += price
#     # Limit the return value to 2 decimal places
#     return round(total, 2)  
# 
# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
#     "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
# 
# print(add_prices(groceries)) # Should print 28.44
# 
# 
# 
#         
#        
#         











# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
#  
# for i,j in wardrobe.items():
#     for k in j:
#         #for k in wardrobe.keys():
#         print("{} {}".format(j,i))
#              
#             
#          
#         
        
# def email_list(domains):
#     emails = []
#     for dom,users in domains.items():
#         for user in users:
#             emails.append(user+"@"+dom)
#     return(emails)
# 
# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# 
# def groups_per_user(group_dictionary):
#     user_groups = {}
#     for group, users in group_dictionary.items():
#         for user in users:
#             if user not in user_groups:
#                 user_groups[user] = []
#             user_groups[user].append(group)
#     return user_groups
# 
# print(groups_per_user({"local": ["admin", "userA"],
#         "public":  ["admin", "userB"],
#         "administrator": ["admin"] }))





# 
# def format_address(address_string):
#   # Declare variables
#     
#     house_no=''
#     street=''
#     lst= address_string.split(' ' )
#     #print(x)
#     
#     for i in lst:
#         if(i.isnumeric()):
#             house_no += str(i) 
#         else:
#             street+= str(i)
#             street+= str(" ")
#     
#   # Separate the address string into parts
# 
#   # Traverse through the address parts
#    # for __:
#     # Determine if the address part is the
#     # house number or part of the street name
# 
#   # Does anything else need to be done 
#   # before returning the result?
#   
#   # Return the formatted string  
#     return "house number {} on street named {}".format(house_no,street)
# 
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
# 
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
# 
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"


        
       
# def highlight_word(sentence, word):
#     if(word in sentence):
#         sentence=sentence.replace(word, word.upper())    
#     return sentence
#         
# 
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))
#         
        
        
         
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
    lst=[]
    lst= list2+list1[::-1]
    
    return lst
     
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
 
print(combine_lists(Jamies_list, Drews_list))
         





# def squares(start, end):
#     lst=[]
#     for i in range(start,end+1):
#         lst.append(i*i)
#     return (lst)
# 
# print(squares(2, 3)) # Should be [4, 9]
# print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# def car_listing(car_prices):
#     result = ""
#     for i,j in car_prices.items():
#         result += "{} costs {} dollars".format(i,j) + "\n"
#     return result
# 
# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

 
#  
# def combine_guests(guests1, guests2):
#   # Combine both dictionaries into one, with each key listed 
#   # only once, and the value from guests1 taking precedence
#     Taylors_guests.update(Rorys_guests)
#     Rorys_guests.update(Taylors_guests)
#     print(Rorys_guests)
#  
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
#  
# print(combine_guests(Rorys_guests, Taylors_guests))




# 
# def count_letters(text):
#     result = {}
#   # Go through each letter in the text
#     for letter in text:
#         
#         if(letter.isalpha()):
#             letter = letter.lower()
#             if(letter not in result):
#                 result[letter] = 1
#             else: 
#                 result[letter] += 1
#               
#     # Check if the letter needs to be counted or not
#     
#     # Add or increment the value in the dictionary
#     
#     return result
# 
# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}
# 
# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
# 
# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
