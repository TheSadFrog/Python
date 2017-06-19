# coding=UTF-8
"""
用字典暴力破解ZIP压缩文件密码
"""
import zipfile
import optparse
from threading import Thread
def extractFile(zFile, password):
    try:
		#3.x 版本必须加上.encode('ascii')，3.x版本不能自动支持ascii码了
        zFile.extractall(pwd=password.encode('ascii'))
        print("[+] Found password " + password + "\n")
    except:
        pass
def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")
    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")
    (options, args) = parser.parse_args()
    if(options.zname == None ) |(options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile,args=(zFile, password))
        t.start()

if __name__ == "__main__":
    main()