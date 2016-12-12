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
from subDomainsBrute.subDomainsBrute import xxx
class Domainscan:
    def __init__(self, domain):
        self.domain = domain
        self.subset = []

    def run(self):
        list = []
        try:
            list1 = Alexa(domain=self.domain).run()
            list2 = Chaxunla(domain=self.domain).run()
            list3 = Threatminer(domain=self.domain).run()
            list4 = Threatcrowd(domain=self.domain).run()
            print "start list5"
            list5 = Sitedossier(domai=self.domain).run()
            print "start list6"
            list6 = Netcraft(domain=self.domain).run()
            list7 = Ilinks(domain=self.domain).run()
            list8 = Chaxunla(domain=self.domain).run()
            list9 = TransparencyReport(domain=self.domain).run()
            print "list10 start"
            m=xxx()
            list10 = SubNameBrute(target=self.domain,options=m).run()
            print list10
            _ = chain(list1,list2,list3,list4,list5,list6,list7,list8,list9,list10)

            for i in _:
                if i not in list:
                    list.append(i)
            print list
        except Exception as e:
            return self.subset


if __name__ == '__main__':
    reslut = []
    result =  Domainscan(domain='swpu.edu.cn')
    re = result.run()


