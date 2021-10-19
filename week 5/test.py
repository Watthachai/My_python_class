class user:
    def __init__(self,user_id,user_name,user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.rank = 'Admin'

user_1 = user('01','Jackson','1234')
print('-'*10)
print(f"User ID : {user_1.user_id}")
print(user_1.user_name)
print(user_1.user_password)
print(user_1.rank)
print('-'*10)