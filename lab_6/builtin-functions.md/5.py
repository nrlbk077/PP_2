def all_true(tup):
    return all(tup)

t = (True, 1, "hello", 5)  
print(all_true(t))  

t2 = (True, 0, "hello") 
print(all_true(t2))  

t3 = (True,False,"dfs","0")
print(all_true(t3))