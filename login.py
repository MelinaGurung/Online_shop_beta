def register():
    db = open("login_credentials.txt", "r")
    username = input("Create username:")
    password = input("Create password:")
    password1 = input("Re-enter password:")
    x = []
    y = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        x.append(a)
        y.append(b)
    data = dict(zip(x,y))
    db.close()

    if password != password1:
        print("Passwords don't match. Restart.")
        register()
    else:
        if username in x:
            print("Username unavailable")
            register()
        elif len(password) < 5:
            print("Password too short. Restart.")
            register()
        else:
            db = open("login_credentials.txt", "a")
            db.write(username + "," + password + "\n")
            print("Successful registration!")


def access():
    db = open("login_credentials.txt", "r")
    username = input("Enter username:")
    password = input("Enter password:")

    if not len(username or password)<1:
        x = []
        y = []
        for i in db:
            a,b = i.split(",")
            b= b.strip()
            x.append(a)
            y.append(b)
        data = dict(zip(x,y))

        if username not in data:
            print("Username doesn't exist")
        else:
            if data[username]:
                if password == data[username]:
                    print("Login Successful.")
                    print("Welcome, " + username)
                else:
                    print("Password is incorrect.")
                    access()


def home(option=None):
    option = input("Login or Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Invalid command. Back to home")
        home()

home()