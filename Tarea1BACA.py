from datetime import datetime

def compareStrings (a,b):
	try:
		f = open("log.txt", "a")
		now = datetime.now()
		current_time = now.strftime("%d/%m/%Y - %H:%M:%S ")
		if (len(b) > len(a)):
			f.write(current_time + a + ", " + b + ", " + b + "\n") 
			return b
		else:
			f.write(current_time + a + ", " + b + ", " + a + "\n")
			return a
	except:
		print("Hubo un error, inténtelo de nuevo")
		f.write(current_time + a + ", " + b + ", error\n")
		return

