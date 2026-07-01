import os

def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return db.execute(query)

def run_command(user_input):
    os.system("ping " + user_input)

API_KEY = "sk-live-51H8xJ2eZvKYlo2C0FAKEKEYFORTESTING"
