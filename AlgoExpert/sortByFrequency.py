ini_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3,
               5, 5, 5, 4, 4, 4, 4, 4, 4]
 
# printing initial ini_list
print ("initial list", str(ini_list))
 
# sorting on bais of frequency of elements
result = sorted(ini_list, key = ini_list.count,
                                reverse = True)
 
# printing final result
print("final list", str(result))