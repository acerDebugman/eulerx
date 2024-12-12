/*
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。

示例 2：
输入：s = "eccbbbbdec"
输出：[10]
*/

struct Solution;
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut pos_map = std::collections::HashMap::<char, usize>::new();
        for (i, c) in s.chars().enumerate() {
            pos_map.insert(c, i);
        }
        //println!("{:?}", pos_map);
        let mut rs = vec![];
        let (mut start, mut end) = (0, 0);
        for (i, c) in s.chars().enumerate() {
            //println!("{:?}", c);
            end = end.max(*pos_map.get(&c).unwrap());
            if i == end {
                rs.push((i-start+1) as i32 );
                start = end + 1; 
            }
        }
        rs
    }
}

pub fn main() {
    let s = "ababcbacadefegdehijhklij".to_owned();
    let s = "eccbbbbdec".to_owned();
    println!("{:?}", s);
    let ans = Solution::partition_labels(s);
    println!("ans: {:?}", ans);
}

