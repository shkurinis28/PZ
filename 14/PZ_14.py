"""
В исходном текстовом файле(radio stations.txt) найти все домены из URL-адресов
(например, в URL-apece http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
домен выделен полужирным).
"""

import re

def extract_domains(filename):
    domains = set()  
    url_pattern = re.compile(r'https?://([^/:]+)')

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
      
            match = url_pattern.search(line)
            if match:
                domain = match.group(1)
                
                domain = domain.split(':')[0]
                domains.add(domain)
    
    return sorted(domains) 

filename = 'radio stations.txt'
domains = extract_domains(filename)

print("Найденные домены:")
for i, domain in enumerate(domains, 1):
    print(f"{i}. {domain}")
