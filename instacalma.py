import time
import random
from colorama import init, Fore, Style
import sys
import os

init(autoreset=True)

def clear_screen():
    # Windows ise cls, değilse clear komutu
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    print(Fore.GREEN + r"""
W       W   OOOOO   RRRRR   DDDD    EEEEE   X     X
W       W  O     O  R    R  D   D   E        X   X
W   W   W  O     O  RRRRR   D   D   EEEEE     X X
W W   W W  O     O  R   R   D   D   E        X   X
WW     WW   OOOOO   R    R  DDDD    EEEEE   X     X
""")
    print(Fore.RED + "@wordexchecker")
    print()
    print(Fore.RED + "1 Password Attack (İnstagram)")
    print(Fore.RED + "2 BlueForce (İnstagram)")
    print(Fore.RED + "3 MegaAttack (İnstagram)")
    print("Exit 00")
    print()
    print(Fore.YELLOW + "Seçim Yapınız...", end=" ")

def simulate_attack(username, mode_name):
    print(Fore.RED + f"\n{mode_name}")
    print(Fore.RED + "İnstagram Username: " + username)
    print(Fore.RED + "\nİşlem başlatılıyor...")
    for i in range(10):
        fake_logs = [
            "2FA kırılıyor...",
            "Proxy ağı başlatıldı...",
            "Bypass token alındı...",
            "Brute-force işlemi aktif...",
            "Instagram rate-limit aşıldı...",
            "Şifre denemesi yapılıyor...",
            "Hedef IP analiz ediliyor...",
            "Json response spoofing...",
            "Exploit tetiklendi...",
            "Yapay zeka saldırı dizisi oluşturuldu..."
        ]
        print(Fore.RED + f"[{i+1}/10] {random.choice(fake_logs)}")
        time.sleep(0.2)

    password_options = [
        f"{username}qq123_checker",
        f"{username}1234.deneme",
        f"12345678{username}checker.deneme"
    ]
    final_password = random.choice(password_options)
    print(Fore.GREEN + f"\n✅ Kullanıcı adı: {username}")
    print(Fore.GREEN + f"✅ Şifre bulundu: {final_password}")
    print()

def main():
    while True:
        clear_screen()
        print_logo()
        choice = input().strip()

        if choice == "1":
            clear_screen()
            username = input(Fore.RED + "\nİnstagram Username: ").strip()
            clear_screen()
            simulate_attack(username, "Password Attack")
        elif choice == "2":
            clear_screen()
            username = input(Fore.RED + "\nİnstagram Username: ").strip()
            clear_screen()
            simulate_attack(username, "BlueForce")
        elif choice == "3":
            clear_screen()
            username = input(Fore.RED + "\nİnstagram Username: ").strip()
            clear_screen()
            simulate_attack(username, "MegaAttack")
        elif choice == "00":
            print(Fore.YELLOW + "\nÇıkılıyor...")
            break
        else:
            print(Fore.RED + "Hatalı seçim! Lütfen tekrar deneyin.\n")

        input(Fore.YELLOW + "Devam etmek için Enter'a basın...")

    sys.exit(0)

if __name__ == "__main__":
    main()
