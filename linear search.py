arr = list(map(int, input("Enter elements of array separated by space: ").split()))
key = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print(f"Element {key} found at position {i}")
        found = True
        break

if not found:
    print(f"Element {key} not found")