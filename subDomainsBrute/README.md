# subDomainsBrute 1.0.3

A simple and fast sub domain brute tool for pentesters. It can rearch as fast as 1000 DNS queries per second.

这个脚本的主要目标是发现其他工具无法探测到的域名, 如Google，aizhan，fofa。高频扫描每秒DNS请求数可超过1000次。

##Change Log (Nov 9, 2016)
* Time performance optimization
* Placeholder {alphnum} {alpha} {num} could be used in Names File

##Dependencies
First you need to install [dnspython](http://www.dnspython.org/kits/1.12.0/) to do DNS query
> pip install dnspython


##Usage


	Usage: subDomainsBrute.py [options] target.com
	
	Options:
	  --version             show program's version number and exit
	  -h, --help            show this help message and exit
	  --full                Full scan, a large NAMES FILE will be used during the scan
	  -i, --ignore-intranet
	                        Ignore domains pointed to private IPs
	  -o OUTPUT, --output=OUTPUT
	                        Output file name. default is {target}.txt


参数 `-t` 已经去掉了，想要设定并发线程的数量，请直接修改dict\dns_servers.txt文件中的行数即可。


##Screenshot
![screenshot](screenshot.png)

Output file could be like: [https://github.com/lijiejie/subDomainsBrute/blob/master/dict/sample_youku.com_full.txt](https://github.com/lijiejie/subDomainsBrute/blob/master/dict/sample_youku.com_full.txt)

LiJieJie my[at]lijiejie.com ([Blog](http://www.lijiejie.com))