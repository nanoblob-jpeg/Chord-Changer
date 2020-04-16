import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
		self.quit.pack(side="bottom")

		self.translate = tk.Button(self)
		self.translate["text"] = "TRANSLATE\n(click me)"
		self.translate["command"] = self.translateIt
		self.translate.pack(side="bottom")

		self.leftSide = tk.Frame(self, height=30, bd=2, relief=tk.RAISED)
		self.leftSide.pack(side="left")

		self.leftSide.scale = tk.Label(self.leftSide, text="what scale is this song in? Ex: A or A# or Ab or Am or Abm or A#m: ")
		self.leftSide.scale.pack()

		self.leftSide.scaleT = tk.Text(self.leftSide, height=1, width=40)
		self.leftSide.scaleT.pack()

		self.leftSide.lab = tk.Label(self.leftSide, text="Untranslated Side")
		self.leftSide.lab.pack()

		self.leftSide.text1 = tk.Text(self.leftSide, height=25, width=40)
		self.leftSide.text1.pack();

		self.rightSide = tk.Frame(self, height=30, bd=2, relief=tk.RAISED)
		self.rightSide.pack(side="right")

		self.rightSide.lab = tk.Label(self.rightSide, text="", height=2)
		self.rightSide.lab.pack()

		self.rightSide.lab = tk.Label(self.rightSide, text="Translated Side")
		self.rightSide.lab.pack()

		self.rightSide.text2 = tk.Text(self.rightSide, height=25, width=40)
		self.rightSide.text2.pack()
		self.rightSide.text2.config(state="disabled")

	def toGreek(self, i, scale):
		if "m" in scale:
			if i == 1:
				return "i";
			elif i == 2:
				return "ii";
			elif i == 3:
				return "III";
			elif i == 4:
				return "iv";
			elif i == 5:
				return "v";
			elif i == 6:
				return "VI";
			elif i == 7:
				return "VII";
	
		else:
			if i == 1:
				return "I";
			elif i == 2:
				return "ii";
			elif i == 3:
				return "iii";
			elif i == 4:
				return "IV";
			elif i == 5:
				return "V";
			elif i == 6:
				return "vi";
			elif i == 7:
				return "vii";
	
	def translateIt(self):
		print("inside")
		scale = self.leftSide.scaleT.get("1.0","end-1c")
		letters = ["A", "B", "C", "D", "E", "F", "G"];
		scales = {
			"Ab" : ("Ab", "Bb", "C", "Db", "Eb", "F", "G"),
			"A" : ("A", "B", "C#", "D", "E", "F#", "G#"),
			"A#" : ("A#", "B#", "C##", "D#", "E#", "F##", "G##"),
			"Bb" : ("Bb", "C", "D", "Eb", "F", "G", "A"),
			"B" : ("B", "C#", "D#", "E", "F#", "G#", "A"),
			"B#" : ("B#", "C##", "D##", "E#", "F##", "G##", "A##"),
			"Cb" : ("Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"),
			"C" : ("C", "D", "E", "F", "G", "A", "B"),
			"C#" : ("C#", "D#", "E#", "F#", "G#", "A#","B#"),
			"Db" : ("Db", "Eb", "F", "Gb", "Ab", "Bb", "C"),
			"D" : ("D", "E", "F#", "G", "A", "Bm", "C#"),
			"D#" : ("D#", "E#", "F##", "G#", "A#", "B#", "C##"),
			"Eb" : ("Eb", "F", "G", "Ab", "Bb", "C", "D"),
			"E" : ("E", "F#", "G#", "A", "B", "C#", "D#"),
			"E#" : ("E#", "F##", "G##", "A#", "B#", "C##", "D##"),
			"Fb" : ("Fb", "Gb", "Ab", "Bbb", "Cb", "Db", "Eb"),
			"F" : ("F", "G", "A", "Bb", "C", "D", "E"),
			"F#" : ("F#", "G#", "A#", "B", "C#", "D#", "E#"),
			"Gb" : ("Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"),
			"G" : ("G", "A", "B", "C", "D", "E", "F#"),
			"G#" : ("G#", "A#", "B#", "C#", "D#", "E#", "F##"),
		
			"Abm" : ("Ab", "Bb", "Cb", "Db", "Eb", "Fb", "G"),
			"Am" : ("A", "B", "C", "Dm", "E", "F", "G#"),
			"A#m" : ("A#", "B#", "C#", "D#", "E#", "F#", "G##"),
			"Bbm" : ("Bb", "C", "Db", "Eb", "F", "Gb", "A"),
			"Bm" : ("B", "C#", "D", "E", "F#", "G", "A#"),
			"B#m" : ("B#", "C##", "D#", "E#", "F##", "G#", "A##"),
			"Cbm" : ("Cb", "Db", "Ebb", "Fb", "Gb", "Abb", "Bb"),
			"Cm" : ("C", "D", "Eb", "F", "G", "Ab", "B"),
			"C#m" : ("C#", "D#", "E", "F#", "G#", "A","B#"),
			"Dbm" : ("Db", "Eb", "Fb", "Gb", "Ab", "Bbb", "C"),
			"Dm" : ("D", "E", "F", "G", "A", "Bb", "C#"),
			"D#m" : ("D#", "E#", "F#", "G#", "A#", "B", "C##"),
			"Ebm" : ("Eb", "F", "Gb", "Ab", "Bb", "Cb", "D"),
			"Em" : ("E", "F#", "G", "A", "B", "C", "D#"),
			"E#m" : ("E#", "F##", "G#", "A#", "B#", "C#", "D##"),
			"Fbm" : ("Fb", "Gb", "Abb", "Bbb", "Cb", "Dbb", "Eb"),
			"Fm" : ("F", "G", "Ab", "Bb", "C", "Db", "E"),
			"F#m" : ("F#", "G#", "A", "B", "C#", "D", "E#"),
			"Gbm" : ("Gb", "Ab", "Bbb", "Cb", "Db", "Ebb", "F"),
			"Gm" : ("G", "A", "Bb", "C", "D", "Eb", "F#"),
			"G#m" : ("G#", "A#", "B", "C#", "D#", "E", "F##")
		}
		
		if(scale not in scales.keys()):
			print(scale, "not recognized");
			exit(1);
		
		print("test")
		contents =  self.leftSide.text1.get("1.0",'end').split('\n')
		
		for i in range(len(contents)):
			if contents[i].count(" ") > len(contents[i])/4 +1:
				contents[i] = contents[i].replace("m", " ");
				for j in scales[scale]:
					contents[i] = contents[i].replace(j, self.toGreek(scales[scale].index(j) + 1, scale))
		
			self.rightSide.text2.config(state="normal")
			self.rightSide.text2.insert(tk.INSERT, contents[i])
			self.rightSide.text2.insert(tk.INSERT,"\n")

root = tk.Tk()
app = Application(master=root)
app.master.title("Chord Changer")
app.mainloop()

exit(0);