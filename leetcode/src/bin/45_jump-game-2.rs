/*
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，
你可以跳转到任意 nums[i + j] 处:
    0 <= j <= nums[i] 
    i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

示例 1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:
输入: nums = [2,3,0,1,4]
输出: 2
*/

struct Solution;
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return 0;
        }
        let (mut last_max_step, mut max_step, mut min_cnt) = (nums[0] as usize, nums[0] as usize, 1);
        for i in 1..nums.len() {
            if i > max_step {
                return 0;
            }
            max_step = std::cmp::max(max_step, nums[i] as usize + i);
            if i == last_max_step && last_max_step < nums.len() - 1{
                min_cnt += 1;
                last_max_step = max_step;
                if max_step >= nums.len() - 1 {
                    println!("??{:?}, {}, {}", last_max_step, max_step, min_cnt);
                    return min_cnt;
                }
            }
        }
        return min_cnt
    } 
}


pub fn main() {
    let nums = vec![2,3,1,1,4];
    let nums = vec![3,2,1,0,4];
    //let nums = vec![2,0,0];
    //let nums = vec![0];
    //let nums = vec![1,2];
    //let nums = vec![7,0,9,6,9,6,1,7,9,0,1,2,9,0,3];
    //let nums = vec![2,3,1,1,4];
    println!("{:?}", nums);
    let ans = Solution::jump(nums);
    println!("ans: {:?}", ans);
}

