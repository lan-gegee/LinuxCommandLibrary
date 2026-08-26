# TAGLINE

使用彩虹表破解密码哈希

# TLDR

**使用彩虹表破解单个哈希**

```rcrack [path/to/tables] -h [5d41402abc4b2a76b9719d911017c592]```

**从文件中破解哈希**

```rcrack [path/to/tables] -l [hashes.txt]```

从 pwdump 文件**破解 LM 哈希**

```rcrack [path/to/tables] -lm [pwdump.txt]```

从 pwdump 文件**破解 NTLM 哈希**

```rcrack [path/to/tables] -ntlm [pwdump.txt]```

**使用多个表目录**

```rcrack [tables1/] [tables2/] -h [hash]```

# SYNOPSIS

**rcrack** _table_path_ [_table_path_...] -h _hash_

**rcrack** _table_path_ -l _hash_file_

**rcrack** _table_path_ -lm _pwdump_file_

**rcrack** _table_path_ -ntlm _pwdump_file_

# PARAMETERS

**-h** _HASH_
> 破解单个哈希

**-l** _FILE_
> 从文件加载哈希（每行一个）

**-lm** _FILE_
> 从 pwdump 文件加载 LM 哈希

**-ntlm** _FILE_
> 从 pwdump 文件加载 NTLM 哈希

**-t** _DIR_
> 彩虹表目录

**-o** _FILE_
> 将破解出的密码写入输出文件

**-p** _NUM_
> 使用的线程数

**-s**
> 显示破解统计信息

**-u**
> 在破解出的密码旁显示用户名

# SUPPORTED ALGORITHMS

**lm**
> LAN Manager 哈希（最长 7 个字符）

**ntlm**
> NT LAN Manager 哈希（最长 15 个字符）

**md5**
> MD5 哈希（最长 15 个字符）

**sha1**
> SHA-1 哈希（最长 20 个字符）

**sha256**
> SHA-256 哈希（最长 20 个字符）

# DESCRIPTION

**rcrack** 是 RainbowCrack 项目推出的基于彩虹表的密码破解工具。它使用预先计算好的表执行时间-内存权衡攻击，从哈希值还原明文密码的速度远快于暴力破解。

彩虹表必须先用 **rtgen** 生成，再用 **rtsort** 排序。这些表编码了哈希计算链，可以快速查找与给定哈希匹配的密码。表文件的扩展名为 **.rt** 或压缩的 **.rtc**。

该工具对来自 Windows 系统的 LM 和 NTLM 哈希尤其有效。LM 哈希被拆分为两个 7 字符的一半，因此特别脆弱。NTLM 更强，但对于常见密码仍然容易受到彩虹表攻击。

# CAVEATS

彩虹表需要大量存储空间（GB 到 TB 级），并且必须与目标密码的哈希算法和字符集相匹配。加盐哈希无法用彩虹表破解。现代密码存储采用盐和慢速哈希函数（bcrypt、scrypt），正是为了抵御彩虹表攻击。只能在你拥有所有权或已获授权的系统上使用。

# HISTORY

RainbowCrack 由 **Zhu Shuanglei** 开发（基于 Philippe Oechslin 提出的彩虹表概念），于 **2003 年**前后首次发布。该项目展示了无盐密码哈希的现实危害，推动了密码存储实践的改进。该工具证明 LM 哈希可在几分钟内被破解，促使微软在 Windows Vista 中弃用了 LM 哈希存储。

# SEE ALSO

[ophcrack](/man/ophcrack)(1), [hashcat](/man/hashcat)(1), [john](/man/john)(1), [rtgen](/man/rtgen)(1)
