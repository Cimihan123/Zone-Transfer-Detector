def url_list(target,wordlist):
    urls = []
    if wordlist:
        with open(wordlist, 'r') as file:
            for line in file:
                if line.startswith(('http://', 'https://')):
                    urls.append(line.rstrip('\n'))
                else:
                    urls.append(line.rstrip('\n'))
                
    if target:
        target = target[0]
        if target.startswith(('http://', 'https://')):
            urls.append(target.rstrip('\n'))
        else:
            urls.append(target.rstrip('\n   '))

      
    
    return urls 