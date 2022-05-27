from django.shortcuts import render
from django.http import HttpResponse

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid,low,high

    # If we reach here, then the element was not present
    return -1,low,high



# Test array



def index_render(request):
    x = None
    search_id = None
    endlist = []
    if request.method == 'POST':
        x = request.POST.get('x[]')
        x = int(x)

        search_id = request.POST.get('array[]')

        search_id = search_id.split(',')


        for i in search_id:
            try:
                i = int(i)
                endlist.append(i)
            except ValueError:
                message = "No array"
                return message


    arr = endlist

    # Function call
    result,low,high = binary_search(arr, x)





    if result != -1:
        ms = "Element is present at index", str(result), "the low is", str(low), "the high is", str(high)
        ms = str(ms)
        ms = ms.replace("'","")
        print(ms)

    else:
        ms = "Element is not present in array"

    context = {"message": ms}


    return render(request,'index.html',context)