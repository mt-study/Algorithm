from typing import List


def count_intervals(a: List[int], x: int) -> int:
    n = len(a)
    prefix_xor = 0
    count = 0
    prefix_count = {0: [-1]}  # 用于存储前缀异或及其对应的最后索引

    for i in range(n):
        prefix_xor ^= a[i]  # 计算当前前缀异或

        # 计算需要的目标前缀异或
        target = prefix_xor ^ x

        # 检查哈希表中是否有目标前缀异或
        if target in prefix_count:
            # 遍历之前记录的索引
            for idx in prefix_count[target]:
                if (i - idx) % 2 == 0:  # 确保区间长度为偶数
                    count += 1

        # 更新哈希表
        if prefix_xor not in prefix_count:
            prefix_count[prefix_xor] = []
        prefix_count[prefix_xor].append(i)
    return count
    # 示例
print(count_intervals([1, 2, 3, 2, 1], 2))
