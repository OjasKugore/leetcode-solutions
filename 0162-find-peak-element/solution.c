int findPeakElement(int* nums, int numsSize) 
{
    int left = 0, right = numsSize -1, mid = 0;

    while (left < right)
    {
        mid = left + (right - left)/2;

        if (nums[mid] < nums[mid+1])
        {
            left = mid+1;
        }
        else
        {
            right = mid ;
        }
    }   
    return right; 
}
