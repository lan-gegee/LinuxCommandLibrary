# TAGLINE

计算密码哈希

# TLDR

使用 SHA-512 crypt（推荐）**对密码做哈希**

```openssl passwd -6```

使用 **SHA-256** crypt 对给定密码做哈希

```openssl passwd -5 [password]```

使用 **Apache apr1** 算法和固定盐值做哈希

```openssl passwd -apr1 -salt [xxxxxxxx] [password]```

从 **stdin** 读取密码（比命令行参数更安全）

```echo -n [password] | openssl passwd -6 -stdin```

以制表符分隔的表格打印**明文和哈希**

```openssl passwd -6 -table [password]```

使用**选定的盐值**使哈希可复现

```openssl passwd -6 -salt [saltsalt] [password]```

# SYNOPSIS

**openssl** **passwd** [**-help**] [**-1**] [**-apr1**] [**-aixmd5**] [**-5**] [**-6**] [**-salt** _string_] [**-in** _file_] [**-stdin**] [**-noverify**] [**-quiet**] [**-table**] [**-reverse**] [_password_]

# PARAMETERS

**-help**
> 打印用法信息后退出。

**-1**
> 使用基于 MD5 的 BSD 密码算法（`$1$`）。这是默认值。

**-apr1**
> 使用 BSD MD5 算法的 Apache apr1 变体（`$apr1$`）。

**-aixmd5**
> 使用 BSD 算法的 AIX MD5 变体。

**-5**
> 使用 Ulrich Drepper 定义的 SHA-256 crypt（`$5$`）。

**-6**
> 使用 Ulrich Drepper 定义的 SHA-512 crypt（`$6$`）。

**-salt** _string_
> 使用此盐值而非随机盐值。从终端读取密码时，还会隐含启用 **-noverify**。

**-in** _file_
> 从 _file_ 读取密码，每行一个。

**-stdin**
> 从标准输入读取密码。

**-noverify**
> 从终端读取密码时不再进行第二次确认提示。

**-quiet**
> 抑制命令行密码被截断的警告。

**-table**
> 在每个哈希前面加上明文密码和一个制表符。

**-reverse**
> 配合 **-table** 使用时，先打印哈希再打印明文，而不是先明文再哈希。

**_password_**
> 要做哈希的密码。若省略且既未给出 **-in** 也未给出 **-stdin**，则从终端读取密码。

# DESCRIPTION

**openssl passwd** 使用 Unix crypt 风格的算法计算密码的单向哈希。密码可以来自命令行参数、文件（**-in**）、标准输入（**-stdin**），或交互式终端提示。

默认算法是 MD5 crypt（**-1**）。**-5** 和 **-6** 分别选择 SHA-256 和 SHA-512 crypt。**-apr1** 生成的哈希与 Apache **htpasswd** 的 MD5 文件兼容。除非给出 **-salt**，否则每次都会使用新的随机盐值，因此同一密码每次运行都会得到不同的哈希字符串。

典型用途包括：为系统配置生成 `/etc/shadow` 风格的哈希、生成 Apache apr1 哈希，以及检查给定密码在所选算法下的编码结果。该命令只打印哈希；不会更改系统账户。

# CAVEATS

命令行上的密码会在进程列表中可见。建议改用终端提示或 **-stdin**。默认的 **-1**（MD5 crypt）按现代标准较弱；除非需要特定的遗留格式，否则请使用 **-6**（SHA-512 crypt）。

不使用 **-salt** 时，每次调用的输出都会不同。传统的 DES **crypt**（`-crypt`，会将密码截断为 8 个字符）已在 **OpenSSL 3.0 中移除**。该命令生成的哈希不是 bcrypt、scrypt 或 Argon2。

# HISTORY

**openssl passwd** 自大约 **2000 年**起就是 OpenSSL 命令行工具的一部分。在 **OpenSSL 1.1.x** 中，默认算法是通过 **-crypt** 选择的传统 Unix **crypt**。**OpenSSL 3.0**（2021 年）移除了 **-crypt**，默认改为 **-1**（MD5 crypt）。**-5** 和 **-6** 实现了 Drepper 的 SHA-crypt。

# INSTALL

```apt: sudo apt install openssl```

```dnf: sudo dnf install openssl```

```pacman: sudo pacman -S openssl```

```apk: sudo apk add openssl```

```zypper: sudo zypper install openssl```

```brew: brew install openssl```

```nix: nix profile install nixpkgs#openssl```

<!-- packages: 2026-08-19 -->

# SEE ALSO

[openssl](/man/openssl)(1), [htpasswd](/man/htpasswd)(1), [mkpasswd](/man/mkpasswd)(1), [passwd](/man/passwd)(1)

# RESOURCES

```[Source code](https://github.com/openssl/openssl)```

```[Homepage](https://www.openssl.org/)```

```[Documentation](https://docs.openssl.org/master/man1/openssl-passwd/)```

<!-- verified: 2026-08-19 -->
