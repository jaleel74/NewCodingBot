set1={1,3,5,7,9}
set2={0,2,4,6,8}
union=set1|set2
print(union)

set1={1,3,5,7,9}
set2={0,2,4,6,8}
set3={1,2,3,4,5,6,7,8,9}
union=set1|set2
print(union)
intersection=set1&set3
print(intersection)

set1={1,3,5,7,9}
set2={0,2,4,6,8}
set3=set1.difference(set2)
print(set3)