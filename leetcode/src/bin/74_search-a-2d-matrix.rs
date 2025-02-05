/*
给你一个满足下述两条属性的 m x n 整数矩阵：每行中的整数从左到右按非严格递增顺序排列。每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
 
示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
*/

struct Solution;
impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let m = matrix.len() as i32;
        if m == 0 {
            return false;
        }
        let n = matrix[0].len() as i32;
        let (mut s, mut e) = (0, m * n - 1);
        while s <= e {
            let mid = s + (e - s)/2;
            let v = matrix[(mid/n) as usize][(mid % n) as usize];
            if v == target {
                return true;
            }
            if target > v {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        false
    }
}

pub fn main() {
    let matrix = vec![vec![1,3,5,7],vec![10,11,16,20],vec![23,30,34,60]];
    let target = 60;
    println!("{:?}, {}", matrix, target);
    let ans = Solution::search_matrix(matrix, target);
    println!("ans: {:?}", ans);
}

