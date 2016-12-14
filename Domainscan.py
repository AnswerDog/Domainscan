from module.fileutils import FileUtils

from module.alexa import Alexa
from module.threatminer import Threatminer
from module.threatcrowd import Threatcrowd
from module.sitedossier import Sitedossier
from module.netcraft import Netcraft
from module.ilinks import Ilinks
from module.chaxunla import Chaxunla
from module.googlect import TransparencyReport
from itertools import chain
from subDomainsBrute.subDomainsBrute import SubNameBrute
import optparse
import sys
class Domainscan:
    def __init__(self, domain,options):
        self.domain = domain
        self.subset = []
        self.options = options

    def run(self):
        list = []
        try:
            print "start Alexa"
            list1 = Alexa(domain=self.domain).run()
            print list1
            print "start Chaxunla"
            list2 = Chaxunla(domain=self.domain).run()
            print list2
            print "start Threatminer"
            list3 = Threatminer(domain=self.domain).run()
            print list3
            print "start Threatcrowd"
            list4 = Threatcrowd(domain=self.domain).run()
            print list4
            print "start Sitedossier"
            list5 = Sitedossier(domain=self.domain).run()
            print list5
            print "start Netcraft"
            list6 = Netcraft(domain=self.domain).run()
            print list6
            print "start Ilinks"
            list7 = Ilinks(domain=self.domain).run()
            print list7
            print "start TransparencyReport"
            list8 = TransparencyReport(domain=self.domain).run()
            print list8
            print "list10 start"
            list9 = SubNameBrute(target=self.domain,options=self.options).run()
            print list9
            _ = chain(list1,list2,list3,list4,list5,list6,list7,list8,list9)

            for i in _:
                if i not in list:
                    list.append(i)
            if self.options.output:
                outfile = options.output
            else:
                outfile = self.domain + '_all.txt' if not options.full_scan else self.domain + '_all.txt'
                outhtml = self.domain + '_all.html' if not options.full_scan else self.domain + '_all.html'
            self.outfile = open(outfile, 'w')
            self.outhtml = open(outhtml, 'w')
            for _list in list:
                self.outfile.write(_list+'\n')
                self.outhtml.write("<a href=http://"+_list+">"+_list+"</a></br>"+'\n')
                self.outhtml.flush()
                self.outfile.flush()
            self.outfile.close()
            self.outhtml.close()
        except Exception as e:
            return self.subset



if __name__ == '__main__':
    parser = optparse.OptionParser('usage: %prog [options] target.com', version="%prog 1.0.3")
    parser.add_option('--full', dest='full_scan', default=False, action='store_true',
              help='Full scan, a large NAMES FILE will be used during the scan')
    parser.add_option('-i', '--ignore-intranet', dest='i', default=False, action='store_true',
              help='Ignore domains pointed to private IPs')
    parser.add_option('-o', '--output', dest='output', default=None,
              type='string', help='Output file name. default is {target}.txt')
    print parser
    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        sys.exit(0)

    d = Domainscan(domain=args[0], options=options)
    d.run()


