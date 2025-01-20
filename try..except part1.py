class UserNotFound(Exception):
    pass
def fetch_user(user_id):
    #user = None
    user = users
    if user == None:
        raise UserNotFound(f'user {user_id} not in the database')
    else:
        #return user

        print(f'valid user {user_id}')


users = [123,456]
for user_id in users:
    try:
        fetch_user(user_id)
    except UserNotFound as e:
        print("There was an error:", e)
