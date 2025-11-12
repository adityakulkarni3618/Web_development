m = int(input("Enter hash table size: "))
table = [[] for _ in range(m)] 

while True:
    ch = int(input("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit\nChoice: "))

    if ch == 1:  
        key = int(input("Key: "))
        
        i = key % m
        if key not in table[i]:
            table[i].append(key)
            print(f"Inserted {key} in bucket {i}")
        else:
            print("Key already exists!")

    elif ch == 2:  
        key = int(input("Key: "))
        i = key % m
        if key in table[i]:
            print(f"Found {key} in bucket {i}")
        else:
            print("Not found!")

    elif ch == 3:  
        key = int(input("Key: "))
        i = key % m
        if key in table[i]:
            table[i].remove(key)
            print("Deleted")
        else:
            print("Not found!")

    elif ch == 4: 
        for i in range(m):
            print(f"Bucket {i}: {table[i]}")

    elif ch == 5: 
        break

    else:
        print("Invalid choice!")