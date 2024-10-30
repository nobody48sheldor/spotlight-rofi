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
