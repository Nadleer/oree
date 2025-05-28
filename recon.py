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

    subs = AssetFinder(domain) 
    subs.sort()
    set(subs)

    os.makedirs("output",exist_ok=True)
    
    aliveSubs = httpxAlive(subs)
    subs_401 = httpx403(subs)
    subs_404 = httpx404(subs) 

if __name__ == "__main__":
    main()
        



