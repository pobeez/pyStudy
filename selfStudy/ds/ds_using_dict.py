ab = {
    'pobeez' : 'pobeez@gmail.com',
    'deall0200' : 'deall0200@gmail.com',
    't00133' : 't00133@lguplus.co.kr',
    'oscarm351' : 'oscarm351@naver.com'
}

print('pobeez mail address is', ab['pobeez'])

del ab['pobeez']

print('There ara {} contacts in the address book'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

ab['sua'] = 'sua@gmail.com'

if 'sua' in ab:
    print("\nsua's address is", ab['sua'])

