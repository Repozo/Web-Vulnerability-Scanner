global resultPorts
resultPorts=['sample']
resultPorts.clear()
def portscan(port,target):
    import threading
    import socket
    #dictionary of common ports and services
    commonPortsDict={
        21:"21:ftp",
        22:"22:ssh",
        23:"23:telnet",
        25:"25:smtp",
        53: "53:domain name system",
        80: "80:http",
        110: "110:pop3",
        111: "111:rpcbind",
        135: "135:msrpc",
        139: "139:netbios-ssn",
        143: "143:imap",
        389:"389:LDAP",
        443: "443:https",
        445: "445:microsoft-ds",
        993: "993:imaps",
        995: "995:pop3s",
        1723: "1723:pptp",
        3306: "3306:mysql",
        3389: "3389:ms-wbt-server",
        5900: "5900:vnc",
        8080: "8080:http-proxy"
    }
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) 
    try:
        con = s.connect((target,port))
        resultPorts.append(commonPortsDict[port])
        con.close()
    except: 
        pass
def portScanner2(fullip):
    import threading
    import socket
    resultPorts.clear()
    #list of common ports
    commonPorts=[21,22,23,25,53,80,110,111,135,139,143,389,443,993,995,1723,3306,3389,5900,8080]
    for x in commonPorts:
         t = threading.Thread(target=portscan,kwargs={'port':x,'target':fullip})     
         t.start()
    t.join()
    return resultPorts



