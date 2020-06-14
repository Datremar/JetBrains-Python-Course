text = input().split()

domains = ('https://', 'http://', 'www.')

for el in text:
    if el.lower().startswith(domains[0]) or el.lower().startswith(domains[1]) or el.lower().startswith(domains[2]):
        print(el)
