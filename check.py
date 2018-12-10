import os
import sys
import dns.resolver

class subdomaintakeover:
    def __init__(self,filename):
        self.filename=filename

    def check(self,domain):
        try:
            print("Check {domain}".format(domain=domain))
            ans = dns.resolver.query(domain, 'a')
        except:
            print("[+]find vul --->{vuldomain}".format(vuldomain=domain))
            with open("result.txt","a") as w:
                w.write(domain+"\n")
            return 0
        for i in ans.response.answer:
            for j in i.items:
                if isinstance(j, dns.rdtypes.IN.A.A):
                    return 0
                if isinstance(j, dns.rdtypes.ANY.CNAME.CNAME):
                    self.check(j.to_text())
                return 0

    def run(self):
        with open(self.filename, 'r') as f:
            for i in f.readlines():
                self.check(i.strip())

if __name__ == "__main__":
    try:
        filename=sys.argv[1]
    except:
        print('''
        Usage: 
            python check.py domainfile.txt
        ''')
        sys.exit()
    if os.path.exists("result.txt"):
        sys.stdout.write("result.txt exists, Do u want to replace it? [Y/n]:")
        scantype = sys.stdin.readline()
        if scantype=="n":
            print("Bye")
        else:
            os.remove("result.txt")
            subdomaintakeover(filename=filename).run()
    else:
        subdomaintakeover(filename=filename).run()
