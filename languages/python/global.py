# Bad code - uses global data

class User():
    def __init__(self, username = "guest", is_admin = False):
        self.username = username
        self.is_admin = is_admin 
    def greet(self,username):
        self.username = username
        print(f"Hello, {self.username}!")


    def check_access(self, is_admin =False):
        self.is_admin = is_admin 
        if self.is_admin:
            print("Access granted")
        else:
            print("Access denied")

# Usage
user=User()
user.greet('daniel')

# ============================================
# YOUR TASK: Rewrite the functions below
# so they don't use any global variables
# ============================================

# def greet(???):
#     pass

# def check_access(???):
#     pass


# ============================================
# BONUS: Create a User class and refactor
# the functions to accept a User object
# ============================================

# class User:
#10     pass
