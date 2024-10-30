import sys

Bookmarks = {
"deezer": "https://www.deezer.com/en/",
"todoist": "https://app.todoist.com/app/today",
"putlockers": "https://putlockers.li/",
"twitter": "https://x.com/home",
"annas-archive": "https://annas-archive.org/",
"whatsapp": "https://web.whatsapp.com/",
"info-llg": "https://info-llg.fr/option-mp/?a=cours",
"youtube": "https://www.youtube.com/",
"instagram": "https://www.instagram.com/",
"github": "https://github.com/nobody48sheldor",
"google calendar": "https://calendar.google.com/calendar/u/0/r?pli=1",
"moodlecpge": "https://moodlecpge.stanislas.fr/login/index.php",
"gmail": "https://mail.google.com/mail/u/0/#inbox",
"cahier-de-prepa": "https://cahier-de-prepa.fr/mp1-janson/",
"chatgpt": "https://chatgpt.com/",
"Google Sheets": "https://docs.google.com/spreadsheets/u/0/",
"e-colle": "https://colles.janson-de-sailly.fr/eleve/action",
"desmos": "https://www.desmos.com/calculator",
}

args = sys.argv[1]

if args == "list":
	string = ""
	for i in Bookmarks.keys():
		string = string + "$ " + i + "\n"
	print(string)
else:
	if args in Bookmarks:
		print(Bookmarks[args])
