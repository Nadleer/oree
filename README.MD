# OREE

<p>welcome to OREE where you can automate some recon stuff</p>
![ore](/images/ore.png)
this tool will help automate subdomain finding and in the future it will fuzz and generate new attack vectors for you

# usage

```
python3 recon.py -d <domain>
```

# how does it work

this tool will make a folder called <b>output</b> and it will have 3 txt files

1. subs_alive.txt => this for 200 OK status subdomains
2. 403_subs.txt => this for 401,403 status codes and it's purpose is for fuzzing
3. 404_subs.txt => like above this is 404 status code subdomains for fuzzing

this tool is still being built by me only and i will making new version.
