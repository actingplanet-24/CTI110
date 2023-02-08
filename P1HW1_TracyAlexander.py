user_num = int(input('Enter integer:\n'))

print("You entered:", user_num)

user_num_sq = user_num * user_num
user_num_cu = user_num * user_num * user_num

print(user_num, "squared is", user_num_sq)
print("And", user_num, "cubed is", user_num_cu, "!!")

print("Enter another integer:")
user_num2 = int(input())

user2_add = user_num + user_num2
user2_multi = user_num * user_num2

print(user_num, "+", user_num2, "is", user2_add)
print(user_num, "*", user_num2, "is", user2_multi)