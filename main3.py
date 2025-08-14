file = open("email.txt", "r")
email = file.read().split("\n")
index = 0
for email in email:
    username = email.split("@")[index:][0]
    print(username)
