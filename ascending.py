import operator
d={1:2,2:3,4:5,6:7,8:9,0:0,1:0}
print("Original dictionary:",d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print("Dictionary in acending order by value:",sorted_d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print("Dictionary in descending order by value:",sorted_d)
