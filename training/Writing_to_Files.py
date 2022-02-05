# w writing a append r read only r+ read/write
file = open("./data.csv", "w+")
file.write("user, email, phone\n")
file.write("Julie, jmilian@gmail.com, 2735839447\n")
file.write("Roger, Rroddrick@gmail.com, 3910236677\n")
file.close()
