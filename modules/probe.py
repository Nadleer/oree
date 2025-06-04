import subprocess

def httpxAlive(subdomains):
    input_data = "\n".join(subdomains)

    try:
        result = subprocess.run(['httpx', '-mc', '200','-silent'],
        input=input_data,
        capture_output=True,
        text=True)
        if result.returncode != 0 :
            print("httpx error:", result.stderr)
            return []
        
        alive = result.stdout.splitlines()
        with open("output/subs_alive.txt", "w") as f:
            f.write(result.stdout)

        print ("[+] alive subdomains saved as subs_alive.txt")
        return alive


    except FileNotFoundError:
        print("httpx not installed or not in path",result.stderr)
        return []
    
    
def httpx404(subdomains):
    input_data ="\n".join(subdomains)

    try:
        result = subprocess.run(['httpx', '-mc', '404', '-silent'],
                                input=input_data,
                                capture_output=True,
                                text=True)
        if result.returncode != 0:
            print("httpx error", result.stderr)
            return []
        
        with open("output/404_subs.txt","w") as f:
            f.write(result.stdout)
        
        print("[+] 404 subdomains saved as 404_subs.txt")

    except FileNotFoundError:
        print("httpx not found or not in path",result.stderr)
        return []





def httpx403(subdomains):
    input_data = "\n".join(subdomains)
    try:
        result = subprocess.run(['httpx','-mc' ,'401', '403', '-silent'],
                                input=input_data,
                                capture_output=True,
                                text=True
                                )
        if result.returncode != 0:
            print("httpx error",result.stderr) 
            return []
        
        with open("output/403_subs.txt","w") as f:
            f.write(result.stdout)

        print("[+] 403 and 401 subdomains saved as 403_subs.txt")

    

    except FileNotFoundError:
        print("httpx not found or not in path",result.stderr)
        return []
