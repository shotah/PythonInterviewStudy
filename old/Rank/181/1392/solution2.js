/**
 * https://leetcode-cn.com/problems/longest-happy-prefix/
 * 
 * 1392. 最长快乐前缀
 * 
 * Hard
 * 
 * 96ms 100.00%
 * 45.4mb 100.00%
 */
const longestPrefix = s => {
  const max = s.length;
  const next = makeNext(s);
  if (max > 0) {
    return s.slice(0, next[max - 1])
  }
  return '';
}

function makeNext(str) {
  let index = 1; // 当前子字符串的结束下标
  let k = 0; // 最长公共前后缀的长度
  const len = str.length;
  const next = Array(len).fill(0);
  for (;index < len; index += 1) {
    while (k > 0 && str[index] !== str[k]) {
      // 递归向前查找最大公共子串
      k = next[k - 1];
    }
    if (str[index] === str[k]) {
      k++;
    }
    next[index] = k;
  }
  return next;
}