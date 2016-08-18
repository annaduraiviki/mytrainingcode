


print False
print str(True)

x = (x **2 for x in range(20))
print x

x = list(x)
print x

colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)

x=[1,2,3,4]
x.extend([5,6])
print x
x.append([7,8])
print x

print "this is a string".split()

print "this is a string"
print sorted("this is a string".split())

print sorted("this Is a String".split())

print sorted("this Is a String".split(), key=lambda word: word.lower())
print str.lower("Hello")[::-1]
print sorted("this Is a String".split(), key=lambda word: word.lower()[::-1])


word="abcDzX"
print word.lower()[::-1]

#str=u'\xa56'
str='sgrh'
str.encode('ascii','ignore')
str.decode()

range(7)
['a','b','c','d','e','f','g']
range(0)
print range(0)
range(7)
['a','b','c','d','e','f','g']
print range(1)
print range(6)

(a,b,c,d)=range(4)
print range(d)
print b
print c

print sorted("hello this is sodexis".split())
print ("hello this is sodexis".split())
print ("hello this is sodexis")
print sorted("hey!, this is me".split())




