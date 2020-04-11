def toGreek(i, scale):
	if "m" in scale:
		if i == 1:
			return "i";
		elif i == 2:
			return "iidim";
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
			return "viidim";


scale = input("what scale is this song in? Ex: A or A# or Ab or Am or Abm or A#m: ");
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

f = open("output.txt", 'w');

contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(str(line))

for i in range(len(contents)):
	if contents[i].count(" ") > len(contents[i])/4 +1:
		contents[i] = contents[i].replace("m", " ");
		for j in scales[scale]:
			contents[i] = contents[i].replace(j, toGreek(scales[scale].index(j) + 1, scale))

	f.write(contents[i]);
	f.write("\n")

f.close()

exit(0);