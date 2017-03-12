# Import stuff
import tkinter, time, os

# GUI
class OpenPyProgram:
	
	# To be initiated right away
	def __init__(self):
	
		# Form a window with frames
		self.main_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		
		# Create buttons - assign text and task to button
		self.ssh_button = tkinter.Button(self.bottom_frame, text='SSH', command=self.openSSH)
		self.scp_button = tkinter.Button(self.bottom_frame, text='SCP', command=self.openSCP)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
		
		# Assign position
		self.ssh_button.pack(side='left')
		self.scp_button.pack(side='left')
		self.quit_button.pack(side='left')
		
		# Pack
		self.top_frame.pack()
		self.bottom_frame.pack()
		
		# Loop, to make window stay open
		tkinter.mainloop()

	# initiate SSH
	def openSSH(self):
		import SSH		# didn't fix the error - the program initiates on import, due to an error
	
	# initiate SCP
	def openSCP(self):
		import SCP		# didn't fix the error - the program initiates on import, due to an error

# run program
open = OpenPyProgram()