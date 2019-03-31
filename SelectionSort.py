


a = [7 , 1, 2 ,5 ,4]

#lenght of Array
print("length" ,len(a))

for i in range(0 ,len(a)):
    print(i ," ")

    # lets consider first number in unsorted array is minimum 
    minimum = i
   
    #get minumum from unsorted element
    for j in range(i+1 , len(a)):

        if(a[j]<a[minimum]):
            minimum = j

    #swap two element
    temp = a[i]
    a[i] = a[minimum]
    a[minimum] =temp

    #print(a)
print(a)
