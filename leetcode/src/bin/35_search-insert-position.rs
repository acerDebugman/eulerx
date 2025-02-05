/*
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4
*/

struct Solution;
impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let (mut s, mut e) = (0, nums.len() as i32 - 1);
        let mut found = false;
        while s <= e {
            let mid = s + (e-s)/2;
            if nums[mid as usize] == target {
                found = true;
                return mid;
            }
            if target > nums[mid as usize] {
                s = mid + 1; 
            } else {
                e = mid - 1;
            }
        }
        return s;
    }
    pub fn search_insert2(nums: Vec<i32>, target: i32) -> i32 {
        let (mut s, mut e) = (0, nums.len() as i32 - 1);
        if target <= nums[s as usize] {
            return s;
        }
        if target > nums[e as usize] {
            return e+1;
        }
        while s < e {
            let mid = s + (e - s)/2; 
            if nums[mid as usize] == target {
                return mid;
            }
            if target > nums[mid as usize] {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        if target > nums[s as usize] {
            return s + 1;
        }
        return s;
    }
}

pub fn main() {
    let nums = vec![1,3,5,7];
    let target = 8;
    //let nums = vec![1,3,5,6];
    //let target = 0;
    //let nums = vec![1,3];
    //let target = 2;
    println!("{:?}, {}", nums, target);
    let ans = Solution::search_insert(nums, target);
    println!("ans: {:?}", ans);
}

