from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

fatiha = InlineKeyboardButton("Fotiha", callback_data="700")
baqara = InlineKeyboardButton("Baqara", callback_data="701")
oliimron = InlineKeyboardButton("Oli Imron", callback_data="702")
niso = InlineKeyboardButton("Niso", callback_data="703")
maida = InlineKeyboardButton("Maida", callback_data="704")
anam = InlineKeyboardButton("An'am", callback_data="705")
arof = InlineKeyboardButton("A'rof", callback_data="706")
anfal = InlineKeyboardButton("Anfal", callback_data="707")
tavba = InlineKeyboardButton("Tavba", callback_data="708")
yunus = InlineKeyboardButton("Yunus", callback_data="709")
hud = InlineKeyboardButton("Hud", callback_data="710")
yusuf = InlineKeyboardButton("Yusuf", callback_data="711")
rad = InlineKeyboardButton("Ra'd", callback_data="712")
ibrohim = InlineKeyboardButton("Ibrohim", callback_data="713")
hijr = InlineKeyboardButton("Hijr", callback_data="714")
nahl = InlineKeyboardButton("Nahl", callback_data="715")
isro = InlineKeyboardButton("Isro", callback_data="716")
kahf = InlineKeyboardButton("Kahf", callback_data="717")
maryam = InlineKeyboardButton("Maryam", callback_data="718")
toha = InlineKeyboardButton("Toha", callback_data="719")
anbiyo = InlineKeyboardButton("Anbiyo", callback_data="720")
haj = InlineKeyboardButton("Haj", callback_data="721")
muminun = InlineKeyboardButton("Mo'minun", callback_data="722")
nur = InlineKeyboardButton("Nur", callback_data="723")
furqon = InlineKeyboardButton("Furqon", callback_data="724")
shuaro = InlineKeyboardButton("Shuaro", callback_data="725")
naml = InlineKeyboardButton("Naml", callback_data="726")
qisos = InlineKeyboardButton("Qosos", callback_data="727")
ankabut = InlineKeyboardButton("Ankabut", callback_data="728")
rum = InlineKeyboardButton("Rum", callback_data="729")
luqman = InlineKeyboardButton("Luqmon", callback_data="730")
sajdah = InlineKeyboardButton("Sajda", callback_data="731")
ahzob = InlineKeyboardButton("Ahzob", callback_data="732")
saba = InlineKeyboardButton("Saba", callback_data="733")
fatir = InlineKeyboardButton("Fatir", callback_data="734")
yasin = InlineKeyboardButton("Yasin", callback_data="735")
soffat = InlineKeyboardButton("Soffat", callback_data="736")
sod = InlineKeyboardButton("Sod", callback_data="737")
zumaro = InlineKeyboardButton("Zumaro", callback_data="738")
gofir = InlineKeyboardButton("G'ofir", callback_data="739")
fussilat = InlineKeyboardButton("Fussilat", callback_data="740")
shuaro1 = InlineKeyboardButton("Shuaro", callback_data="741")
zuhuf = InlineKeyboardButton("Zuhuf", callback_data="742")
duhan = InlineKeyboardButton("Duhan", callback_data="743")
jasiya = InlineKeyboardButton("Jasiya", callback_data="744")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="745")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="746")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="747")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="748")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="748")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="749")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="750")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="751")
# ahqov = InlineKeyboardButton("Ahqov", callback_data="752")


mainmenu = InlineKeyboardButton("🔙 Bosh Menyu", callback_data="mainmenu")

quranKey = InlineKeyboardMarkup().add(fatiha, baqara, oliimron).add(niso, maida, anam).add(arof, anfal, tavba).add(yunus, hud, yusuf).add(rad, ibrohim, hijr).add(nahl, isro, kahf).add(maryam, toha, anbiyo).add(haj, muminun, nur).add(furqon, shuaro, naml).add(qisos, ankabut,rum).add(luqman, sajdah, ahzob).add(saba, fatir, yasin).add(soffat, sod, zumaro).add(gofir, fussilat, shuaro1).add(zuhuf, duhan, jasiya).add(mainmenu)