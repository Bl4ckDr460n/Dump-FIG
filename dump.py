import os,sys,time
try:
	import requests
except ImportError:
	input("\033[31m[-] module 'requests' belum di install\n\033[32m[=] Enter Untuk Menginstall ")
	os.system('pip install requests request')
try:
	from bs4 import BeautifulSoup as bs
except ImportError:
	input("\033[31m[-] module 'bs4' belum di install\n\033[32[=] Enter Untuk Menginstall ")
	os.system('pip install bs4')
banner = """\033[33m
    ____                           ________________
   / __ \__  ______ ___  ____     / ____/  _/ ____/
  / / / / / / / __ `__ \/ __ \   / /_   / // / __
 / /_/ / /_/ / / / / / / /_/ /  / __/ _/ // /_/ /
/_____/\__,_/_/ /_/ /_/ .___/  /_/   /___/\____/
                     /_/\033[32m
  [+] Codded By BL4CK DR460N \033[37mfeat SalisM3"""
def index():
	os.system('clear')
	print (banner)
	print ("")
	u = str(input("\033[37m[?] Username (ex:@Billal_Fzn) :\033[32m "))
	if not "@" in u:
		print ("\033[31m[-] Wajib Menggunakan \033[33m@\033[37musermame")
		sys.exit()
	else:
		usr = u.replace("@","")
		try:
			limit = int(input("\033[37m[?] Limit :\033[32m "))
		except ValueError:
			print ("\033[31m[?] Masukan Angka contoh 10")
			sys.exit()
		out = str(input("\033[37m[?] Output :\033[32m "))
		main(usr,limit,out)
		print ("\033[32m[!] DONE")

def main(usr,limit,out):
	oh = ""
	angka = 0
	global info
	try:
		requests.get("https://google.com")
	except requests.exceptions.ConnectionError:
		print ("\033[31m[-] Tidak Ada Koneksi :(")
		sys.exit()
	if not '.txt' in out:
		op = open(out+".txt","w")
		oh += out + ".txt"
	else:
		op = open(out,'w')
		oh += out
	penentu = 0
	url = "https://pitaname.com/"+usr+"/followers"
	print ("\033[32m[!] Mengecek Followers ..!")
	while penentu == 0:
		get = requests.get(url).text
		if not "Followers" in get:
			print ("\033[31m[-] Username Tidak Ditemukan")
			sys.exit()
		time.sleep(2)
		soup = bs(get,'html.parser')
		data = soup.find_all("a")
		for t in data:
			c = t.get("class")
			if str(c) == "['fullname']":
				info = t.get("href").replace('https://pitaname.com/', '')
				op.write(info+"\n")
				angka += 1
				print("\033[37m[\033[33m"+str(angka)+"\033[37m] \033[32m@"+info)
				if angka == limit:
					penentu += 1
					break
				time.sleep(0.0001)
		if "Load More ↓" in get:
			url = soup.find("a",id="loadmore").get("href")
		else:
			penentu += 1
if __name__ == '__main__':
	index()
