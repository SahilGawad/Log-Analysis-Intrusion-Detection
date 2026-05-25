import re
from collections import Counter

def analyze_logs(content):

    logs = content.splitlines()

    ips = []

    for log in logs:

        found_ips = re.findall(r'\d+\.\d+\.\d+\.\d+', log)

        for ip in found_ips:
            ips.append(ip)

    counter = Counter(ips)

    suspicious = []

    for ip, count in counter.items():

        if count > 5:

            suspicious.append({
                "ip": ip,
                "count": count
            })

    return suspicious