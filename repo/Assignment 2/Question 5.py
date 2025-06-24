list1 = [10,2,8,17,23]
smallest = min(list1)
print("Smallest no in list: ",smallest)
first = list1[0]
sec = list1[0]
for i in range(len(list1)):
    if list1[i]>first:
        sec = first
        first = list1[i]
    elif first > list1[i] > sec:
        sec = list1[i]
print("\nSecond greatest no in list: ",sec)
first = list1[0]
sec = list1[0]
for i in range(len(list1)):
    if list1[i]< first:
        sec = first
        first = list1[i]
    elif first<list1[i]<sec:
         sec = list1[i]
print("\n Second smallest: ",sec)