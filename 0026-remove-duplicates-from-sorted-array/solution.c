int removeDuplicates(int* nums, int numsSize) 
{
    int trailer, leader;

    trailer = 0;
    for (leader = 1; leader<numsSize; leader++)
    {
        if (nums[trailer]<nums[leader])
        {
            trailer++;
            nums[trailer] = nums[leader];
        }
    }
    return trailer +1 ;
}
