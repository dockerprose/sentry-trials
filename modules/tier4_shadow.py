# Tier 4 Databank: The Shadow Operative (Networking & Hardening)

QUESTIONS = [
    {
        "id": "T4_Q1",
        "type": "MCQ",
        "scenario": "You suspect a rogue backend malicious process has opened an unauthorized listening port on your server interface.",
        "question": "Which modern command combination replaces the old 'netstat' to list active listening TCP sockets with raw numerical port values and their associated Process PIDs?",
        "options": ["A) ss -tlnp", "B) net -listening", "C) sockstat -a", "D) ip route show"],
        "correct": "A",
        "insight": "The 'ss' utility queries kernel socket arrays directly. The flags filter for: -t (TCP), -l (Listening state), -n (Numeric port mapping format), and -p (Process PID identity mapping)."
    },
    {
        "id": "T4_Q2",
        "type": "DIRECT",
        "scenario": "You are verifying connectivity to an external database layer endpoint cluster at IP address '10.0.0.5' specifically on database port 5432.",
        "question": "Type the exact standard short 'nc' or 'netcat' command format used to test raw TCP connection scanning status directly to that endpoint port path without sending data blocks.",
        "correct": "nc -zv 10.0.0.5 5432",
        "insight": "The -z flag drops out data streaming (zero-I/O mode for port scanning), and -v triggers verbose reporting to clearly capture whether the target port socket successfully handles raw socket handshakes."
    },
    {
        "id": "T4_Q3",
        "type": "MCQ",
        "scenario": "You need to pull down the raw HTML layout manifest map data stream from an external API secure route endpoint at 'https://api.sentry.internal/v1/status' via command terminal.",
        "question": "Which robust data transfer utility tool handles streaming downloads across URL protocol strings natively directly from command prompt layers?",
        "options": ["A) wget", "B) curl", "C) fetch", "D) secure_get"],
        "correct": "B",
        "insight": "'curl' streams URL resource payloads directly onto stdout by default, making it the premier pipeline tooling mechanism for handling RESTful endpoint connectivity loops inside background system layers."
    },
    {
        "id": "T4_Q4",
        "type": "DIRECT",
        "scenario": "You need to display the absolute interface state settings, network layer hardware MAC address attributes, and bound local IPv4 addresses configurations of your physical system interfaces.",
        "question": "Type the modern short 'ip' object command string that replaces old 'ifconfig' loops to list all active system interface parameters.",
        "correct": "ip addr",
        "insight": "The 'ip addr' object mapping interacts directly with the Linux kernel's modern Netlink interface routing configuration infrastructure, returning state attributes instantly."
    },
    {
        "id": "T4_Q5",
        "type": "MCQ",
        "scenario": "You want to track the actual path route map of routers and tracking hops that network packets hop across from your local machine to reach an external domain node at 'google.com'.",
        "question": "Which network path validation utility drops ICMP/UDP diagnostic packets with incrementally scaling Time-To-Live (TTL) values to map target hops?",
        "options": ["A) ping", "B) traceroute", "C) tracepath", "D) route-map"],
        "correct": "B",
        "insight": "'traceroute' analyzes expired ICMP time-exceeded response messages returned from intermediary core networking gateways, printing out an end-to-end routing hop timeline."
    },
    {
        "id": "T4_Q6",
        "type": "DIRECT",
        "scenario": "You are troubleshooting a DNS routing error and need to query the official DNS name servers to look up the authoritative 'MX' (Mail Exchange) records assigned to a target zone named 'secops.org'.",
        "question": "Type the standard 'dig' command syntax used to isolate and read exactly the MX records block for that domain name target zone.",
        "correct": "dig secops.org MX",
        "insight": "The 'dig' (domain information groper) utility interfaces with resolver nodes directly, allowing engineers to append query arguments (like A, MX, TXT) to isolate target namespace resource records panels."
    },
    {
        "id": "T4_Q7",
        "type": "MCQ",
        "scenario": "You are managing the native Linux Uncomplicated Firewall (UFW) profile engine layer and need to check the active rule matrix tracking statuses.",
        "question": "Which specific management flag configuration command outputs the firewall rule tables along with their active rule sequence priority lines?",
        "options": ["A) ufw show", "B) ufw status numbered", "C) ufw list", "D) ufw rules"],
        "correct": "B",
        "insight": "Appending the 'status numbered' block configuration instruction allows administrators to inspect firewall indexing tables with numeric prefixes, making precision deletion operations straightforward."
    },
    {
        "id": "T4_Q8",
        "type": "DIRECT",
        "scenario": "You need to add a hard security restriction line rule inside the local UFW firewall parameters to completely block any incoming traffic packets attempting to cross port 23 (Telnet).",
        "question": "Type the exact 'ufw' operational layout statement string required to create an absolute drop rule on port 23 traffic streams.",
        "correct": "ufw deny 23",
        "insight": "The 'ufw deny' modifier constructs a high-priority packet filter line drop match targeting any data packets routing onto the designated port index descriptor."
    },
    {
        "id": "T4_Q9",
        "type": "MCQ",
        "scenario": "You need to view the localized static IP-to-Hostname lookups file mapped to bypass internet DNS resolution sweeps for development testing environments.",
        "question": "Inside which protected system file block path are these localized hard-coded static network maps maintained on a standard Linux platform infrastructure?",
        "options": ["A) /etc/resolv.conf", "B) /etc/hosts", "C) /etc/networks", "D) /var/dns/local"],
        "correct": "B",
        "insight": "The local system mapping engine parses '/etc/hosts' first before looking out to network DNS providers, allowing instant domain routing translation manipulation for development pathways."
    },
    {
        "id": "T4_Q10",
        "type": "DIRECT",
        "scenario": "You need to analyze internet data packet traffic patterns passing across your active network stack lines in real time by scanning interface packets directly.",
        "question": "Type the industry standard core command utility name tool used to capture, dissect, and log network raw packets via terminal loop.",
        "correct": "tcpdump",
        "insight": "The 'tcpdump' engine functions by binding a raw socket capture layer straight onto the physical network interface card, tracing raw stream data strings for infrastructure analysis."
    }
]
