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
        let mut rs = vec![vec![1]];
        if num_rows == 1 {
            return rs;
        }
        for i in 1..(num_rows as usize) {
            let mut new_v = vec![0;i+1];
            new_v[0] = 1; new_v[i]=1;
            let (mut s, mut e) = (1, i-1);
            
            while s < e {
                new_v[s] = rs[i-1][s-1] + rs[i-1][s];
                new_v[e] = rs[i-1][e-1] + rs[i-1][e];
                s+=1; e-=1;
            }
            if s == e {
                new_v[s] = rs[i-1][s-1] + rs[i-1][s];
            }
            
            rs.push(new_v); 
        }

        return rs 
    }
}

pub fn main() {
    //let nums = vec![1,2,3,4];    
    //println!("{:?}", nums);
    //let n = 1;
    let n = 10;
    let ans = Solution::generate(n);
    println!("ans: {:?}", ans);
}

