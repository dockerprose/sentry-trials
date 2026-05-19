# Tier 1 Databank: The Scavenger (File & System Navigation)

QUESTIONS = [
    {
        "id": "T1_Q1",
        "type": "MCQ",
        "scenario": "A hidden config file containing critical environment variables is stored in your workspace directory.",
        "question": "Which flag appended to the 'ls' command will display hidden files (files starting with a dot)?",
        "options": ["A) ls -h", "B) ls -a", "C) ls -l", "D) ls -x"],
        "correct": "B",
        "insight": "The -a (--all) flag instructs the file system kernel to list entries starting with a dot (.), bypassing the standard hidden filter."
    },
    {
        "id": "T1_Q2",
        "type": "DIRECT",
        "scenario": "You need to verify the absolute directory path of your current shell environment session.",
        "question": "Type the exact native short command used to print the working directory path string.",
        "correct": "pwd",
        "insight": "The 'pwd' (print working directory) command pulls the current environment shell path directly from the active shell environment buffer."
    },
    {
        "id": "T1_Q3",
        "type": "MCQ",
        "scenario": "You need to view file sizes in a human-readable format (like KB, MB, GB) instead of raw blocks/bytes.",
        "question": "Which modifier combination gives you a detailed long listing with human-readable file sizes?",
        "options": ["A) ls -lh", "B) ls -la", "C) ls -s", "D) ls -x"],
        "correct": "A",
        "insight": "Combining -l (long listing) and -h (human-readable) scales byte counts to easily digestible metrics (K, M, G)."
    },
    {
        "id": "T1_Q4",
        "type": "DIRECT",
        "scenario": "You need to quickly switch back to your user's primary home directory (/home/ubuntu) from deep within the file system.",
        "question": "Type the single-character shell shortcut symbol used with 'cd' to represent the home directory path.",
        "correct": "~",
        "insight": "The tilde (~) is globally recognized by the shell interpreter as a shortcut mapping straight to the current user's environmental $HOME variable."
    },
    {
        "id": "T1_Q5",
        "type": "MCQ",
        "scenario": "You want to find out what type of data a file contains (e.g., ASCII text, ELF binary, or JPEG data) without opening it.",
        "question": "Which native Linux command analyzes the file header to print its actual file type format?",
        "options": ["A) cat", "B) file", "C) type", "D) stat"],
        "correct": "B",
        "insight": "The 'file' command reads the magic numbers stored in the file header blocks to accurately report its underlying MIME type."
    },
    {
        "id": "T1_Q6",
        "type": "DIRECT",
        "scenario": "You need to instantly create a completely empty file named 'log.txt' inside your working directory.",
        "question": "Type the short command used to instantiate an empty file or update its modified timestamp.",
        "correct": "touch log.txt",
        "insight": "The 'touch' command checks for file existence. If missing, it allocates an empty file allocation index node (inode) instantly."
    },
    {
        "id": "T1_Q7",
        "type": "MCQ",
        "scenario": "You need to create a nested directory tree structure (e.g., project/src/bin) in a single command execution.",
        "question": "Which flag must be appended to 'mkdir' to automatically build parent directories if they don't exist?",
        "options": ["A) mkdir -p", "B) mkdir -f", "C) mkdir -r", "D) mkdir -v"],
        "correct": "A",
        "insight": "The -p (--parents) flag tells mkdir to silently generate all missing upper-level directory nodes along the provided path string."
    },
    {
        "id": "T1_Q8",
        "type": "DIRECT",
        "scenario": "You are deep inside a subdirectory and want to jump exactly one level backward into the immediate parent folder.",
        "question": "Type the precise 'cd' argument syntax used to specify the parent directory node link.",
        "correct": "cd ..",
        "insight": "In Unix filesystems, double dots (..) act as a constant hard-coded shortcut referencing the parent directory block."
    },
    {
        "id": "T1_Q9",
        "type": "MCQ",
        "scenario": "You need to look up detailed file metrics, including exact access/modify timestamps, inode numbers, and block counts.",
        "question": "Which diagnostic utility displays comprehensive metadata statistics about a specific file node?",
        "options": ["A) file", "B) stat", "C) lsattr", "D) details"],
        "correct": "B",
        "insight": "The 'stat' command extracts full metadata fields directly from the filesystem's inode table, bypassing standard shallow listing profiles."
    },
    {
        "id": "T1_Q10",
        "type": "DIRECT",
        "scenario": "You want to display the full raw contents of a small text file named 'flag.txt' directly on your terminal display panel.",
        "question": "Type the short command used to concatenate and print file contents directly to standard output.",
        "correct": "cat flag.txt",
        "insight": "The 'cat' (concatenate) command reads stream bytes sequentially from a file descriptor and pumps them directly onto the stdout screen layout."
    }
]
