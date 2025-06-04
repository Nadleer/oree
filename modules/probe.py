import subprocess
import os

def httpxAlive(subdomains, output_dir):
    input_data = "\n".join(subdomains)
    subdomains_dir = os.path.join(output_dir, "subdomains")
    os.makedirs(subdomains_dir, exist_ok=True)

    try:
        result = subprocess.run(['httpx', '-mc', '200','-silent'],
        input=input_data,
        capture_output=True,
        text=True)
        if result.returncode != 0 :
            print("httpx error:", result.stderr)
            return []
        
        alive = result.stdout.splitlines()
        with open(f"{subdomains_dir}/alive.txt", "w") as f:
            f.write(result.stdout)

        print (f"[+] alive subdomains saved as {subdomains_dir}/alive.txt")
        return alive


    except FileNotFoundError:
        print("httpx not installed or not in path",result.stderr)
        return []
    
    
def httpx404(subdomains, output_dir):
    input_data ="\n".join(subdomains)
    subdomains_dir = os.path.join(output_dir, "subdomains")
    os.makedirs(subdomains_dir, exist_ok=True)

    try:
        result = subprocess.run(['httpx', '-mc', '404', '-silent'],
                                input=input_data,
                                capture_output=True,
                                text=True)
        if result.returncode != 0:
            print("httpx error", result.stderr)
            return []
        
        with open(f"{subdomains_dir}/404.txt","w") as f:
            f.write(result.stdout)
        
        print(f"[+] 404 subdomains saved as {subdomains_dir}/404.txt")

    except FileNotFoundError:
        print("httpx not found or not in path",result.stderr)
        return []





def httpx403(subdomains, output_dir):
    input_data = "\n".join(subdomains)
    subdomains_dir = os.path.join(output_dir, "subdomains")
    os.makedirs(subdomains_dir, exist_ok=True)

    try:
        result = subprocess.run(['httpx','-mc' ,'401', '403', '-silent'],
                                input=input_data,
                                capture_output=True,
                                text=True
                                )
        if result.returncode != 0:
            print("httpx error",result.stderr) 
            return []
        
        with open(f"{subdomains_dir}/403.txt","w") as f:
            f.write(result.stdout)

        print(f"[+] 403 and 401 subdomains saved as {subdomains_dir}/403.txt")

    

    except FileNotFoundError:
        print("httpx not found or not in path",result.stderr)
        return []
