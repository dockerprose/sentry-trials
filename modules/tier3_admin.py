# Tier 3 Databank: The Sys-Admin (Process Control & Rights)

QUESTIONS = [
    {
        "id": "T3_Q1",
        "type": "MCQ",
        "scenario": "A background service process has locked up and is consuming 100% CPU. You have its Process ID (PID) and need to force-kill it immediately.",
        "question": "Which signal number represents SIGKILL, forcing the Linux kernel to abruptly terminate the process execution path?",
        "options": ["A) -1", "B) -9", "C) -15", "D) -2"],
        "correct": "B",
        "insight": "Signal -9 (SIGKILL) cannot be caught, blocked, or ignored by the target process, forcing the kernel to instantly tear down its memory space."
    },
    {
        "id": "T3_Q2",
        "type": "DIRECT",
        "scenario": "You need to inspect every active process currently running across the entire operating system kernel infrastructure.",
        "question": "Type the standard 'ps' command string with standard flags used to display a snapshot of all system-wide processes in standard syntax.",
        "correct": "ps -ef",
        "insight": "The -e flag selects all processes, and -f activates the full-format listing profile showing detailed UID, PID, and PPID parent linkages."
    },
    {
        "id": "T3_Q3",
        "type": "MCQ",
        "scenario": "You have a bash script named 'deploy.sh' that currently cannot be executed because its file permissions are restricted.",
        "question": "Which octal (numerical) mode notation passed to 'chmod' grants full Read, Write, and Execute rights to the Owner, but only Read/Execute to everyone else?",
        "options": ["A) 777", "B) 755", "C) 644", "D) 700"],
        "correct": "B",
        "insight": "Octal 755 evaluates to: Owner (4+2+1=7), Group (4+0+1=5), and Public (4+0+1=5). This is the standard deployment configuration for executable script assets."
    },
    {
        "id": "T3_Q4",
        "type": "DIRECT",
        "scenario": "You need to change the absolute owner configuration of a configuration directory named '/etc/nginx/ssl' to a system user named 'secops'.",
        "question": "Type the exact command syntax used to assign ownership of that path to the 'secops' user account.",
        "correct": "chown secops /etc/nginx/ssl",
        "insight": "The 'chown' (change owner) utility maps the directory node filesystem descriptor straight to the new user account UID profile entry."
    },
    {
        "id": "T3_Q5",
        "type": "MCQ",
        "scenario": "You launched a heavy data-backup migration script in your terminal, but you need to clear the current shell prompt by pushing that active task into the background.",
        "question": "Which keyboard shortcut sequence sends a running foreground process a SIGTSTP signal to suspend its loop execution so you can run 'bg'?",
        "options": ["A) Ctrl + C", "B) Ctrl + Z", "C) Ctrl + D", "D) Ctrl + X"],
        "correct": "B",
        "insight": "Ctrl+Z intercepts foreground stream executions and places them into an isolated 'Stopped' stack index frame, freeing up your active prompt shell context."
    },
    {
        "id": "T3_Q6",
        "type": "DIRECT",
        "scenario": "You have suspended a backup task and now want to resume its execution routine quietly in the background without locking your prompt screen.",
        "question": "Type the exact short shell command used to resume the last suspended process index job in the background space.",
        "correct": "bg",
        "insight": "The 'bg' (background) command passes a resume signal to the last indexed job control slot, turning its state descriptor from suspended to active-background."
    },
    {
        "id": "T3_Q7",
        "type": "MCQ",
        "scenario": "You need to monitor real-time system resource allocation, including live-updating tracking loops for CPU core states, RAM consumption blocks, and active process threads.",
        "question": "Which interactive, colored console utility is modernly preferred over standard 'top' for real-time performance troubleshooting?",
        "options": ["A) htop", "B) sysstat", "C) pstat", "D) nmon"],
        "correct": "A",
        "insight": "'htop' provides an interactive, scrollable, and color-coded text layout representation of system resources, allowing direct process signaling controls."
    },
    {
        "id": "T3_Q8",
        "type": "DIRECT",
        "scenario": "You want to run a long-duration data scraping tool, but you want to ensure it keeps executing even if your SSH terminal session unexpectedly drops out or disconnects.",
        "question": "Type the prefix command utility string used to run a script named 'track.sh' wrapped inside a hangup-immune session container.",
        "correct": "nohup ./track.sh &",
        "insight": "The 'nohup' (no hangup) command intercepts incoming SIGHUP terminal signals, rerouting output onto a local file while the '&' character forces immediate background fork assignment."
    },
    {
        "id": "T3_Q9",
        "type": "MCQ",
        "scenario": "You need to inspect the absolute default access mask settings applied to newly instantiated files and directories inside your current user shell profile environment.",
        "question": "Which native internal configuration command reports or alters this default base permission filter mask metric?",
        "options": ["A) mask", "B) umask", "C) chmod", "D) setfacl"],
        "correct": "B",
        "insight": "The 'umask' value sets bits that are subtracted from default base creation modes (777 for directories, 666 for files) to establish security permissions by default."
    },
    {
        "id": "T3_Q10",
        "type": "DIRECT",
        "scenario": "You need to modify the file ownership settings of a folder named '/var/www/html' so that both the user owner and group owner are instantly updated to 'www-data' simultaneously.",
        "question": "Type the short 'chown' syntax used to apply 'www-data' as both the user and group owner in a single operation step.",
        "correct": "chown www-data:www-data /var/www/html",
        "insight": "Passing the username and group name separated by a colon (:) instructs the chown syscall parser to adjust both permission attribute targets across the target folder metadata frame."
    }
]
