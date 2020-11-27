import tkinter as tk
from tkinter import messagebox
import mysql.connector

#koneksi database, ganti 'testing' menjadi nama database

try:
	mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='testing')
	myCursor = mydb.cursor()
except:
	tk.messagebox.showerror(title = 'Error', message = 'Database Tidak Ditemukan')

class MainApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Aplikasi Informasi Kesehatan")
		self._frame = None
		self.geometry("640x480")
		self.switchFrame(HomePage)

	def switchFrame(self,frameClass):
		newFrame = frameClass(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = newFrame
		self._frame.pack()

class HomePage(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')
		user_btn = tk.Button(self, text = "You are a User", bg = "#6BE964", font = ('verdana', 24), command = lambda: master.switchFrame(UserWindow))
		user_btn.pack(side = 'top', expand = 1, fill = tk.BOTH)

		admin_btn = tk.Button(self, text = "You are an Admin", bg = "#1E822A", font = ('verdana', 24), command = lambda: master.switchFrame(AdminLogin))
		admin_btn.pack(side = 'top', expand = 1, fill = tk.BOTH)

		quit_btn = tk.Button(self, text = "Quit", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.destroy())
		quit_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)		

class AdminLogin(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#1E822A')
		self.pack(side = 'top', expand = 1, fill = 'both')

		inName = tk.StringVar(master)
		inPw = tk.StringVar(master)

		l1 = tk.Label(self, text = "Username: ", bg = "#287624", font = ('verdana', 18))
		l1.pack(side = 'top', expand = 0, fill = tk.BOTH)
		e1 = tk.Entry(self, textvariable = inName)
		e1.pack(side = 'top')
		l2 = tk.Label(self, text = "Password: ", bg = "#287624", font = ('verdana', 18))
		l2.pack(side = 'top', expand = 0, fill = tk.BOTH)
		e2 = tk.Entry(self, textvariable = inPw)
		e2.pack(side = 'top')

		log_button = tk.Button(self, text = 'LOG IN', command = lambda: self.confirmAdmin(master,inName,inPw)) 
		log_button.pack()

		back_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		back_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

	def confirmAdmin(self,master,name,pw):
		username = name.get()
		password = pw.get()

		sql = "select password from admin where name = '"+username+"'"
		myCursor.execute(sql)
		res = myCursor.fetchone()
		
		if res is None:
			print('login failed, username do not exist')
			tk.messagebox.showerror(title = 'Error', message = 'Username do not exist')
			master.switchFrame(AdminLogin)
		else:
			for i in res:
				if(i == password):
					print('login successful')
					master.switchFrame(AdminWindow)
				else:
					print('login failed, wrong pasword')
					tk.messagebox.showerror(title = 'Error', message = 'Wrong password')
					master.switchFrame(AdminLogin)

class AdminWindow(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')
		addPost_btn = tk.Button(self, text = "Add New Post", bg = "#6BE964", font = ('verdana', 24), command = lambda: master.switchFrame(AddPost))
		addPost_btn.pack(side = 'top', expand = 1, fill = tk.BOTH)

		editPost_btn = tk.Button(self, text = "Edit Existing Post", bg = "#6BE964", font = ('verdana', 24), command = lambda: master.switchFrame(EditPost))
		editPost_btn.pack(side = 'top', expand = 1, fill = tk.BOTH)

		readFb_btn = tk.Button(self, text = "Read Feedback", bg = "#6BE964", font = ('verdana', 24), command = lambda: master.switchFrame(FeedbackWindow))
		readFb_btn.pack(side = 'top', expand = 1, fill = tk.BOTH)

		back_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		back_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

class FeedbackWindow(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')
		## TO DO SHOW FEEDBACK

		fb = tk.Text(self, height = 20, width = 60)

		fb.insert(tk.END, "FEEDBACK HERE\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ntest")
		fb.config(state = 'disabled')
		fb.pack()

		home_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		home_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

		back_btn = tk.Button(self, text = "Back to Admin Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(AdminWindow))
		back_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

class AddPost(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')

		injudul = tk.StringVar()
		intype = tk.StringVar()

		tk.Label(self, text = "Nama", bg = "#55f24b", font = ('verdana', 18)).pack()
		e1 = tk.Entry(self, textvariable = injudul, width = 40)
		e1.pack()
		tk.Label(self, text = "Tipe Informasi (1: Makanan, 2: Olahraga)", bg = "#55f24b", font = ('verdana', 18)).pack()
		e2 = tk.Entry(self, textvariable = intype, width = 20)
		e2.pack()
		tk.Label(self, text = "Deskripsi", bg = "#55f24b", font = ('verdana', 18)).pack()

		desc = tk.Text(self, height = 10, width = 60)
		desc.pack()

		submit_btn = tk.Button(self, text = "Submit Post", bg = "#75fa6e", font = ('verdana', 16), command = lambda: self.submitPost(injudul, desc, intype))
		submit_btn.pack()

		home_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		home_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

		back_btn = tk.Button(self, text = "Back to Admin Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(AdminWindow))
		back_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

	def submitPost(self, injudul, text, intype):
		judul = injudul.get()
		postType = int(intype.get())
		desc = text.get("1.0","end-1c")
		print(judul,desc,postType)
		## TO DO KIRIM FEEDBACK KE DATABASE

class EditPost(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')

		inkeyword = tk.StringVar()
		injudul = tk.StringVar()
		intype = tk.StringVar()

		l1 = tk.Label(self, text = "Judul Post", bg = "#55f24b", font = ('verdana', 18))
		l1.pack(side = 'top', expand = 0, fill = tk.BOTH)
		e1 = tk.Entry(self, textvariable = inkeyword, width = 40)
		e1.pack()

		l2 = tk.Label(self, text = "Judul Baru", bg = "#55f24b", font = ('verdana', 18))
		l2.pack(side = 'top', expand = 0, fill = tk.BOTH)
		e2 = tk.Entry(self, textvariable = inkeyword, width = 40)
		e2.pack()

		l3 = tk.Label(self, text = "Tipe Informasi (1: Makanan, 2: Olahraga)", bg = "#55f24b", font = ('verdana', 18))
		l3.pack(side = 'top', expand = 0, fill = tk.BOTH)
		e3 = tk.Entry(self, textvariable = intype, width = 20)
		e3.pack()

		l4 = tk.Label(self, text = "Deskripsi Baru", bg = "#55f24b", font = ('verdana', 18))
		l4.pack(side = 'top', expand = 0, fill = tk.BOTH)
		newdesc = tk.Text(self, height = 10, width = 60)
		newdesc.pack()

		log_button = tk.Button(self, text = 'Submit', command = self.editInfo())
		log_button.pack()

		home_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		home_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

		back_btn = tk.Button(self, text = "Back to Admin Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(AdminWindow))
		back_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

	def editInfo(self):
		return 0

class UserWindow(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')

		food_btn = tk.Button(self, text = "Food\nInformation", bg = "#6BE964", font = ('verdana', 24), command = lambda: master.switchFrame(FoodInfo))
		food_btn.pack(side = 'top', expand = 1, fill = tk.BOTH)

		sport_btn = tk.Button(self, text = "Sport\nInformation", bg = "#6BE964", font = ('verdana', 24), command = lambda: master.switchFrame(SportInfo))
		sport_btn.pack(side = 'top', expand = 1, fill = tk.BOTH)

		home_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		home_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

		fb_btn = tk.Button(self, text = "Give Feedback!", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(GiveFeedback))
		fb_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

class FoodInfo(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')

		inkeyword = tk.StringVar()
		desc = ""

		l1 = tk.Label(self, text = "Kata Kunci", bg = "#55f24b", font = ('verdana', 18))
		l1.pack(side = 'top', expand = 0, fill = tk.BOTH)
		e1 = tk.Entry(self, textvariable = inkeyword)
		e1.pack(side = 'top')

		log_button = tk.Button(self, text = 'Search', command = lambda: self.searchPost(inkeyword, desc_lbl)) 
		log_button.pack()

		desc_lbl = tk.Label(self, text = "Deskripsi: " + desc, bg = "#55f24b", font = ('verdana', 14), wraplength = 600)
		desc_lbl.pack()

		home_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		home_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

		back_btn = tk.Button(self, text = "Back to User Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(UserWindow))
		back_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

	def searchPost(self, kw, desc_lbl):
		keyword = kw.get()
		sql = "select isi from posting where type = 0 and judul='"+keyword+"'"
		myCursor.execute(sql)
		res = myCursor.fetchone()
		if res is None:
			tk.messagebox.showerror(title = 'Error', message = 'Post not found')
		else:
			for i in res:
				desc = i
			desc_lbl.config(text = "Deskripsi: " + desc)
			desc_lbl.pack()

class SportInfo(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')

		inkeyword = tk.StringVar()
		desc = ""

		l1 = tk.Label(self, text = "Kata Kunci", bg = "#55f24b", font = ('verdana', 18))
		l1.pack(side = 'top', expand = 0, fill = tk.BOTH)
		e1 = tk.Entry(self, textvariable = inkeyword)
		e1.pack(side = 'top')

		log_button = tk.Button(self, text = 'Search', command = lambda: self.searchPost(inkeyword, desc_lbl)) 
		log_button.pack()

		desc_lbl = tk.Label(self, text = "Deskripsi: " + desc, bg = "#55f24b", font = ('verdana', 14), wraplength = 600)
		desc_lbl.pack()

		home_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		home_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

		back_btn = tk.Button(self, text = "Back to User Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(UserWindow))
		back_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

	def searchPost(self, kw, desc_lbl):
		keyword = kw.get()
		sql = "select isi from posting where type = 1 and judul='"+keyword+"'"
		myCursor.execute(sql)
		res = myCursor.fetchone()
		if res is None:
			tk.messagebox.showerror(title = 'Error', message = 'Post not found')
		else:
			for i in res:
				desc = i
			desc_lbl.config(text = "Deskripsi: " + desc)
			desc_lbl.pack()

class GiveFeedback(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master, bg = '#6FFF80')
		self.pack(side = 'top', expand = 1, fill = 'both')

		injudul = tk.StringVar()
		tk.Label(self, text = "Judul", bg = "#55f24b", font = ('verdana', 18)).pack()
		e1 = tk.Entry(self, textvariable = injudul, width = 40)
		e1.pack(side = 'top')
		tk.Label(self, text = "Feedback", bg = "#55f24b", font = ('verdana', 18)).pack()

		fbtext = tk.Text(self, height = 10, width = 60)
		fbtext.pack()

		submit_btn = tk.Button(self, text = "Submit Feedback", bg = "#75fa6e", font = ('verdana', 16), command = lambda: self.submitFeedback(injudul, fbtext))
		submit_btn.pack()

		home_btn = tk.Button(self, text = "Back to Home Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(HomePage))
		home_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

		back_btn = tk.Button(self, text = "Back to User Page", bg = "#75fa6e", font = ('verdana', 16), command = lambda: master.switchFrame(UserWindow))
		back_btn.pack(side = 'bottom', expand = 0, fill = tk.BOTH)

	def submitFeedback(self, injudul, text):
		judul = injudul.get()
		fb_text = text.get("1.0","end-1c")
		print(judul,fb_text)
		## TO DO KIRIM FEEDBACK KE DATABASE

def main():
	checkDb = "mydb" in globals()
	if not checkDb:
		return 0
	app = MainApp()
	app.mainloop()

if __name__ == '__main__':
	main()