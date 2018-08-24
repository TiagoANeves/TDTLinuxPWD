# TDTLinuxPWD

Linux shadow password crack

## Installing

Clone this repository:
``` sh
git clone https://github.com/TiagoANeves/TDTLinuxPWD.git
```

Now, extract the wordlist file:
``` sh
gunzip wordlist.txt.gz
```

## Default wordlist file

The script will use the file `wordlist.txt` by default if the option -w is not specified

## Examples
### Help menu
``` sh
python TDTLinuxPWD.py -h 
```
### Using the default wordlist
``` sh
python TDTLinuxPWD.py -s /etc/shadow 
```
### Using a personalized wordlist
``` sh
python TDTLinuxPWD.py -s /etc/shadow -w /path/to/wordlist.txt 
```
![Print](/images/Print.png)

That's all folks!

## License

TDTLinuxPWD is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/TiagoANeves/TDTLinuxPWD/blob/master/LICENSE) for more information.

## Version
**Current version is 1.1.0**

## Credits
- [Tiago Neves](https://github.com/TiagoANeves)
