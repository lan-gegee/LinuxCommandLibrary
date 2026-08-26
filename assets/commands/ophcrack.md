# TAGLINE

使用彩虹表从 LM 等哈希恢复密码的 Windows 密码破解工具

# TLDR

**使用彩虹表从 pwdump 文件破解密码**

```ophcrack -g -d [path/to/tables] -f [hashes.txt]```

**使用指定的表**并开启多线程破解

```ophcrack -g -d [path/to/tables] -t [xp_free_fast] -f [hashes.txt] -n [4]```

**破解并将结果保存**到文件

```ophcrack -g -d [path/to/tables] -f [hashes.txt] -o [cracked.txt]```

**在彩虹表之外启用暴力破解**

```ophcrack -g -B -d [path/to/tables] -f [hashes.txt]```

**以静默模式运行**并记录日志

```ophcrack -g -q -d [path/to/tables] -f [hashes.txt] -l [log.txt]```

**启动图形界面模式**

```ophcrack```

# SYNOPSIS

**ophcrack** [_options_]

**ophcrack** -g -d _tables_dir_ -f _hash_file_

# PARAMETERS

**-g**
> 禁用图形界面，以命令行模式运行

**-d** _DIR_
> 指定彩虹表的基础目录

**-t** _TABLES_
> 指定要使用的表（table_name,start,end:...）

**-f** _FILE_
> 从 pwdump 或会话文件加载哈希

**-o** _FILE_
> 以 pwdump 格式写出结果

**-l** _FILE_
> 将所有输出记录到文件

**-n** _NUM_
> 使用的线程数

**-a**
> 禁用审计模式（默认）

**-A**
> 启用审计模式

**-b**
> 禁用暴力破解

**-B**
> 启用暴力破解（默认）

**-c** _FILE_
> 指定配置文件

**-e**
> 不显示空密码

**-i**
> 在输出中隐藏用户名

**-I**
> 显示用户名（默认）

**-p** _NUM_
> 预加载级别（0=不加载，1=索引，2=索引+结尾，3=全部）

**-q**
> 静默模式

**-r**
> 立即开始破解（仅限 GUI）

**-s**
> 禁用会话自动保存

**-S** _FILE_
> 用于自动保存进度的会话文件

**-u**
> 显示统计信息

**-D**
> 显示调试信息

**-h**
> 显示帮助

# DESCRIPTION

**ophcrack** 是一款 Windows 密码破解工具，使用彩虹表从 LM 和 NTLM 哈希中恢复密码。它采用时间-内存权衡技术，通过预计算的哈希链大幅加快破解过程。

该工具可破解 Windows NT、2000、XP、Vista、7、8 和 10 的密码。常见密码模式有免费彩虹表可用，付费表的破解成功率更高。它可以从 pwdump 文件、SAM/SYSTEM 注册表文件导入哈希，也可以直接从本地/远程 Windows 系统转储哈希。

Ophcrack 同时提供 GUI 和命令行两种界面。GUI 包含分析密码强度分布的实时图表。LiveCD 版本可以直接在 Windows 机器上启动，无需安装软件即可提取并破解密码。

# CAVEATS

彩虹表需要大量磁盘空间（数百 MB 到数十 GB）。LM 哈希仅支持最长 14 个字符且不区分大小写的密码。NTLM 哈希更难破解。成功与否取决于是否拥有与密码字符集相匹配的表。只能在你拥有所有权或已获授权的系统上使用。

# HISTORY

Ophcrack 由 **Philippe Oechslin** 在洛桑联邦理工学院（EPFL）开发，于 **2004 年**首次发布。Oechslin 发明了彩虹表技术，作为对早期时间-内存权衡方法的改进。该工具揭示了 LM 哈希存储的脆弱性，促使 Microsoft 决定在 Windows Vista 及后续版本中弃用 LM 哈希。

# INSTALL

```apt: sudo apt install ophcrack```

```dnf: sudo dnf install ophcrack```

```brew: brew install ophcrack```

```nix: nix profile install nixpkgs#ophcrack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hashcat](/man/hashcat)(1), [john](/man/john)(1), [pwdump](/man/pwdump)(1), [rcrack](/man/rcrack)(1)
