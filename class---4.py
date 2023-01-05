#create a list of prime numbers
prime_numbers =[1,4,2,0,1,3]
#reverse the order of list elements
prime_numbers.reverse()                  # reverse ()
print("reversed list:", prime_numbers)

#sort
m =[14,20,13,26,19,200,199]
m.sort()
print(m)

v =["vive","krushi","manu","manja"]
v.sort()
print(v)

k = [11,14,20,26,13,28,44,89,96,100,]
k.sort(reverse = True)
print(k)

#a=[1,2,3,4,5,6,7,8,9,10,"v"]
#a.soet()                      note: not supported between of 'str' and 'int'
#print(a)

#sorted()
m=[11,24,36,3,5,4,9,8,26,14]
print(sorted(m))

#reversed:
v =[11,14,25,3,58,86,2,1,6,98,]
reverse_object = reversed (v)
for r in reverse_object:
    print(r)

#tuple:
p=(14,20,26,50,40,)
for v in p:
    print(v)
#delete tuple using,del tuple_name
#k=(11,22,33,44,)
#del k
#print(k)

#creat tuple:
v=11,14,20,26,     # note: we can write also tuple     
print(v)
p=()
print(p) #note: this is empty tuple.
k=14,
print(k)       # note: this is tuple (comma is given)

#methodes on tuple
k=tuple([1,12,14,15,63,3,8,47,20,26.45,])
print(k)
print(len(k))
print(k.count(6))
print(k.index(14))
k_sorted=sorted(k)
print(k_sorted)
print(min(k))
print(max(k))

# tuple packing:
v=14
k=20
m=26
j=13
p = v,k,m,j
print(p)

# tuple unpacking:
m,k,v,j,= p
print(m)
print(k)
print(v)
print(j)
print(p)

#create dictionary:

s={}     #this is empty dictionary
print(s)
d={'key'}
print(d)
d={100:'manu'}
print(d)
d[102] = "krushi"
print(d)
for key,value in d.items():
    print(key,value)
k={1:2,3:4,5:6,7:8,9:5}
print(k)
print(len(k))
print(d.get(4))
print(d.get(100,90))

