<p align="center"> <img src="https://raw.githubusercontent.com/qeeqbox/analyzer/master/readme/analyzerlogo.png"></p>

#
[![Generic badge](https://img.shields.io/badge/dynamic/json.svg?url=https://raw.githubusercontent.com/qeeqbox/analyzer/master/info&label=version&query=$.version&colorB=blue&style=flat-square)](https://github.com/qeeqbox/analyzer/blob/master/changes.md) [![Generic badge](https://img.shields.io/badge/dynamic/json.svg?url=https://raw.githubusercontent.com/qeeqbox/analyzer/master/info&label=docker-compose&query=$.dockercompose&colorB=green&style=flat-square)](https://github.com/qeeqbox/analyzer/blob/master/changes.md) [![Generic badge](https://img.shields.io/static/v1?label=%F0%9F%91%8D&message=Thank%20You!&color=yellow&style=flat-square)](https://github.com/qeeqbox/analyzer/stargazers)

Offline Threat Intelligence Analyzer for extracting features, artifacts and IoCs from data into readable and visualized format. `This project was developed for analyzing classified data and training some AI locally without internet/external resources interaction`

## New Dark Interface
<img src="https://raw.githubusercontent.com/qeeqbox/analyzer/master/readme/intro.gif" style="max-width:768px"/>

## Output 
- [APT-Malware JSON\HTML reports (+190 sample)](https://files.qeeqbox.com/set1/)

## General Features
- Runs locally (Offline)
- Analyze buffer, file or full folder
- Intime analysis (Session is saved)
- 2 modes (Interactive and silent)
- Generates HTML or JSON as output
- Dump output file with details to mongodb
- Save raw json result to mongodb
- Basic file information MD5, charset, mime, ssdeep
- Different string/patterns analysis methods
- NL English words detection
- OCR words detection
- IPS hints and countries description
- Ports hints
- World IPS world image and flags
- DNS servers description (Top servers)
- Websites similarity detection (Top 10000)
- Artifacts force directed image
- Cross references force directed image and table
- MITRE att&ck tools and patterns detection (could be FP)
- Similarity image divided to classes
- YARA module and YARA rules included (Downloaded a copy from yara-rules-github)
- YARA module includes conditions
- Yara tags by index
- URL/EMAIL/TEL/Tags patterns extraction
- Credit Cards patterns extraction
- Credential patterns extraction
- Encryption patterns (base64, md5, sha1..) extraction
- DGA (Domain Generation Algorithm) patterns extraction 
- BOM (Byte Order Mark) detection
- URL shorteners extraction
- ASCII extraction from UNICODE
- Whitelist implemented (Windows7, 8 and 10 files)
- Check WAF and bypass proxy
- Free/Fake email extraction
- Spelling and punctuation check
- Top phishing words included
- Snort support
- Web interface
- Supports threat intelligence platform feeds

## Other Features
- Linux (wrapper)
    - ELF information
    - API functions descriptions
    - System commands descriptions
    - Sections descriptions
    - Lib descriptions
    - Encrypted section detection
    - Symbols extraction
    - MITRE artifacts mapped to detection
    - Cross references detection
    - Behavior detection
- macOS (wrapper)
    - DMG extraction
    - Shell code detection
    - PLIST information
    - MITRE artifacts mapped to detection
    - macOS information
- Windows (wrapper)
    - PE information
    - Encrypted section detection
    - Sections descriptions
    - DLL descriptions
    - Symbols extraction
    - Signature extraction and validation
    - API descriptions
    - PE ASLR, DEP, SEH and CFG detection
    - MITRE artifacts mapped to detection
    - API Behavior detection (DLL injection, Process Hollowing, Process Doppelganging etc..)
    - Cross references detection
    - Icon extraction
    - Extract String file info (FileDescription, FileDescription etc..)
- Android (wrapper)
    - APK information
    - DEX information
    - Manifest descriptions
    - Intent descriptions
    - Resources extraction
    - Symbols extraction
    - Classes extraction
    - Big functions identification 
    - Cross references detection
    - API Behavior detection
- IPhone (built-in)
    - IPA information
- BlackBerry (COD) (built-in)
    - COD information
    - Functions extraction
    - Strings extraction
- PCAP (wrapper)
    - Frame filter
    - HTTP filter
    - DNS filter
    - ARP filter
    - WAF detection
    - DGA detection
    - Snort parsing
- PDF (built-in)
    - Objects enumeration
    - Keys (javascript, js, OpenAction) extraction
    - Streams parsing
    - String analysis
- Office (built-in and wrapper)
    - Meta info extraction
    - Hyper and target links extraction
    - Bin printable parser
    - Extract Text
    - Extract DDE
    - Macros extraction
- OLE (wrapper)
    - Number of objects
    - Object extraction
    - Macros extraction
- EMAIL (built-in and wrapper)
    - Header information
    - Attachment extraction and parsing 
    - Extract body
    - Phishing patterns check
- Archives (wrapper)
    - Extract mimes and guess by extensions
    - Finding patterns in all unpacked files
    - Encrypted archives detection
- HTML (wrapper)
    - Extract scripts, iframes, links and forms
    - Decode/analyze links
    - Script entropy
- Online TIPs (Required tokens, Moving to different project)
    - HybridAnalysis
    - MalShare
    - MetaDefender
    - VirusTotal
    - AlienVault
    - PulseDive

## Roadmap
- &#9745; ~~Reduce file I/O~~
- &#9745; ~~PDF module~~
- &#9745; ~~RTF module~~
- &#9745; ~~Fix htmlmaker (return concat(self.root_render_func(self.new_context(vars))) MemoryError) due to rendering large objects.. this happened due to yara module appending too many results that caused htmlmaker to hang . Solved by grouping yara results into one~~
- &#9745; ~~HTML module~~
- &#9745; ~~Refactoring modules v2~~
- &#9745; ~~Converting some yara rules into individual modules (Requested by users)~~
- &#9745; ~~Whitelist (Requested by users)~~
- &#9745; ~~Switching to mongodb (Requested by users)~~
- &#9745; ~~Phishing module~~
- &#9745; ~~Web service and API~~
- &#9745; ~~Web interface (Requested by users)~~
- &#9745; ~~Curling some TIPs (Requested by users)~~
- &#9745; ~~MS office module~~
- &#9745; ~~Snort wrapper (Requested by users)~~
- &#9745; ~~Machine learning modules - Moving to different project~~
- &#9745; ~~Offline multiscanner - Moving to different project~~
- Java analysis (Requested by users)
- Web detection
- Adding username and password wrappers to databases
- Adding more creds pattern (Requested by users)
- CSS clean up

## Running
#### One click auto-configure
git clone https://github.com/qeeqbox/analyzer.git <br>
cd analyzer <br>
chmod +x run.sh <br>
./run.sh auto_configure <br>

The project interface http://127.0.0.1:8000/login/ will open automatically after finishing the initialization process

#### Or, if you already have docker-compose
docker-compose -f docker-compose-dev.yml up --build

Then open http://127.0.0.1:8000/login/

## Prerequisites
apt-get install -y python3 python3-pip curl libfuzzy-dev yara libmagic-dev libjansson-dev libssl-dev libffi-dev tesseract-ocr libtesseract-dev libssl-dev swig p7zip-full radare2 dmg2img mongodb redis

pip3 install pyelftools macholib python-magic nltk Pillow jinja2 ssdeep pefile scapy r2pipe pytesseract M2Crypto requests tld tldextract bs4 psutil pymongo flask pyOpenSSL oletools extract_msg

Prerequisites packages are required for some modules (If you are having issues using those packages, I might be able to share with you my own alternatives that I developed in the past in C#\C)

## Resources
- Linux documentation
- MacOS documentation
- Windows documentation
- Android documentation
- software77
- MITRE ATT&CK™
- sc0ty
- hexacorn
- PEID
- cisco umbrella 
- yara rules community 
- TONS OF RESEARCHES.. (Please let me know if i missed a resource or dependency)

## Other Licenses
By using this framework, you are accepting the license terms of each package listed below:
- https://github.com/arbor/yara/blob/master/LICENSE
- https://github.com/Yara-Rules/rules/blob/master/LICENSE
- https://github.com/tesseract-ocr/tesseract/blob/master/LICENSE
- http://www.swig.org/Release/LICENSE
- https://www.radare.org/r/license.html
- http://vu1tur.eu.org/tools/LICENSE
- https://github.com/decalage2/oletools/wiki/License
- https://www.mongodb.com/community/licensing
- https://github.com/Supervisor/supervisor/blob/master/COPYRIGHT.txt
- https://github.com/mattgwwalker/msg-extractor/blob/master/LICENSE.txt
- https://www.snort.org/license
- https://github.com/eliben/pyelftools/blob/master/LICENSE
- https://bitbucket.org/ronaldoussoren/macholib/src/default/LICENSE
- https://github.com/erocarrera/pefile/blob/master/LICENSE
- https://github.com/secdev/scapy/blob/master/LICENSE
- https://github.com/ahupp/python-magic/blob/master/LICENSE
- https://flask.palletsprojects.com/en/0.12.x/license/
- https://github.com/pallets/werkzeug/blob/master/LICENSE.rst
- https://github.com/benoitc/gunicorn/blob/master/LICENSE
- https://github.com/MongoEngine/flask-mongoengine/blob/master/LICENSE
- https://github.com/flask-admin/flask-admin/blob/master/LICENSE
- https://github.com/maxcountryman/flask-login/blob/master/LICENSE
- https://github.com/maxcountryman/flask-bcrypt/blob/master/LICENSE
- https://github.com/pyca/pyopenssl/blob/master/LICENSE
- https://github.com/dcolish/flask-markdown/blob/master/LICENSE
- https://github.com/barseghyanartur/tld/blob/master/LICENSE_GPL2.0.txt
- https://github.com/giampaolo/psutil/blob/master/LICENSE
- https://github.com/gevent/gevent/blob/master/LICENSE
- https://github.com/dateutil/dateutil/blob/master/LICENSE
- https://requests.readthedocs.io/en/master/user/intro/
- https://github.com/mher/pymongo/blob/master/LICENSE
- https://www.crummy.com/software/BeautifulSoup/
- https://github.com/john-kurkowski/tldextract/blob/master/LICENSE
- https://gitlab.com/m2crypto/m2crypto/-/blob/master/LICENCE
- https://github.com/madmaze/pytesseract/blob/master/LICENSE
- https://github.com/radareorg/radare2-r2pipe/blob/master/dotnet/LICENSE
- https://ssdeep-project.github.io/ssdeep/index.html
- https://github.com/Kronuz/jinja2/blob/master/LICENSE
- https://github.com/python-pillow/Pillow/blob/master/LICENSE
- https://github.com/nltk/nltk/blob/develop/LICENSE.txt
- http://p7zip.sourceforge.net/
- https://redislabs.com/legal/licenses/
- https://github.com/andymccurdy/redis-py/blob/master/LICENSE

## Disclaimer\Notes
- Do not deploy without proper configuration
- Setup some security group rules and remove default credentials
- This project is NOT an anti malware project and does not quarantine or delete malicious files

