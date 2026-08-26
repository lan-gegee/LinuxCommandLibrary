# TAGLINE

生成用于密码破解的彩虹表

# TLDR

**生成彩虹表**

```rtgen [hash_algorithm] [charset] [min_len] [max_len] [table_index] [chain_len] [chain_num] [part_index]```

**生成 MD5 表**

```rtgen md5 loweralpha 1 7 0 2400 67108864 0```

**生成 NTLM 表**

```rtgen ntlm numeric 1 8 0 2400 67108864 0```

**对表排序**

```rtsort [table.rt]```

# SYNOPSIS

**rtgen** _algorithm_ _charset_ _min_ _max_ _index_ _chain_len_ _chain_num_ _part_

# PARAMETERS

**algorithm**
> 哈希类型（md5、sha1、ntlm、lm）。

**charset**
> 字符集（loweralpha、numeric 等）。

**min_len**
> 最小密码长度。

**max_len**
> 最大密码长度。

**table_index**
> 生成多张表时使用的表索引。

**chain_len**
> 规约链（reduction chain）的长度。

**chain_num**
> 链的数量。

**part_index**
> 分片索引。

# DESCRIPTION

**rtgen** 用于生成密码破解所需的彩虹表。彩虹表是对密码学哈希函数进行逆向运算的预计算表。它是 RainbowCrack 工具集的一部分。

# EXAMPLES

```bash
# Generate MD5 lowercase table
rtgen md5 loweralpha 1 7 0 2400 67108864 0

# NTLM numeric
rtgen ntlm numeric 1 8 0 2400 33554432 0

# Sort generated table
rtsort md5_loweralpha#1-7_0_2400x67108864_0.rt

# Use with rcrack
rcrack . -h 5d41402abc4b2a76b9719d911017c592
```

# CHARSETS

```
numeric           - 0-9
loweralpha        - a-z
alpha             - a-zA-Z
loweralpha-numeric - a-z0-9
mixalpha-numeric  - a-zA-Z0-9
```

# CAVEATS

极度消耗存储空间。生成过程耗时较长。仅限授权的安全测试使用。属于 RainbowCrack 项目。

# HISTORY

rtgen 是 **Zhu Shuanglei** 开发的 **RainbowCrack** 的组成部分，实现了 Philippe Oechslin 提出的更快速的时间-内存权衡技术。

# SEE ALSO

[rcrack](/man/rcrack)(1), [john](/man/john)(1), [hashcat](/man/hashcat)(1)
