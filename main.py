# isort:skip_file

#################################
# Website Blocker by DhitzBlock #
# Author : dhitznswa            #
#                               #
# Telegram : @dhitznswa         #
# Instagram : @dhitz.nswa       #
# TikTok : IDEsaya              #
#################################


import os
import sys
import time
import platform
import datetime
import http.client as httplib

try:
    import shellingham
    import requests
    from rich.console import Console
except ModuleNotFoundError:
    print("\nModule Tidak Ditemukan Plis Jalankan `pip install -r req.txt`.\n"); exit()

shell = shellingham.detect_shell()

os.system('mode con: cols=50 lines=25')

console = Console()

if platform.system() == "Windows": 
    if shell[0] != "cmd": console.print("[bold red]\nWARNING : Jalankan tools dengan Command Prompt / CMD agar tools berjalan dengan baik\n[/bold red]"); clear_terminal="clear";time.sleep(5);exit()
    else : clear_terminal = "cls"
    filepath_host = "C:\Windows\System32\drivers\etc\hosts"
else: filepath_host = "/etc/hosts"; clear_terminal = "clear"

isexit = False
tools_version = os.path.join("core", "version.txt")
default_hosts = os.path.join("core", "default-hosts.txt")
width_terminal, height_terminal = os.get_terminal_size()


class Dhitzblocker():
    def __init__(self):
        self._address = "127.0.0.1"
        self.now = datetime.date.today().strftime("%d/%m/%Y")
        try: self._sites = open("sites.txt", "r")
        except FileNotFoundError: self._sites = open("sites.txt", "w")
        if not os.path.isfile(filepath_host): console.print("[bold red]\n Maaf OS anda tidak didukung tools ini ![/bold red]"); exit()

        self._hosts = open(filepath_host, "a")

    def cnet(self):
        try: requests.get("https://www.google.com", timeout=5)
        except: return False

    def help(self):
        with console.status("[bold blue]\nMembuka dokumentasi bantuan[/bold blue]", spinner="point"):
            os.system("python -m webbrowser -t 'https://dhitznswa.github.io'")

    def block(self):
        sites = self._sites.readlines()
        self._hosts.write(f"\n\n# Website blocked on {self.now} by Dhitzblocker tools #\n")
        with console.status("[bold green]Sedang proses pemblokiran[/bold green]", spinner="point") as status:
            for site in sites:
                site = site.strip()
                if len(site) < 6: continue
                if "#" in site: continue
                self._hosts.write(f"{self._address} {site}\n")
                console.print("[green]BLOCKED[/green] > ", site)
                time.sleep(1)
            self._hosts.close()
            self._sites.close()
            console.print("\n\n[green bold]Sukses[/green bold] memblokir semua website!")

    def unblock(self):
        defhosts = open(default_hosts, "r")
        hosts = open(filepath_host, "w")
        with console.status("[bold green]\nSedang proses membuka semua website    [/bold green]", spinner="point"):
            hosts.truncate()    
            hosts.write(defhosts.read())
            hosts.close()
            defhosts.close()    
            time.sleep(10)
        console.print("\n[bold green]Sukses[/bold green] membuka semua website yang diblockir! \n")


def main():
    dblock = Dhitzblocker()
    version = open(tools_version, "r")
    with console.status("[bold blue]Melakukan pengecekan jaringan[/bold blue]", spinner="point"):
        if dblock.cnet() == False: console.print("[bold yellow]Komputer anda dalam keadaan offline, mohon hubungkan komputer dengan internet[/bold yellow]"); exit()
        time.sleep(2)
    while not isexit:
        os.system(clear_terminal)
        console.print("[bold green]+[/bold green]"*width_terminal)
        print("Selamat Datang".center(width_terminal, " "))
        console.print("[bold green]-[/bold green]"*width_terminal)
        print(f"Dhitzblocker Tools v{version.read()}".center(width_terminal, " "))
        console.print("[bold green]+[/bold green]"*width_terminal)
        console.print("[DB-001] Block Website ", style="italic")
        console.print("[DB-002] Unblock Semua Website ", style="italic")
        console.print("[DB-099] Keluar ", style="italic")
        console.print("[bold green]+[/bold green]"*width_terminal)
        pilihan = input("[?] Pilihan anda : DB-")
        console.print(f"\nPersiapan menjalankan kode perintah DB-{pilihan}...\n")
        time.sleep(3)
        if pilihan == "001":
            os.system(clear_terminal)
            dblock.block()
            time.sleep(5)
        elif pilihan == "002":
            os.system(clear_terminal)
            dblock.unblock()
            time.sleep(5)
        elif pilihan == "098":
            os.system(clear_terminal)
            dblock.help()
        elif pilihan == "099":
            os.system(clear_terminal)
            console.print(f"\nGoodbay, Terima Kasih...\n")
            exit()
        else:
            console.print(f"Tidak ada perintah dengan kode DB-{pilihan}\n")
            time.sleep(3)
        


if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt:
        isexit = True
        os.system(clear_terminal)
        console.print(f"\nGoodbay, Terima Kasih...\n", style="bold blue")