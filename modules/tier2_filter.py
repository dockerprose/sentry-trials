# Tier 2 Databank: The Data Filter (Text Processing & Pipes)

QUESTIONS = [
    {
        "id": "T2_Q1",
        "type": "MCQ",
        "scenario": "A massive Nginx access log contains thousands of entries, and you need to filter out only the rows that contain a '404' status code.",
        "question": "Which command pipe structure isolates rows containing '404' from a file named 'access.log'?",
        "options": [
            "A) cat access.log | grep '404'",
            "B) grep '404' < access.log",
            "C) Both A and B are syntactically valid",
            "D) filter '404' access.log"
        ],
        "correct": "C",
        "insight": "Both structures work perfectly. 'cat' pipes the stdout stream into grep, whereas the '<' operator redirects the file's data stream directly into grep's stdin."
    },
    {
        "id": "T2_Q2",
        "type": "DIRECT",
        "scenario": "You are auditing a security authentication log file located at '/var/log/auth.log' to check for unauthorized access attempts.",
        "question": "Type the exact command used to read the log file and continuously print new appended rows in real time.",
        "correct": "tail -f /var/log/auth.log",
        "insight": "The 'tail -f' (follow) command keeps the file descriptor open and streams incoming blocks directly to standard output as they are written."
    },
    {
        "id": "T2_Q3",
        "type": "MCQ",
        "scenario": "You want to count the exact number of failed login attempts from a pre-filtered text dump file named 'failed_attempts.txt'.",
        "question": "Which command utility and flag combination counts the absolute number of lines in a text file stream?",
        "options": ["A) wc -l", "B) wc -w", "C) count -l", "D) grep -c"],
        "correct": "A",
        "insight": "The 'wc' (word count) utility with the -l flag isolates newline characters to measure total line count instances."
    },
    {
        "id": "T2_Q4",
        "type": "DIRECT",
        "scenario": "You have a comma-separated text file called 'users.csv' and you only want to extract the first column (usernames).",
        "question": "Type the exact command using 'cut' with a comma delimiter to parse out only field column 1.",
        "correct": "cut -d',' -f1 users.csv",
        "insight": "The -d parameter changes the token separator from a tab to a comma, and -f1 restricts output to the first delimited field container."
    },
    {
        "id": "T2_Q5",
        "type": "MCQ",
        "scenario": "You need to locate the word 'CRITICAL' across hundreds of log files buried inside nested directories.",
        "question": "Which flag combination allows 'grep' to search recursively down all subdirectories while ignoring text case matching?",
        "options": ["A) grep -ri", "B) grep -rc", "C) grep -v", "D) grep -x"],
        "correct": "A",
        "insight": "The -r flag triggers a deep recursive filesystem traversal, while the -i flag neutralizes case-sensitivity barriers (CRITICAL vs critical)."
    },
    {
        "id": "T2_Q6",
        "type": "DIRECT",
        "scenario": "You need to quickly view just the first 15 lines of a configuration file named 'sysctl.conf' to verify its network parameters.",
        "question": "Type the exact command syntax used to output only the first 15 lines of this file.",
        "correct": "head -n 15 sysctl.conf",
        "insight": "The 'head' utility defaults to 10 lines, but passing the -n modifier overrides the display frame to the exact line threshold specified."
    },
    {
        "id": "T2_Q7",
        "type": "MCQ",
        "scenario": "You have an unsorted log file named 'ips.txt' filled with duplicate IP addresses. You want a list of unique IPs.",
        "question": "What is the correct pipeline structure to clean out duplicate entries from a raw text file stream?",
        "options": [
            "A) unique ips.txt",
            "B) cat ips.txt | sort | uniq",
            "C) cat ips.txt | uniq",
            "D) sort -u < ips.txt"
        ],
        "correct": "B",
        "insight": "The 'uniq' filter only drops adjacent duplicate records. Therefore, data streams must be processed through 'sort' first to aggregate duplicates together."
    },
    {
        "id": "T2_Q8",
        "type": "DIRECT",
        "scenario": "You need to search an error log 'error.log' and print out all lines that do NOT contain the string 'DEBUG'.",
        "question": "Type the exact 'grep' command string used to invert a pattern match search on this file.",
        "correct": "grep -v 'DEBUG' error.log",
        "insight": "The -v (--invert-match) parameter flips the filtering criteria, dropping matched lines and transmitting non-matching data blocks downstream."
    },
    {
        "id": "T2_Q9",
        "type": "MCQ",
        "scenario": "You want to stream a data stream onto the screen layout while simultaneously routing a twin copy into a permanent log file named 'output.log'.",
        "question": "Which specialized stream multiplexer command splits standard input into multiple targets?",
        "options": ["A) split", "B) tee", "C) mirror", "D) dump"],
        "correct": "B",
        "insight": "The 'tee' command functions like a T-splitter pipe connection, copying input streams directly to stdout while writing an exact mirror onto disk storage."
    },
    {
        "id": "T2_Q10",
        "type": "DIRECT",
        "scenario": "You need to dynamically change every instance of the string 'PORT=80' to 'PORT=443' inside a local file named 'server.conf'.",
        "question": "Type the standard 'sed' stream editor command string used to execute this global substitution inline.",
        "correct": "sed -i 's/PORT=80/PORT=443/g' server.conf",
        "insight": "The -i parameter writes modifications directly back to the target file block, while the 's/old/new/g' syntax implements a global replacement pass."
    }
]
