// Given an array of integers, show indices of the two numbers such that they add up to a
// specific target. You can assume that each input would have exactly one solution, and you
// can not use the same element twice.

function twoSum(nums, target){
    // your code here
    size = 0
    for(i in nums){
        size += 1;
    }
    
    for(j = 0; j < size; j++){
        for( k = size - 1; k >= 0; k--){
            if ( nums[j] + nums[k] == target){
                return [j, k]
            }
        }
    }
}
    
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9