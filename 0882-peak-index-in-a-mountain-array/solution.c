int peakIndexInMountainArray(int* arr, int arrSize) 
{
    int left = 0, right = arrSize - 1, mid = 0;

    while (left < right)
    {
        mid = left + (right-left)/2;
        if (arr[mid] < arr[mid+1])
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }    
    return right;
}
