def domain_name(url):
    prefixes = ["https://", "http://", "www."]
    for prefix in prefixes:
        url = url.replace(prefix, "")       
    urllist = url.split(".")
    return urllist[0]