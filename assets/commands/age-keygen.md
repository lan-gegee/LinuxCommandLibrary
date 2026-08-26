# TAGLINE

为 age 生成加密密钥对

# TLDR

**生成**新的密钥对（打印到标准输出）

```age-keygen```

**保存**密钥到文件

```age-keygen -o [key.txt]```

从现有身份文件**提取公钥**

```age-keygen -y [key.txt]```

从 SSH ed25519 密钥**提取公钥**

```age-keygen -y [~/.ssh/id_ed25519]```

**生成**混合后量子密钥对（age v1.3.0+）

```age-keygen -pq -o [key.txt]```

# SYNOPSIS

**age-keygen** [_options_] [**-o** _file_]

**age-keygen** **-y** [_identity-file_]

# PARAMETERS

**-o** _file_
> 把密钥写入文件而不是标准输出。文件已存在时不会覆盖。

**-y** [_file_]
> 读取身份文件（或标准输入）并输出对应的公钥（recipient）。支持 age 私钥和 ed25519 SSH 密钥。

**-pq**
> 使用 ML-KEM-768 + X25519 生成混合后量子密钥（age v1.3.0+）。

**--version**
> 打印版本并退出。

# OUTPUT FORMAT

```
# created: 2024-01-15T10:30:00Z
# public key: age1...
AGE-SECRET-KEY-1...
```

后量子密钥使用前缀 **age1pq1...**（公钥）和 **AGE-SECRET-KEY-PQ-1...**（私钥）。

# DESCRIPTION

**age-keygen** 生成供 age 加密工具使用的 X25519 密钥对。私钥（身份）会被打印到标准输出或写入文件，而公钥则以注释的形式包含在输出中。

生成的密钥就是简单的文本字符串：公钥以 “age1” 开头，私钥以 “AGE-SECRET-KEY-1” 开头。**-y** 标志可以从现有身份中提取公钥，方便你在不暴露私钥的情况下分享自己的 recipient 信息。

# CAVEATS

务必保管好私钥；任何拿到它的人都能解密本属于你的文件。age 没有密钥吊销机制。请安全地备份你的密钥。**-o** 标志不会覆盖已存在的文件。后量子 recipient 的长度约为 2000 个字符。

# HISTORY

**age-keygen** 由 **Filippo Valsorda** 于 **2019** 年与 age 一同发布。它提供了一个极简的密钥生成工具，延续 age 本身的设计哲学：简单、安全、没有多余的选项。版本 **1.3.0** 通过 **-pq** 标志加入了混合后量子密钥生成能力。

# INSTALL

```apt: sudo apt install age```

```dnf: sudo dnf install age```

```pacman: sudo pacman -S age```

```apk: sudo apk add age```

```zypper: sudo zypper install age```

```brew: brew install age```

```nix: nix profile install nixpkgs#age```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[age](/man/age)(1), [ssh-keygen](/man/ssh-keygen)(1), [gpg](/man/gpg)(1)
