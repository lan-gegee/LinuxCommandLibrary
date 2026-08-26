# TAGLINE

生成随机密码

# TLDR

**生成**随机密码

```apg```

以**指定长度**生成

```apg -m [16] -x [20]```

生成**可发音**的密码

```apg -a 0```

生成**随机字符**密码

```apg -a 1```

使用**指定字符集**生成

```apg -M SNCL```

生成时排除**易混淆字符**

```apg -E "0O1lI"```

# SYNOPSIS

**apg** [_-a algorithm_] [_-m min_] [_-x max_] [_-M mode_] [_-E chars_] [_options_]

# DESCRIPTION

**apg**（Automated Password Generator）创建随机密码，既可使用可发音密码算法（基于音素序列），也可使用完全随机的字符。

可发音的密码更容易记忆，但安全性可能较低。随机密码具有最大的熵，但更难记住。

# PARAMETERS

**-a** _algorithm_
> 算法：0=可发音，1=随机

**-m** _length_
> 最小密码长度

**-x** _length_
> 最大密码长度

**-n** _count_
> 要生成的密码数量

**-M** _mode_
> 字符类别：S=特殊字符、N=数字、C=大写字母、L=小写字母。用大写作为前缀表示必须包含该类别。

**-E** _chars_
> 排除特定字符

**-r** _file_
> 对照字典文件进行密码过滤检查

**-t**
> 为可发音密码打印发音

**-q**
> 安静模式（只输出密码）

**-s**
> 提示通过键盘输入随机种子

**-l**
> 按发音拼读生成的密码

# CAVEATS

可发音密码可能存在降低熵的模式。对高安全场景请使用足够长度的随机模式。输出到终端；可通过管道送入 clip 以复制到剪贴板。

# HISTORY

**apg** 由 Adel I. Mirzazhanov 创建，为 Unix 系统同时实现了随机和可发音两种密码生成算法。

# INSTALL

```apt: sudo apt install apg```

```dnf: sudo dnf install apg```

```aur: yay -S apg```

```apk: sudo apk add apg```

```zypper: sudo zypper install apg```

```nix: nix profile install nixpkgs#apg```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pwgen](/man/pwgen)(1), [openssl](/man/openssl)(1), [mkpasswd](/man/mkpasswd)(1)
