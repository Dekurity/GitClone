import os
import subprocess
import termcolor
import pyfiglet
import requests
import threading
import pygame

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("whoa.mp3")  
    pygame.mixer.music.play(-1)

def print_banner():
    cyan = "\033[38;5;51m"
    reset = "\033[0m"
    print("\n")
    banner = pyfiglet.figlet_format("GitClone")
    print(f"{cyan}{banner}{reset}")
    print("\n")
    print(f"{cyan}  [*] GitClone\n{reset}")
    print(f"{cyan}  [*] Developer: Dekurity\n{reset}")
    print(f"{cyan}  [*] Source Code Bebas Rename/Recode\n{reset}")
    print("\n")

def get_github_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        followers = data.get("followers", 0)
        following = data.get("following", 0)
        public_repos = data.get("public_repos", 0)
        repos_url = data.get("repos_url", "")
        
        print(termcolor.colored(f"\n[👥] Followers: {followers} | Following: {following} | Total Repos: {public_repos}", "cyan"))
        
        repos_response = requests.get(repos_url)
        if repos_response.status_code == 200:
            repos_data = repos_response.json()
            repo_names = [repo["name"] for repo in repos_data]
            print(termcolor.colored("\n[📚] Daftar Repository:", "magenta"))
            for i, repo in enumerate(repo_names, start=1):
                print(termcolor.colored(f" {i}. {repo}", "yellow"))
            return repo_names
    else:
        print(termcolor.colored("[❌] Username ini tidak tersedia di GitHub!", "red"))
        return None

def run_command(command):
    try:
        print(termcolor.colored(f"🔍 Menjalankan perintah: {' '.join(command)}", "yellow"))
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        if result.stdout:
            print(termcolor.colored(result.stdout, "green"))
        if result.stderr:
            print(termcolor.colored(result.stderr, "red"))
    except subprocess.CalledProcessError as e:
        print(termcolor.colored(f"❌ Error: {e}", "red"))
        if e.stdout:
            print(termcolor.colored(e.stdout, "green"))
        if e.stderr:
            print(termcolor.colored(e.stderr, "red"))

def clone_repo(username, repo_name):
    repo_url = f"https://github.com/{username}/{repo_name}.git"
    
    if os.path.exists(repo_name):
        print(termcolor.colored("[ℹ️] Repository sudah ada di sistem Anda!", "yellow"))
        return
    
    print(termcolor.colored(f"[🔄] Mengkloning repository dari {repo_url}...", "green"))
    run_command(["git", "clone", repo_url])

def clone_and_install():
    print_banner()
    pink = "\033[38;5;205m"
    reset = "\033[0m"
    
    username = input(f"{pink}[💛] Masukkan username GitHub: {reset}").strip()
    repo_list = get_github_info(username)
    
    if not repo_list:
        return
    
    repo_name = input(f"{pink}[📂] Masukkan nama repository dari daftar di atas: {reset}").strip()
    
    if repo_name not in repo_list:
        print(termcolor.colored("[❌] Nama repository tidak valid!", "red"))
        return
    
    clone_thread = threading.Thread(target=clone_repo, args=(username, repo_name))
    clone_thread.start()
    clone_thread.join()
    
    print(termcolor.colored("[🙏] Terima kasih telah menggunakan GitClone! 😊", "cyan"))

if __name__ == "__main__":
    play_music()
    clone_and_install()
