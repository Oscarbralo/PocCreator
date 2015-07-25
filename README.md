# PocCreator
POC creator for GET and POST request.


YOu only need to edit the script, then choose the output folder, and add the request taked form for example, Burp or Fiddler, like in this example:

POST /create_account.php HTTP/1.1
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

    email=email.com&masterpassword=XXXXXXXXX&passwordreminder=ss&timezone=%2B01%3A00%2C0&language=en-US&loglogins=on&improve=on&json=1&website=1&iterations=5000


and then we will get in the output folder, two html files, one for GET and one for POST requests. Inside this files we will have a simple html and <form> tag, with hidden fields and a javascript to run this form.