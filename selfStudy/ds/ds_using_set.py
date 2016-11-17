bri = set(['brazil', 'russia', 'india'])

print('india' in bri)
print('korea' in bri)

bric = bri.copy()
bric.add('china')
bric.issuperset(bri)

bri.remove('russia')
print(bri & bric)
print(bri | bric)

bri2= bri | bric

print(bri2)
