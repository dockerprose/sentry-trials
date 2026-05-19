#!/usr/bin/env python3
import os
import sys
import json
import time
import hashlib
import random
from blessed import Terminal

term = Terminal()

PROFILE_FILE = ".sentry_profile.json"
SECRET_SALT = "DevSecOps_Sentry_Salt_2026"

def calculate_hash(data_dict):
    payload = f"{data_dict['tier_1_unlocked']}{data_dict['tier_2_unlocked']}{data_dict['tier_3_unlocked']}{data_dict['tier_4_unlocked']}{SECRET_SALT}"
    return hashlib.sha256(payload.encode()).hexdigest()

def load_profile():
    default_profile = {"tier_1_unlocked": True, "tier_2_unlocked": False, "tier_3_unlocked": False, "tier_4_unlocked": False, "signature": ""}
    if not os.path.exists(PROFILE_FILE):
        default_profile["signature"] = calculate_hash(default_profile)
        with open(PROFILE_FILE, "w") as f: json.dump(default_profile, f, indent=4)
        return default_profile
    try:
        with open(PROFILE_FILE, "r") as f: user_data = json.load(f)
        if user_data.get("signature", "") == calculate_hash(user_data): return user_data
        default_profile["signature"] = calculate_hash(default_profile)
        return default_profile
    except Exception: return default_profile

def save_profile(profile):
    profile["signature"] = calculate_hash(profile)
    with open(PROFILE_FILE, "w") as f: json.dump(profile, f, indent=4)

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

def execute_tier_session(tier_name, module_path, profile):
    try:
        sys.path.append(os.getcwd())
        mod = __import__(f"modules.{module_path}", fromlist=["QUESTIONS"])
        all_questions = mod.QUESTIONS
    except Exception as e:
        print(term.red(f"\n[-] Failed to load question asset bank: {e}"))
        time.sleep(2)
        return False

    sample_size = min(len(all_questions), 15)
    session_questions = random.sample(all_questions, sample_size)
    
    correct_counter = 0
    total_accumulated_points = 0

    for index, q in enumerate(session_questions):
        q_limit = 60.0
        q_start = time.time()
        user_ans = ""
        timed_out = False
        last_refresh_sec = -1

        print(term.clear() + term.home, end="")

        while True:
            elapsed = time.time() - q_start
            time_remaining = q_limit - elapsed

            if time_remaining <= 0:
                timed_out = True
                break

            current_sec = int(time_remaining)

            if current_sec != last_refresh_sec:
                last_refresh_sec = current_sec
                print(term.home, end="")
                
                print(term.green("\n    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗\n    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║\n    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║\n    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║\n    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝\n    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ \n              --- T H E   S E N T R Y   T R I A L S ---"))
                print(term.cyan(f"\n TIER: {tier_name.upper()} | CHECKPOINT {index+1} of {sample_size}"))
                
                timer_color = term.bold_bright_red if time_remaining <= 10.0 else term.bold_yellow
                print(timer_color(f" ⌛ TIME REMAINING: [ {current_sec}s ] ") + term.magenta(f"       TOTAL SCORE: [ {total_accumulated_points} pts ]"))
                print("=" * 60 + "\n")
                print(term.bold("[!] MISSION SCENARIO:\n") + f"    {q['scenario']}\n")
                print(term.clear_eos)
                print(term.bold("[?] CHALLENGE:\n") + f"    {q['question']}\n")

                if q["type"] == "MCQ":
                    for opt in q["options"]: print(f"    {opt}")
                    print("\n" + term.cyan(f"sentry_user@trials:~$ Selection (A-D) [Current: {user_ans}]: "), end="")
                    sys.stdout.flush()
                else:
                    print(term.dim("    (Type exact terminal syntax, then press ENTER to submit)"))
                    print("\n" + term.cyan("sentry_user@trials:~$ ") + term.bright_white(user_ans), end="")
                    sys.stdout.flush()

            with term.cbreak():
                val = term.inkey(timeout=0.05)
                if val:
                    if q["type"] == "MCQ":
                        val_up = val.upper()
                        if val_up in ['A', 'B', 'C', 'D']:
                            user_ans = val_up
                            last_refresh_sec = -1
                        elif val.name == "KEY_ENTER" or val == '\n':
                            if user_ans != "": break
                    else:
                        if val.name == "KEY_ENTER" or val == '\n':
                            if user_ans.strip() != "": break
                        elif val.name == "KEY_BACKSPACE" or val == '\b' or ord(val) == 127:
                            user_ans = user_ans[:-1]
                            last_refresh_sec = -1
                        elif not val.is_sequence:
                            user_ans += val
                            last_refresh_sec = -1

        # --- Grading & Speed Bonus Evaluator ---
        print("\n" + "=" * 60)
        if timed_out:
            print(term.bold_red(">> [X] TERMINATED: Operational timeout window expired! (0 pts)"))
        elif user_ans.strip() == q["correct"]:
            if time_remaining >= 45.0: bonus, rating, color = 50, "SHADOW VELOCITY [BLITZ]", term.bold_bright_green
            elif time_remaining >= 30.0: bonus, rating, color = 25, "RAPID TACTICAL EXECUTION", term.bright_green
            else: bonus, rating, color = 0, "STANDARD SYS-ADMIN PACE", term.cyan
            
            question_score = 100 + bonus
            correct_counter += 1
            total_accumulated_points += question_score
            print(term.bold_green(f">> [✓] ACCESS GRANTED: Instruction syntax verified!"))
            print(f">> SPEED CLASS: {color(rating)} ({elapsed:.2f}s elapsed)")
            print(f">> MATRIX SCORE: +100 Base + {bonus} Speed Bonus = " + term.bold_bright_green(f"{question_score} pts"))
        else:
            print(term.bold_red(">> [X] INTERCEPTED: Malformed configuration parameters!"))
            print(term.yellow(f">> REQUIRED STRING: {q['correct']}"))
            print(f">> MATRIX SCORE: " + term.bold_red("0 pts"))

        print(term.dim(f"\nSENTRY INSIGHT: {q.get('insight', 'No breakdown profile provided.')}"))
        print("\n" + term.yellow("Press [SPACEBAR] to advance..."))
        with term.cbreak():
            while term.inkey() != ' ': pass

    # --- Compliance Run Evaluation Summary (With Static Q-Exit Hold) ---
    print(term.clear() + term.home, end="")
    pass_mark = 1
    is_compliant = correct_counter >= pass_mark
    
    print(term.green("\n    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗\n    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║\n    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║\n    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║\n    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝\n    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ \n              --- T H E   S E N T R Y   T R I A L S ---"))
    print("\n" + "="*60)
    print(term.center(term.bold_cyan("== COMPLIANCE EVALUATION COMPLETED ==")))
    print("="*60)
    print(f"\n\t-> Valid Instructions Sent: {correct_counter} out of {sample_size}")
    print(f"\t-> Required Passing Mark:  {pass_mark}")
    print(f"\t-> Cumulative Net Points:   " + term.bold_bright_green(f"{total_accumulated_points} pts"))
    
    if is_compliant:
        print("\n\t" + term.bold_bright_green("[+] PARADIGM SHIFT: COMPLIANT. NEXT OPERATIONAL LAYER DECRYPTED!"))
    else:
        print("\n\t" + term.bold_red("[-] PARADIGM SHIFT: INSECURE STATE. GAUNTLET RE-ENGAGED."))
    
    print("\n" + "="*60)
    print(term.bold_yellow(term.center(">>> PRESS [Q] TO RETURN TO THE MASTER CONSOLE MENU <<<")))
    print("="*60)
    
    # Infinite hold loop until user inputs 'Q' to bounce back safely
    with term.cbreak():
        while True:
            exit_key = term.inkey().upper()
            if exit_key == 'Q':
                break
                
    return is_compliant

def menu_loop():
    while True:
        profile = load_profile()
        render_banner()
        print(term.center(term.bold_cyan("== CHOOSE YOUR TRAINING CRUCIBLE ==")))
        print("\n")
        t1_status = term.green("[ UNLOCKED ]") if profile["tier_1_unlocked"] else term.red("[ LOCKED ]")
        t2_status = term.green("[ UNLOCKED ]") if profile["tier_2_unlocked"] else term.black_on_bright_black("[ ENCRYPTED ]")
        t3_status = term.green("[ UNLOCKED ]") if profile["tier_3_unlocked"] else term.black_on_bright_black("[ ENCRYPTED ]")
        t4_status = term.green("[ UNLOCKED ]") if profile["tier_4_unlocked"] else term.black_on_bright_black("[ ENCRYPTED ]")
        
        print(f"\t[1] TIER 1: The Scavenger -> {t1_status}\n\t[2] TIER 2: The Data Filter -> {t2_status}\n\t[3] TIER 3: The Sys-Admin -> {t3_status}\n\t[4] TIER 4: The Shadow Operative -> {t4_status}\n\n\t[E] Exit System Console\n")
        print(term.cyan("sentry_user@trials:~# "), end=""); sys.stdout.flush()
        with term.cbreak(): inp = term.inkey().upper()
            
        if inp == 'E':
       	    print("\n[+] Exiting terminal matrix cleanly. Stay secure.")
            print("SENTRY_SIGNAL_DEACTIVATE")
            break
        elif inp == '1':
            if execute_tier_session("The Scavenger", "tier1_scavenger", profile):
                profile["tier_2_unlocked"] = True; save_profile(profile)
        elif inp == '2' and profile["tier_2_unlocked"]:
            if execute_tier_session("The Data Filter", "tier2_filter", profile):
                profile["tier_3_unlocked"] = True; save_profile(profile)
        elif inp == '3' and profile["tier_3_unlocked"]:
            if execute_tier_session("The Sys-Admin", "tier3_admin", profile):
                profile["tier_4_unlocked"] = True; save_profile(profile)
        elif inp == '4' and profile["tier_4_unlocked"]:
            execute_tier_session("The Shadow Operative", "tier4_shadow", profile)
        elif inp in ['1', '2', '3', '4']:
            print("\n" + term.red("[!] ACCESS DENIED!")); time.sleep(1)

if __name__ == "__main__":
    menu_loop()
