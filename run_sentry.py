#!/usr/bin/env python3
import os
import sys
import json
import time
import hashlib
from blessed import Terminal

term = Terminal()

PROFILE_FILE = ".sentry_profile.json"
SECRET_SALT = "DevSecOps_Sentry_Salt_2026"

def calculate_hash(data_dict):
    payload = f"{data_dict['tier_1_unlocked']}{data_dict['tier_2_unlocked']}{data_dict['tier_3_unlocked']}{data_dict['tier_4_unlocked']}{SECRET_SALT}"
    return hashlib.sha256(payload.encode()).hexdigest()

def load_profile():
    default_profile = {
        "tier_1_unlocked": True,
        "tier_2_unlocked": False,
        "tier_3_unlocked": False,
        "tier_4_unlocked": False,
        "signature": ""
    }
    if not os.path.exists(PROFILE_FILE):
        default_profile["signature"] = calculate_hash(default_profile)
        with open(PROFILE_FILE, "w") as f:
            json.dump(default_profile, f, indent=4)
        return default_profile
    
    try:
        with open(PROFILE_FILE, "r") as f:
            user_data = json.load(f)
        saved_sig = user_data.get("signature", "")
        if saved_sig == calculate_hash(user_data):
            return user_data
        else:
            print(term.red("[!] CRITICAL: Profile integrity verification failed! Anti-cheat triggered."))
            print(term.yellow("[~] Resetting secure local environment variables to factory defaults..."))
            time.sleep(2)
            default_profile["signature"] = calculate_hash(default_profile)
            with open(PROFILE_FILE, "w") as f:
                json.dump(default_profile, f, indent=4)
            return default_profile
    except Exception:
        return default_profile

def render_banner():
    banner = """
    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 
              --- T H E   S E N T R Y   T R I A L S ---
    """
    print(term.clear() + term.green(banner))

def menu_loop():
    profile = load_profile()
    while True:
        render_banner()
        print(term.center(term.bold_cyan("== CHOOSE YOUR TRAINING CRUCIBLE ==")))
        print("\n")
        
        t1_status = term.green("[ UNLOCKED / ACTIVE ]") if profile["tier_1_unlocked"] else term.red("[ LOCKED ]")
        t2_status = term.green("[ UNLOCKED / ACTIVE ]") if profile["tier_2_unlocked"] else term.black_on_bright_black("[ ENCRYPTED - COMPLETE TIER 1 ]")
        t3_status = term.green("[ UNLOCKED / ACTIVE ]") if profile["tier_3_unlocked"] else term.black_on_bright_black("[ ENCRYPTED - COMPLETE TIER 2 ]")
        t4_status = term.green("[ UNLOCKED / ACTIVE ]") if profile["tier_4_unlocked"] else term.black_on_bright_black("[ ENCRYPTED - COMPLETE TIER 3 ]")
        
        print(f"\t[1] TIER 1: The Scavenger (File & System Navigation) -> {t1_status}")
        print(f"\t[2] TIER 2: The Data Filter (Text Processing & Pipes) -> {t2_status}")
        print(f"\t[3] TIER 3: The Sys-Admin (Process Control & Rights) -> {t3_status}")
        print(f"\t[4] TIER 4: The Shadow Operative (Networking & Hardening) -> {t4_status}")
        print("\n\t[E] Exit System Console\n")
        
        print(term.cyan("sentry_user@trials:~# "), end="")
        sys.stdout.flush()
        
        with term.cbreak():
            inp = term.inkey().upper()
            
        if inp == 'E':
            print("\n[+] Exiting terminal matrix cleanly. Stay secure.")
            break
        elif inp == '1':
            print("\n[+] Engaging Tier 1 Operations Protocol..."); time.sleep(1)
        elif inp == '2':
            if profile["tier_2_unlocked"]:
                print("\n[+] Engaging Tier 2 Log Analytics Protocol...")
            else:
                print("\n" + term.red("[!] ACCESS DENIED: Complete Tier 1 checkpoint with 80% accuracy first!")); time.sleep(1.5)
        elif inp == '3':
            if profile["tier_3_unlocked"]:
                print("\n[+] Engaging Tier 3 Hardening Systems Protocol...")
            else:
                print("\n" + term.red("[!] ACCESS DENIED: Complete Tier 2 checkpoint with 80% accuracy first!")); time.sleep(1.5)
        elif inp == '4':
            if profile["tier_4_unlocked"]:
                print("\n[+] Engaging Tier 4 Perimetric Network Protocol...")
            else:
                print("\n" + term.red("[!] ACCESS DENIED: Complete Tier 3 checkpoint with 80% accuracy first!")); time.sleep(1.5)

if __name__ == "__main__":
    menu_loop()
