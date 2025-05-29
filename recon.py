# this code will serve in steps
# 1. get subdomains from various tools and maybe sites in the future
# 2. filter them from duplicates
# 3. run httpx to filter lives
# 4. then it will create a folder that has alot of txt files a file for 403,401 and file for live subdomains and a file for 404s if you want to test fuzzing or something
from modules.gather import *
from modules.probe import *
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain',required=True, help="target domain")
    args = parser.parse_args()
    domain = args.domain

    # Create output directory
    os.makedirs("output",exist_ok=True)
    
    # Get subdomains from multiple sources
    print("[*] Gathering subdomains...")
    subs = set()
    
    # Get subdomains from AssetFinder
    assetfinder_subs = AssetFinder(domain)
    subs.update(assetfinder_subs)
    print(f"[+] Found {len(assetfinder_subs)} subdomains from AssetFinder")
    
    # Get subdomains from SubFinder
    subfinder_subs = SubFinder(domain)
    subs.update(subfinder_subs)
    print(f"[+] Found {len(subfinder_subs)} subdomains from SubFinder")
    
    # Get subdomains from FindDomain
    findomain_subs = FindDomain(domain)
    subs.update(findomain_subs)
    print(f"[+] Found {len(findomain_subs)} subdomains from FindDomain")
    
    # Convert set to sorted list
    subs = sorted(list(subs))
    print(f"[+] Total unique subdomains found: {len(subs)}")
    
    # Get Wayback URLs for all subdomains
    #wayback_urls = getWaybackUrls(domain, subs)
    
    # Probe subdomains
    print("[*] Probing subdomains...")
    aliveSubs = httpxAlive(subs)
    subs_401 = httpx403(subs)
    subs_404 = httpx404(subs)

if __name__ == "__main__":
    main()
        



