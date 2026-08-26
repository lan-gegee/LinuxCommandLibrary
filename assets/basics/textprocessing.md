# 文本处理

## 替换文本
**sed** 对每一行应用编辑命令。替换命令 **s/old/new/** 替换每行的第一个匹配项；**g** 替换所有匹配项，**I** 不区分大小写。**-i** 直接修改文件本身，而不是打印结果。
```[sed](/man/sed) 's/old/new/g' [file]```
```[sed](/man/sed) -i 's/old/new/g' [file]```
```[sed](/man/sed) -i 's/old/new/gI' [file]```

**sd** 以更简单的语法完成同样的工作，且默认使用正则表达式。
```[sd](/man/sd) "old" "new" [file]```

s 命令可以用任意字符作分隔符：**s|/usr/bin|/usr/local/bin|** 避免了对路径中的斜杠进行转义。

## 删除或打印特定行
**d** 删除匹配的行；**-n** 配合 **p** 只打印选中的行。地址可以是模式、行号或范围。
```[sed](/man/sed) '/pattern/d' [file]```
```[sed](/man/sed) -i '/^$/d' [file]```
```[sed](/man/sed) -n '5,10p' [file]```
```[sed](/man/sed) -n '/pattern/p' [file]```

## 提取字段
**awk** 把每行拆分为字段：**$1** 是第一个字段，**$0** 是整行，**NR** 是行号。**-F** 把字段分隔符从空白改为其他字符。
```[awk](/man/awk) '{print $1}' [file]```
```[awk](/man/awk) -F: '{print $1, $3}' /etc/passwd```
```[awk](/man/awk) '{print NR, $0}' [file]```

**cut** 是简单列提取场景下的轻量替代方案，可按分隔符（**-d**、**-f**）或字符位置（**-c**）提取。
```[cut](/man/cut) -d: -f1 [file]```
```[cut](/man/cut) -d',' -f1,3 [file]```
```[cut](/man/cut) -c1-10 [file]```

## 条件过滤
awk 程序的结构是 **condition { action }**：匹配条件的行会执行相应动作（默认动作：打印该行）。
```[awk](/man/awk) '$3 > 100' [file]```
```[awk](/man/awk) '/pattern/ {print $2}' [file]```
```[awk](/man/awk) 'NR>=5 && NR<=10' [file]```

用变量和 **END** 块跨行汇总统计。
```[awk](/man/awk) '{sum += $1} END {print sum}' [file]```
```[awk](/man/awk) '{sum += $1} END {print sum/NR}' [file]```

## 行排序
默认按字母顺序排序；**-n** 按数值排序，**-r** 反转顺序，**-u** 去除重复项，**-t** 和 **-k** 按指定字段排序。**-h** 能理解 2K、1G 这类人类可读的大小单位。
```[sort](/man/sort) [file]```
```[sort](/man/sort) -n [file]```
```[sort](/man/sort) -r [file]```
```[sort](/man/sort) -t: -k3 -n [file]```
```[sort](/man/sort) -u [file]```

## 查找重复行
**uniq** 只比较相邻的行，因此要先排序。**-c** 统计出现次数，**-d** 只显示重复的行，**-u** 只显示不重复的行。
```[sort](/man/sort) [file] | [uniq](/man/uniq)```
```[sort](/man/sort) [file] | [uniq](/man/uniq) -c | [sort](/man/sort) -rn```
```[sort](/man/sort) [file] | [uniq](/man/uniq) -d```

**sort | uniq -c | sort -rn** 管道是经典的频率统计器：按出现频率为每个不同的行排名。

## 转换或删除字符
**tr** 把一组字符映射为另一组，**-d** 删除字符，**-s** 把连续重复压缩为一个。
```[tr](/man/tr) 'a-z' 'A-Z' < [file]```
```[tr](/man/tr) -d '[:digit:]' < [file]```
```[tr](/man/tr) -s ' ' < [file]```
```[tr](/man/tr) '\n' ' ' < [file]```

## 比较文件
**diff -u** 是标准的补丁式比较；**-y** 并排显示两个文件；**cmp** 逐字节比较，最适合二进制文件。
```[diff](/man/diff) -u [file1] [file2]```
```[diff](/man/diff) -y [file1] [file2]```
```[cmp](/man/cmp) [file1] [file2]```

**comm** 用三列分别显示两个已排序文件各自独有的行以及共有的行。可以用数字屏蔽不需要的列。
```[comm](/man/comm) [file1] [file2]```
```[comm](/man/comm) -12 [file1] [file2]```

**comm** 和 **join** 都要求输入文件已排序。

## 合并文件
**paste** 逐行拼接多个文件；**-s** 把一个文件的所有行合并为一行。**join** 依据公共字段匹配两个文件的行，就像数据库的连接操作。
```[paste](/man/paste) [file1] [file2]```
```[paste](/man/paste) -d',' [file1] [file2]```
```[paste](/man/paste) -s [file]```
```[join](/man/join) [file1] [file2]```
```[join](/man/join) -t: -1 1 -2 3 [file1] [file2]```

## 格式化文本
把字段对齐成表格，或对长行折行。**fmt** 智能地重新排版段落，**fold** 在指定宽度处硬性截断（**-s** 在空格处断开）。
```[column](/man/column) -t [file]```
```[column](/man/column) -t -s',' [file]```
```[fmt](/man/fmt) -w 80 [file]```
```[fold](/man/fold) -s -w 80 [file]```

## 添加行号
**nl** 默认只给非空行编号；**-ba** 给所有行编号，效果如同 **cat -n**。
```[nl](/man/nl) [file]```
```[nl](/man/nl) -ba [file]```
```[cat](/man/cat) -n [file]```

## 计数
统计行数、单词数和字节数；**-m** 统计多字节编码下的字符数。
```[wc](/man/wc) [file]```
```[wc](/man/wc) -l [file]```
```[wc](/man/wc) -w [file]```
```[wc](/man/wc) -c [file]```

## 反转与打乱
**tac** 倒序打印文件（最后一行在最前），**rev** 反转每行的字符顺序，**shuf** 打乱行的顺序。
```[tac](/man/tac) [file]```
```[rev](/man/rev) [file]```
```[shuf](/man/shuf) [file]```
```[shuf](/man/shuf) -n 1 [file]```
