import subprocess
def ping_test():
    return "OI"
    for ping in range(1,2):
        address = "127.0.0." + str(ping)
        res = subprocess.call(['ping', '-c', '3', address])
        result=""
        if res == 0:
            result+= "".join(["ping to",address,"OK"])
        elif res == 2:
            result+="".join(["no response from",address])
        else:
            result+= "".join(["ping to",address,"failed"])
    return(result)




