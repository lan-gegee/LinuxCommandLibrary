# TAGLINE

生成易记或随机的密码

# TLDR

**生成一个密码**

```pwgen```

**生成指定长度**的密码

```pwgen [16]```

**生成多个密码**

```pwgen [16] [5]```

**生成安全密码**（更难记忆）

```pwgen -s [16]```

**生成至少含一个符号**的密码

```pwgen -y [16]```

**生成不含易混淆字符**的密码

```pwgen -B [16]```

**生成单个密码**（不分列显示）

```pwgen -1 [16]```

**生成完全随机**的密码

```pwgen -sy [20] [1]```

# SYNOPSIS

**pwgen** [_options_] [_length_] [_count_]

# DESCRIPTION

**pwgen** 生成随机的、可发音的密码。默认情况下，它生成的密码专为人类易于记忆而设计，同时保持相当的安全性。

该工具可以生成不同风格的密码：可发音的（默认）、完全随机的、包含或不包含特殊字符的，以及带有各种约束条件的密码。它会输出多个密码，让用户从中挑选一个自己觉得好记的。

pwgen 常用于创建初始密码、为脚本生成密钥，以及批量创建密码。

# PARAMETERS

**-s**, **--secure**
> 生成完全随机的密码。

**-y**, **--symbols**
> 至少包含一个特殊字符。

**-n**, **--numerals**
> 至少包含一个数字。

**-c**, **--capitalize**
> 至少包含一个大写字母。

**-A**, **--no-capitalize**
> 不含大写字母。

**-0**, **--no-numerals**
> 不含数字。

**-B**, **--ambiguous**
> 避免易混淆字符（0O1lI）。

**-1**
> 每行只打印一个密码。

**-v**, **--no-vowels**
> 不含元音字母（避免出现冒犯性词汇）。

**-H** _file_, **--sha1=** _file_
> 使用文件的 SHA1 哈希作为种子。

**-r** _chars_
> 移除指定的字符。

# CAVEATS

默认的可发音密码不如随机密码安全。生成的密码仍应满足你的安全要求。高安全性场景请使用 -s。熵取决于密码长度和字符集。

# HISTORY

**pwgen** 由 **Theodore Ts'o** 于 **2001** 年编写。它的设计目标是生成用户真正能记住的密码，从而减少把密码写下来的倾向。该工具在个人和管理员的密码生成中一直很受欢迎。

# INSTALL

```apt: sudo apt install pwgen```

```dnf: sudo dnf install pwgen```

```pacman: sudo pacman -S pwgen```

```apk: sudo apk add pwgen```

```zypper: sudo zypper install pwgen```

```brew: brew install pwgen```

```nix: nix profile install nixpkgs#pwgen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [mkpasswd](/man/mkpasswd)(1), [apg](/man/apg)(1), [pass](/man/pass)(1)
