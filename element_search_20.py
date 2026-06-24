a = [1, 3, 5, 30, 42, 43, 500]
ip = int(input("Enter a number: "))

def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        print("Element not found.")
        return

    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found!")
    elif arr[mid] > target:
        binary_search(arr, target, low, mid - 1)
    else:
        binary_search(arr, target, mid + 1, high)

binary_search(a, ip)