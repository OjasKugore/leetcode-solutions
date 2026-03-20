int removeDuplicates(int* nums, int numsSize) 
{
    int trailer = 2, leader = 2, temp;

    if (numsSize < 2)
    {
        return numsSize;
    }

    for (leader; leader< numsSize; leader++)
    {
        if (nums[leader] > nums[trailer -2])
        {
            temp = nums[leader];
            nums[leader] = nums[trailer];
            nums[trailer] = temp;

            trailer ++;

        }
    }

    return trailer;
}
