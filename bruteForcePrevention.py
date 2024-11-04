import time

correct_username = "prakhar"
correct_password = "abc123"

max_attempts = 3       
lockout_time = 30      

attempt_count = 0
is_locked = False
lockout_start = None

def check_login(username, password):
    global attempt_count, is_locked, lockout_start

    if is_locked:
        time_passed = time.time() - lockout_start
        if time_passed < lockout_time:
            remaining_time = lockout_time - int(time_passed)
            print(f"Account locked. Try again in {remaining_time} seconds.")
            return False
        else:
            
            is_locked = False
            attempt_count = 0
            print("Lockout period ended. You may try again.")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        attempt_count = 0  
        return True
    else:
        attempt_count += 1
        print(f"Login failed. Attempt {attempt_count} of {max_attempts}.")

        if attempt_count >= max_attempts:
            is_locked = True
            lockout_start = time.time()
            print(f"Account locked for {lockout_time} seconds due to too many failed attempts.")

        return False

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if check_login(username, password):
        break
