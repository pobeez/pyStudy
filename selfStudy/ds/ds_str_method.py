name = "Moon Sungjin"

if name.startswith("Moon"):
    print("name start with 'Moon")

if 'j' in name:
    print('name contains \'j\'')

cont = 'Park'
print(name.find(cont))
if name.find(cont) == 1:
    print('name contains \'', cont, '\'')
else:
    print('name does not contain \'', cont, '\'')

delemeter = '_+_'

mycountries = ['china', 'japan', 'taipei', 'korea', 'north korea']

print(delemeter.join(mycountries))
