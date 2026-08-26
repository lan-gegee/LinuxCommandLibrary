# TAGLINE

GnuPG 2 加密与数字签名

# TLDR

**生成密钥对**

```gpg2 --full-generate-key```

**列出密钥**

```gpg2 --list-keys```

**为接收者加密文件**

```gpg2 -e -r [recipient@email.com] [file]```

**解密文件**

```gpg2 -d [file.gpg]```

**签名文件**

```gpg2 --sign [file]```

**验证签名**

```gpg2 --verify [file.sig]```

**导出公钥**

```gpg2 --armor --export [keyid] > [public.asc]```

**导入密钥**

```gpg2 --import [public.asc]```

使用口令进行**对称加密**

```gpg2 -c [file]```

# SYNOPSIS

**gpg2** [_options_] [_files_]

# PARAMETERS

**-e**, **--encrypt**
> 加密数据。

**-d**, **--decrypt**
> 解密数据。

**-s**, **--sign**
> 签名数据。

**--verify**
> 验证签名。

**-r**, **--recipient** _name_
> 为指定接收者加密。

**-a**, **--armor**
> ASCII 封装输出。

**--gen-key**
> 使用默认设置生成密钥对。

**--full-generate-key**
> 通过完整选项生成密钥对（算法、长度、有效期）。

**--list-keys**
> 列出公钥。

**--list-secret-keys**
> 列出私钥。

**--export** _keyid_
> 导出公钥。

**--import** _file_
> 导入密钥。

**--delete-keys** _keyid_
> 从密钥环删除公钥。

**--delete-secret-keys** _keyid_
> 从密钥环删除私钥。

**--keyserver** _server_
> 要使用的密钥服务器。

**-o**, **--output** _file_
> 将输出写入文件而不是标准输出。

**--clearsign**
> 生成明文签名。

**--detach-sign**
> 生成分离签名。

**-c**, **--symmetric**
> 使用口令进行对称加密。

**--batch**
> 以非交互批处理模式运行。

**-q**, **--quiet**
> 尽量减少输出。

**-v**, **--verbose**
> 显示详细的处理信息。

# DESCRIPTION

**gpg2**（GnuPG 2）是 GNU Privacy Guard 的现代版本，实现了 OpenPGP 标准，用于加密、数字签名和密钥管理。它采用模块化架构，将功能拆分到独立的守护进程中以提高安全性。

在大多数现代系统上，**gpg** 是 gpg2 的别名。两者共享密钥环且功能等价，gpg2 提供了更好的架构和守护进程管理。

# CONFIGURATION

**~/.gnupg/gpg.conf**
> 用户配置文件，用于设置默认选项、首选算法和密钥服务器。

**~/.gnupg/gpg-agent.conf**
> gpg-agent 守护进程的配置文件，负责口令缓存和密钥操作。

# CAVEATS

密钥管理需要理解信任网络（web of trust）。私钥必须妥善保护。口令的选择至关重要。在现代系统上 gpg 和 gpg2 共享密钥环。

# HISTORY

GnuPG 由 **Werner Koch** 于 **1997 年**创建，作为 PGP 的自由软件替代品。GPG 2.0 于 **2006 年**发布，引入模块化架构。它是安全电子邮件和软件签名的基础工具。

# INSTALL

```apk: sudo apk add gpg```

```zypper: sudo zypper install gpg2```

```brew: brew install gpg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [gpgconf](/man/gpgconf)(1)
