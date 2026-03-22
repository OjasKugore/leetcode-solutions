void reverse(int* nums, int start, int end) {
    while (start < end) {
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}

void rotate(int* nums, int numsSize, int k) {
    if (numsSize <= 1) return;
    
    // Crucial: handle k larger than numsSize
    k %= numsSize;
    if (k == 0) return;

    // 1. Reverse the entire array
    reverse(nums, 0, numsSize - 1);
    
    // 2. Reverse the first k elements
    reverse(nums, 0, k - 1);
    
    // 3. Reverse the rest
    reverse(nums, k, numsSize - 1);
}
