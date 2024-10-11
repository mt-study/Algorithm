# 算法学习
## 动态规划
用结果来表示，往回去走，最后得到一个表达式fn 和 fn-1的关系……
## 滑动窗口
双指针 i 和 j 表示开始和结束

算法特点：不重复遍历，i的向右移动，j也是向右移动，一单走过就再也不会再走，所以算法时间缩减
相较于一般，向右遍历，重复遍历到最后，算法时间浪费

# 编程语言的查漏补缺

## (一) python

### 1. 大小写转化
`s.lower()`

`s.upper()`
### 2. 生成指定 x × y 尺寸的列表
`
[[[] for _ in range(3)] for _ in range(3)]
`
### 3. 数组删除指定元素
`list.remove('a')`
### 4. 统计列表中元素以及频率
`collections.Counter(list)`
### 5. 列表入栈和出栈
`list.append()`
`list.pop()`
### 6. 列表中间隔选取
`list[x::y]`
x为开始的地址，y是间隔数
### 7. 绝对值
`abs()`
### 8.数组的初始化
**m * n**

`flag=[[0] *n for _ in range(m)]`
### 9.set方法
可以将字符转成数组

去重

例如 "egg" 变 ['e','g'']

### 10.二维数组的排序
按照第一个排序`sorted(intervals)`

按照第二个排序`sorted(array, key=lambda x: x[1])`
