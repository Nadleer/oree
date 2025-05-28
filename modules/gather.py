# tools to add:
# apis from the famous domain collectors
# finddomain

import subprocess


def SubFinder(domain):
    try:
        result = subprocess.run(['subfinder', '-d', domain, '-silent'],
                                capture_output=True,
                                text=True)
        if result.returncode != 0:
            print("subfinder error:", result.stderr)
            return []
            
        subdomains = result.stdout.strip().split('\n')
        return subdomains
    
    except FileNotFoundError:
        print("subfinder now installed or not in path")
        return []

def AssetFinder(domain):
    try:
        result = subprocess.run(['assetfinder', domain],
                                 capture_output=True,
                                 text=True)
        if result.returncode != 0:
            print("assetfinder error", result.stderr)
            return []
            
        
        subdomains = result.stdout.strip().split("\n")
        return subdomains
    

    except FileNotFoundError:
            print("assetfinder not installed or not in path", result.stderr)
            return []
        

def FindDomain(domain):
    try:
        result = subprocess.run(['findomain', '-t', domain , '-q'], capture_output= True, text=True)
        if result.returncode != 0:
            print("findomain error", result.stderr)
            return []
            
        subdomains = result.stdout.strip().split("\n")
        return subdomains
            
    

    except FileNotFoundError:
        print("findomain not installed or not in path", result.stderr)
        return []