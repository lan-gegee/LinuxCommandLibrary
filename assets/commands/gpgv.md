# TAGLINE

精简版 OpenPGP 签名验证工具

# TLDR

**验证已签名的文件**

```gpgv [file.sig]```

**验证分离签名**

```gpgv [file.sig] [file]```

**使用指定的密钥环**

```gpgv --keyring [keyring.gpg] [file.sig]```

**详细模式验证**

```gpgv -v [file.sig]```

**安静模式**

```gpgv -q [file.sig]```

# SYNOPSIS

**gpgv** [_options_] [_sigfile_] [_files_]

# PARAMETERS

**-v**, **--verbose**
> 处理过程中输出更多信息。

**-q**, **--quiet**
> 尽量保持安静。

**--keyring** _file_
> 使用指定的密钥环。

**--homedir** _dir_
> GnuPG 主目录。

**--ignore-time-conflict**
> 将时间戳检查降级为警告。

**--weak-digest** _name_
> 将指定摘要算法视为弱算法。

**--status-fd** _n_
> 将状态字符串写入文件描述符。

# DESCRIPTION

**gpgv** 是 gpg 的精简版本，专门用于验证 OpenPGP 签名。它假定密钥环中的所有密钥都是可信的，不会检查密钥是否过期或被吊销。

默认情况下，它使用 GnuPG 主目录中的 trustedkeys.kbx 或 trustedkeys.gpg 密钥环。它常用于包管理器和自动化验证脚本等信任关系已预先建立的场景。

# CAVEATS

验证成功返回 0，任何签名无效返回 1，致命错误返回其他代码。与 gpg 不同，gpgv 不验证密钥的信任状态。

# INSTALL

```apt: sudo apt install gpgv```

```apk: sudo apk add gpgv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [gpg2](/man/gpg2)(1)

# RESOURCES

```[Source code](https://dev.gnupg.org/source/gnupg/)```

```[Homepage](https://www.gnupg.org/)```

```[Documentation](https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html)```

<!-- verified: 2026-07-17 -->
