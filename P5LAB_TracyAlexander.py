# Define your function here.

if __name__ == '__main__':
    def days_in_feb(user_year):
        if user_year % 4 == 0 and (user_year % 100 != 0 or user_year % 400 == 0):
            print(f'{user_year} has 29 days in February.')
        else:
            print(f'{user_year} has 28 days in February.')

user_year = int(input())
days_in_feb(user_year)
user_year = int(input())
days_in_feb(user_year)