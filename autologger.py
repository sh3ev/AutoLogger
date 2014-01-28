import sys, os, re

sys.path.append("./mechanize")

from mechanize import Browser


def log(url, num, ac, pas, msg, login, password):
        br = Browser()
        page = br.open(url)
	try:
		br.select_form(nr=num)
	except:
		print "\nThis form does not exist!"
		print "Please enter correct form number\n"
        br.form[ac] = login
        br.form[pas] = password
        response = br.submit()
        content = response.read()
        
        if content.find(msg) == -1:
                os.system('clear')
                print "Failed to login"
        else:
                os.system('clear')
                print "Logged in"


url = raw_input("Enter page adress: ")
num = int(raw_input("Enter form number: "))-1
ac = raw_input("Enter name of first form field: ")
pas = raw_input("Enter name of second form field: ")
msg = raw_input("Welcome message: ")
login = raw_input("Login: ")
password = raw_input("Password: ")

log(url, num, ac, pas, msg, login, password)
