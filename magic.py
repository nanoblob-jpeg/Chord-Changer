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
	"Ab" : ("Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gm"),
	"A" : ("A", "Bm", "C#m", "D", "E", "F#m", "G#m"),
	"A#" : ("A#", "B#m", "C##m", "D#", "E#", "F##m", "G##m"),
	"Bb" : ("Bb", "Cm", "Dm", "Eb", "F", "Gm", "Am"),
	"B" : ("B", "C#m", "D#m", "E", "F#", "G#m", "Am"),
	"B#" : ("B#", "C##m", "D##m", "E#", "F##", "G##m", "A##m"),
	"Cb" : ("Cb", "Dbm", "Ebm", "Fb", "Gb", "Abm", "Bbm"),
	"C" : ("C", "Dm", "Em", "F", "G", "Am", "Bm"),
	"C#" : ("C#", "D#m", "E#m", "F#", "G#", "A#m","B#m"),
	"Db" : ("Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cm"),
	"D" : ("D", "Em", "F#m", "G", "A", "Bm", "C#m"),
	"D#" : ("D#", "E#m", "F##m", "G#", "A#", "B#m", "C##m"),
	"Eb" : ("Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Dm"),
	"E" : ("E", "F#m", "G#m", "A", "B", "C#m", "D#m"),
	"E#" : ("E#", "F##m", "G##m", "A#", "B#", "C##m", "D##m"),
	"Fb" : ("Fb", "Gbm", "Abm", "Bbb", "Cb", "Dbm", "Ebm"),
	"F" : ("F", "Gm", "Am", "Bb", "C", "Dm", "Em"),
	"F#" : ("F#", "G#m", "A#m", "B", "C#", "D#m", "E#m"),
	"Gb" : ("Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "Fm"),
	"G" : ("G", "Am", "Bm", "C", "D", "Em", "F#m"),
	"G#" : ("G#", "A#m", "B#m", "C#", "D#", "E#m", "F##m"),

	"Abm" : ("Abm", "Bbm", "Cb", "Dbm", "Eb", "Fb", "G"),
	"Am" : ("Am", "Bm", "C", "Dm", "E", "F", "G#"),
	"A#m" : ("A#m", "B#m", "C#", "D#m", "E#", "F#", "G##"),
	"Bbm" : ("Bbm", "Cm", "Db", "Ebm", "F", "Gb", "A"),
	"Bm" : ("Bm", "C#m", "D", "Em", "F#", "G", "A#"),
	"B#m" : ("B#m", "C##m", "D#", "E#m", "F##", "G#", "A##"),
	"Cbm" : ("Cbm", "Dbm", "Ebb", "Fbm", "Gb", "Abb", "Bb"),
	"Cm" : ("Cm", "Dm", "Eb", "Fm", "G", "Ab", "B"),
	"C#m" : ("C#m", "D#m", "E", "F#m", "G#", "A","B#"),
	"Dbm" : ("Dbm", "Ebm", "Fb", "Gbm", "Ab", "Bbb", "C"),
	"Dm" : ("Dm", "Em", "F", "Gm", "A", "Bb", "C#"),
	"D#m" : ("D#m", "E#m", "F#", "G#m", "A#", "B", "C##"),
	"Ebm" : ("Ebm", "Fm", "Gb", "Abm", "Bb", "Cb", "D"),
	"Em" : ("Em", "F#m", "G", "Am", "B", "C", "D#"),
	"E#m" : ("E#m", "F##m", "G#", "A#m", "B#", "C#", "D##"),
	"Fbm" : ("Fbm", "Gbm", "Abb", "Bbbm", "Cb", "Dbb", "Eb"),
	"Fm" : ("Fm", "Gm", "Ab", "Bbm", "C", "Db", "E"),
	"F#m" : ("F#m", "G#m", "A", "Bm", "C#", "D", "E#"),
	"Gbm" : ("Gbm", "Abm", "Bbb", "Cbm", "Db", "Ebb", "F"),
	"Gm" : ("Gm", "Am", "Bb", "Cm", "D", "Eb", "F#"),
	"G#m" : ("G#m", "A#m", "B", "C#m", "D#", "E", "F##")
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
	if contents[i].count(" ") > len(contents[i])/3 +1:
		for j in scales[scale]:
			contents[i] = contents[i].replace(j, toGreek(scales[scale].index(j) + 1, scale))
	f.write(contents[i]);
	f.write("\n")

f.close()

exit(0);