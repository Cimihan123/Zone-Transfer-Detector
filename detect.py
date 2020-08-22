import dns.zone
import pydig
import dns.resolver
import socket
import argparse
import time
from core.utils import url_list
from core.colors import red ,end, yellow,green,minus
import subprocess


parser = argparse.ArgumentParser(description='Help is Here')
parser.add_argument('-t','--target',action='store',help='singel target name',nargs=1)
parser.add_argument('-w','--wordlist',help='target list',dest='wordlist')
args = parser.parse_args()
#single domain
target = args.target

#wordlist
wordlist = args.wordlist
urls = url_list(target,wordlist)


def DnsResolve(urls):

    for target in urls:

        try:
            with open('ns.txt','a+') as file:
                dns_resolver = pydig.query(target,'NS')
                file = [file.write(str(dns)+'\n') for dns in dns_resolver]

                if file:
                  print(f"[{minus}] %s NameServer Found for {red}{target}{end}"%(green))
                else:

                 print(f"[{minus}] %s No NameServer Found for {yellow}{target}{end}"%(red))
        except subprocess.CalledProcessError:
            print(f"[{minus}] %s No NameServer Found for {yellow}{target}{end}"%(red))
        except :
            print(f"[{minus}] %s No NameServer Found for {yellow}{target}{end}"%(red))



#remove deuplicate from files
lines = set()
outfile = open('ns.txt', "w")
for line in open('ns.txt', "r"):
    if line not in lines:
        outfile.write(line)
        lines.add(line)
outfile.close()



def zoneXFR(target):
    file = open('ns.txt','r')
    name_server = [i.rstrip('\n') for i in file.readlines() ]
    for target in urls:

        for server in name_server:
            if None:
                print('No NameServers Present in ns.txt file')
            else:
                try :
                        query = dns.zone.from_xfr(dns.query.xfr(server ,target,timeout=5,lifetime=6))
                        node = query.nodes.keys()
                        for i in node:
                            axfr = query[i].to_text(i)

                        print(f"{green} [+]{end} {red}vulnerabilty {end}Discovered for {yellow} {server}{end} at {yellow} {target}{end} ")
                #Error Handling
                except  ConnectionResetError :
                    print(f"[{minus}] %s No vulnerabilty Discovered for  {yellow}{server} at {target}{end}"%(red))
                except ConnectionResetError:
                    print(f"[{minus}] %s No vulnerabilty Discovered for  {yellow}{server} at {target}{end}"%(red))
                except  ConnectionResetError :
                    print(f"[{minus}] %s No vulnerabilty Discovered for  {yellow}{server} at {target}{end}"%(red))
                except dns.exception.Timeout  :
                    print(f"[{minus}] %s No vulnerabilty Discovered for  {yellow}{server} at {target}{end}"%(red))
                except  dns.exception.FormError :
                    print(f"[{minus}] %s No vulnerabilty Discovered for  {yellow}{server} at {target}{end}"%(red))
                except  dns.exception.SyntaxError :
                    print(f"[{minus}] %s No vulnerabilty Discovered for  {yellow}{server} at {target}{end}"%(red))
                except socket.gaierror:
                    print(f"[{minus}] %s No vulnerabilty Discovered for  {yellow}{server} at {target}{end}"%(red))
            time.sleep(0.1)

#saving nameserver
DnsResolve(urls)

#zonetransfer
zoneXFR(target)
