import optparse
import socket

parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
parser.add_option('-H',
                  dest='tgtHost',
                  type='string',
                  help='specify target host'
                  )

parser.add_option('-p',
                  dest='tgtPort',
                  type='int',
                  help='specify target port'
                  )

(options, args) = parser.parse_args()

tgtHost = options.tgtHost
tgtPort = options.tgtPort

if tgtHost is None or tgtPort is None:
    print parser.usage
    exit(0)


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print '[+]%d/tcp open' % tgtPort
        connSkt.close()
    except: # fix bare exception!!!!!!!!!!!!
        print '[-]%d/tcp closed' % tgtPort


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except: # here too
        print "[-] Cannot resolve '%s': Unknown host" % tgtHost
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print '\n[+] Scan results for: %s' % tgtName[0]
    except: # make it stop!
        print '\n[+] Scan results for: %s' % tgtIP
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print 'Scanning port %d' % tgtPort
        connScan(tgtHost, int(tgtPort))
