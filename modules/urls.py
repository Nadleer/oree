#this section will have the extracting urls part. 
#1. waybackurls in all subs
#2. gau bec why not
#3. params
import subprocess  
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, parse_qs
import os
#helper functions----
def save_to_file(data,path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,'w') as f:
        f.write("\n".join(sorted(set(data)))+ "\n")

def run_tool(tool, input_file):
    try:
        cmd = f"cat {input_file} | {tool}"
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            print(f"[!] {tool} failed: {result.stderr.strip()}")
            return []
        return result.stdout.splitlines()

    except FileNotFoundError:
        print(f"[!] {tool} not installed or not in path")
        return []
    except subprocess.TimeoutExpired:
        print(f"[!] {tool} timed out")
        return []


#----------------
def getWaybackurls(domain ,file, output_dir):
    print("[*] fetching archived URLs (waybackurls + gau)...")

    urls_dir = os.path.join(output_dir,"urls")
    wayback_file = os.path.join(urls_dir,"waybackurls.txt")
    gau_file = os.path.join(urls_dir,"gau.txt")

    #run both tools in parallel
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_wayback = executor.submit(run_tool,"waybackurls",file)
        future_gau = executor.submit(run_tool,"gau",file)

        wayback_urls = future_wayback.result()
        gau_urls = future_gau.result()

    save_to_file(wayback_urls,wayback_file)
    save_to_file(gau_urls,gau_file)
    all_urls = wayback_urls + gau_urls
    print(f"[+] total archived URLs collected: {len(set(all_urls))}")
    return list(set(all_urls))
