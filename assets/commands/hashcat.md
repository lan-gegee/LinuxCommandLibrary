# TAGLINE

利用 CPU、GPU 及其他硬件的高性能密码恢复工具

# TLDR

对 MD5 哈希**执行字典攻击**

```hashcat -m 0 -a 0 [hashes.txt] [wordlist.txt]```

使用词表**破解 SHA-256 哈希**并输出到文件

```hashcat -m 1400 -a 0 -o [cracked.txt] [hashes.txt] [wordlist.txt]```

使用掩码发起**暴力破解攻击**（8 个小写字符）

```hashcat -m 0 -a 3 [hashes.txt] '?l?l?l?l?l?l?l?l'```

**运行基准测试**以检验系统性能

```hashcat -b```

从 potfile **显示已破解的密码**

```hashcat -m 0 --show [hashes.txt]```

使用 GPU **破解 bcrypt 哈希**

```hashcat -m 3200 -a 0 -D 2 [hashes.txt] [wordlist.txt]```

**恢复之前的会话**

```hashcat --restore```

配合规则**破解 NTLM 哈希**

```hashcat -m 1000 -a 0 -r [rules/best64.rule] [hashes.txt] [wordlist.txt]```

# SYNOPSIS

**hashcat** [_options_] _hashfile_ [_dictionary_|_mask_]

**hashcat** -m _hashtype_ -a _attackmode_ [_options_] _hashfile_ _wordlist_

# PARAMETERS

**-m**, **--hash-type** _NUM_
> 哈希类型（0=MD5，1000=NTLM，1400=SHA256，1800=SHA512crypt，3200=bcrypt）

**-a**, **--attack-mode** _NUM_
> 攻击模式（0=字典，1=组合器，3=暴力破解，6=混合，7=混合）

**-o**, **--outfile** _FILE_
> 存放已恢复密码的输出文件

**-r**, **--rules-file** _FILE_
> 用于变换单词的规则文件

**-D**, **--opencl-device-types** _NUM_
> 设备类型（1=CPU，2=GPU，3=FPGA/DSP/协处理器）

**-w**, **--workload-profile** _NUM_
> 工作负载档位（1=低，2=默认，3=高，4=nightmare）

**-b**, **--benchmark**
> 对所有哈希类型运行基准测试

**--show**
> 显示 potfile 中已破解的密码

**--remove**
> 哈希被破解后立即从文件中移除

**--restore**
> 恢复之前的会话

**--session** _NAME_
> 为会话命名，以便日后恢复

**--status**
> 启用自动状态更新

**--runtime** _SECS_
> 在指定秒数后中止

**-1**, **-2**, **-3**, **-4**
> 为掩码定义自定义字符集

**-i**, **--increment**
> 启用掩码增量模式

**--increment-min** _NUM_
> 增量模式的起始掩码长度

**--increment-max** _NUM_
> 增量模式的结束掩码长度

**-h**, **--help**
> 显示帮助信息

**-V**, **--version**
> 显示版本号

# MASK CHARSETS

**?l**
> 小写字母（a-z）

**?u**
> 大写字母（A-Z）

**?d**
> 数字（0-9）

**?s**
> 特殊字符

**?a**
> 所有可打印字符（?l?u?d?s）

**?b**
> 二进制（0x00-0xff）

# DESCRIPTION

**hashcat** 是一款高性能密码恢复工具，它利用 CPU、GPU 和其他硬件加速器来破解哈希密码。它支持 300 多种哈希类型，包括 MD5、SHA 系列、bcrypt、WPA 以及众多应用专用格式。

该工具提供多种攻击模式：字典攻击使用词表；暴力破解使用掩码生成候选密码；组合器把多个词典中的单词拼接起来；混合模式则结合上述方法。规则可以对词典单词进行变换，以覆盖常见的密码模式。

Hashcat 维护一个 potfile，记录已破解的哈希以避免重复工作。会话可以暂停和恢复。该工具会自动针对可用硬件进行优化，并支持跨多台机器的分布式破解。

# CAVEATS

密码破解极度消耗 CPU/GPU 并产生大量热量。只应在自己拥有或已获明确授权测试的系统上使用。大型词表和复杂攻击可能需要运行数天甚至数周。必须正确安装 GPU 驱动才能启用硬件加速。某些哈希类型（bcrypt、scrypt）在设计上就难以快速破解。

# HISTORY

Hashcat 由 **Jens Steube**（atom）创建，首个版本发布于 **2009 年**。它最初是闭源软件，于 **2015 年 12 月**转为开源。该项目从仅支持 CPU（hashcat-legacy）演进到 GPU 加速（oclHashcat），最终统一为支持多平台的 hashcat。它已成为世界上最快的密码恢复工具，开创了基于规则的攻击、优化的 GPU 内核等技术。

# INSTALL

```apt: sudo apt install hashcat```

```dnf: sudo dnf install hashcat```

```pacman: sudo pacman -S hashcat```

```zypper: sudo zypper install hashcat```

```brew: brew install hashcat```

```nix: nix profile install nixpkgs#hashcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[john](/man/john)(1), [hydra](/man/hydra)(1), [ophcrack](/man/ophcrack)(1), [aircrack-ng](/man/aircrack-ng)(1)
