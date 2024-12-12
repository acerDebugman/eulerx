/*
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:
输入: numRows = 1
输出: [[1]]
*/

struct Solution;
impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
            
    }
}

pub fn main() {
    //let nums = vec![1,2,3,4];    
    //println!("{:?}", nums);
    let n = 5;
    let ans = Solution::generate(n);
    println!("ans: {:?}", ans);
}

