# OREE

A reconnaissance tool that automates subdomain enumeration and analysis.

![ore](images/ore.png)

## Features

- Automated subdomain discovery using multiple tools
- Subdomain categorization by HTTP status codes
- Wayback machine URL gathering
- Organized output structure

## Installation

```bash
git clone https://github.com/Nadleer/oree.git
```

## Usage

```bash
python3 recon.py -d <domain>
```

## Output Structure

```
output/
└── domain.com/
    ├── urls/
    │   ├── waybackurls.txt  # waybackurls archived urls
        ├── gau.txt          # gau archived urls

    └── subdomains/
        ├── alive.txt        # 200 OK status subdomains
        ├── 403.txt          # 401/403 status subdomains
        └── 404.txt          # 404 status subdomains
```

## Future Plans

- Fuzzing capabilities
- Attack vector generation
- Additional reconnaissance features
