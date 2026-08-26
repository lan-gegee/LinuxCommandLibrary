# TAGLINE

操作由 ipaggcreate 创建的 IP 地址聚合文件

# TLDR

**读取聚合文件并按计数排序输出**

```ipaggmanip -r [input.agg] --sorted-counts```

**合并（求并集）多个聚合文件**

```ipaggmanip --or [file1.agg] [file2.agg] -o [combined.agg]```

**重新聚合成更短的前缀长度（例如 /16）**

```ipaggmanip --prefix [16] -r [input.agg]```

**丢弃少于 N 个数据包的标签**

```ipaggmanip --cut-smaller [100] -r [input.agg]```

**以带 IP 地址的 ASCII 输出**

```ipaggmanip --ip -r [input.agg]```

**统计活跃标签数量**

```ipaggmanip --num-labels -r [input.agg]```

# SYNOPSIS

**ipaggmanip** [_options_] [_files_]

# PARAMETERS

**-r**, **--read-file** _FILE_
> 从 FILE 读取聚合数据（默认：stdin）。

**-o**, **--output** _FILE_
> 将结果写入 FILE（默认：stdout）。

**-b**, **--binary**
> 以二进制格式输出。

**-A**, **--text**
> 以 ASCII 文本格式输出。

**--ip**
> 以 ASCII 输出，用 IP 地址代替原始整数标签。

**-p**, **--prefix** _P_
> 重新聚合到前缀级别 P（例如 16 表示 /16）。

**-P**, **--posterize**
> 将所有非零计数替换为 1。

**--sample** _N_
> 以 1/N 的概率随机采样数据包。

**--cut-smaller** _N_
> 丢弃少于 N 个数据包的标签。

**--cut-larger** _N_
> 丢弃 N 个及以上数据包的标签。

**-n**, **--num-labels**
> 打印活跃标签的数量。

**--counts**
> 按标签顺序输出计数。

**--sorted-counts**
> 按降序输出计数。

**-e**, **--each**
> 分别处理每个输入文件。

**--or**
> 通过累加聚合来合并输入文件（并集）。

**--and**
> 合并输入，仅保留所有文件共有的标签。

**--minus**
> 保留 FILE1，丢弃其他文件中也存在的标签。

**--xor**
> 仅保留恰好出现在一个文件中的标签。

# DESCRIPTION

**ipaggmanip** 操作由 **ipaggcreate** 创建的 IP 地址聚合文件。它可以合并多个聚合文件、按阈值过滤、以不同参数重新聚合，并在不同格式之间转换。

该工具补全了 ipsumdump 套件的网络流量分析工作流：用 **ipsumdump** 抓取，用 **ipaggcreate** 聚合，再用 **ipaggmanip** 操作和分析。

# CAVEATS

输入文件必须是 ipaggcreate 生成的 ipagg 格式。合并使用不兼容聚合参数的文件可能产生意外结果。

# HISTORY

Eddie Kohler 开发的 **ipsumdump** 软件包的一部分。专为大规模网络测量研究设计，用于跨多个数据源进行流量汇总与分析。

# SEE ALSO

[ipsumdump](/man/ipsumdump)(1), [ipaggcreate](/man/ipaggcreate)(1), [tcpdump](/man/tcpdump)(1)
