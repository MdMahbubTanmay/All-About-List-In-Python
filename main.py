main=["1","2","3","4","5"]
copy = main
copy[0]="Hello"
print(copy) #['Hello', '2', '3', '4', '5']
print(main) #['Hello', '2', '3', '4', '5']
#See on changing copy, the main is changing because here copy isnot the copy of main, rather its a referance
#so if we change any of them, another one will change. 
# so for copying one list to anotjer list, see line 60 and line 80 of this program









name=["1","2","3","4","5"] #list
search = "3"


print(name.index(search)) #Get the position of data in list



if search in name: # if data is in the list
    print("Found")   
else:
    print("Not Found")





#print spesific position of list  :  list_var[start_pos , end_pos , incriment]
print(name[::1]) #['1', '2', '3', '4', '5']
print(name[::2]) #['1', '3', '5']



# Size of list:
print(len(name))





#******************************************
#List Generate and print: list_var = [what_to_print  for  a_var in range(starting_value,less_than,incriment)  blank_or_a_condition]
gen = [i for i in range(0,5,1)]
print(gen) #[0, 1, 2, 3, 4]

gen1 = [i*i for i in range(0,5,2)]
print(gen1) #[0, 4, 16]

gen3 = [i for i in range(0,6,1) if(i%2==0)] #print only positive num
print(gen3) #[0, 2, 4]


#Copy one list into another usimg loop. We can use string method here
gen4 = [i for i in name] #Copy content of another list
print(gen4) #['1', '2', '3', '4', '5', '6', '7']








#****************Method In List*************


# convert string to list
import json #must include
h="[1,2,3]"
h = json.loads(h)
print(type(h))  # Still a list!
print(h) 


#we can also convert string to list like this
line = "1,2,3"
print(line.split(",")) #['1', '2', '3']
line = "1-2-3"
print(line.split("-")) #['1', '2', '3']




#add some list
name1=["6","7"]
name=name+name1
print(name)




# copy one list into another using method
main=["1","2","3","4","5"]
copy_list = main.copy()
print(copy_list) #['1', '2', '3', '4', '5']





# Replacing a position of list
colour=["red","green","blue"]
colour[1] = "Black"
print(colour) #['red', 'Black', 'blue']
colour[1] = 5 # we can also change data taypes of the position
print(colour) #['red', 5, 'blue']






lst = ["1","2","3","4","5"]
lst.append("6") #using append we can add only one item at the end of the list.  lst = lst + ["6"]
print(lst) #['1', '2', '3', '4', '5', '6']



#sorting list
lst2 = ["3","5","1","2","4"] #for number it will sort with small to big
lst3 = ["hi","hello","bye"] #for string it will sort with first letter. if first multiples bojcet has same first letter then it will check the second letter
lst2.sort()
lst3.sort()
print(lst2) #['1', '2', '3', '4', '5']
print(lst3) #['bye', 'hello', 'hi']



#Reverse List
rvs=["1","2","3","4","5"]
rvs.reverse()
print(rvs) #['5', '4', '3', '2', '1']





# Remove given data. if has same multiple data,it will remove the 1st one only
rmv = ["1","2","3","2"]
rmv.remove("2") 
print(rmv) #['1', '3', '2']



'''
Some More Methods :

list_var.count(data_name) ---> to count how much time the data_name object used in the list

list_var.insert(position,data) ---> to insert data in a position
'''
