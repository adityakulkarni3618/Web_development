arr = [int(x) for x in input("Enter array elements: ").split()]
arr = sorted(arr)

key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print(f"Element {key} found at position {mid}")
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"Element {key} not found in list")