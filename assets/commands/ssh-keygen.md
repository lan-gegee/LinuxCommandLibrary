# TAGLINE

OpenSSH 的认证密钥生成、管理与转换工具

# TLDR

**生成 SSH 密钥对**（Ed25519，推荐）

```ssh-keygen -t ed25519```

**生成 4096 位的 RSA 密钥**

```ssh-keygen -t rsa -b 4096```

**以自定义文件名生成密钥**并附加注释

```ssh-keygen -t ed25519 -f [~/.ssh/mykey] -C "[user@host]"```

**更改现有密钥的口令**

```ssh-keygen -p -f [~/.ssh/id_ed25519]```

**查看密钥的指纹**

```ssh-keygen -l -f [~/.ssh/id_ed25519.pub]```

**从私钥提取公钥**

```ssh-keygen -y -f [~/.ssh/id_ed25519] > [~/.ssh/id_ed25519.pub]```

**生成主机密钥**（所有标准类型）

```sudo ssh-keygen -A```

**将密钥转换为其他格式**

```ssh-keygen -e -f [~/.ssh/id_rsa.pub] -m [RFC4716]```

# SYNOPSIS

**ssh-keygen** [_options_]

**ssh-keygen** -t _type_ [-b _bits_] [-f _file_] [-C _comment_]

# PARAMETERS

**-t** _TYPE_
> 密钥类型：ed25519（推荐）、rsa、ecdsa、dsa

**-b** _BITS_
> 密钥位数（RSA：2048-4096；ECDSA：256/384/521）

**-f** _FILE_
> 密钥的输出文件名

**-C** _COMMENT_
> 嵌入密钥中的注释（通常为 user@host）

**-N** _PASSPHRASE_
> 密钥的新口令

**-P** _PASSPHRASE_
> 更改时的旧口令

**-p**
> 更改现有密钥的口令

**-l**
> 显示密钥文件的指纹

**-E** _HASH_
> 指纹哈希算法（md5、sha256）

**-y**
> 从私钥输出公钥

**-e**
> 将密钥导出为其他格式

**-i**
> 从其他格式导入密钥

**-m** _FORMAT_
> 密钥格式（RFC4716、PKCS8、PEM）

**-A**
> 生成所有缺失的主机密钥类型

**-R** _HOST_
> 从 known_hosts 中移除主机

**-F** _HOST_
> 在 known_hosts 中搜索主机

**-q**
> 静默模式

# DESCRIPTION

**ssh-keygen** 为 SSH 生成、管理和转换认证密钥。它创建用于免密认证和主机验证的公钥/私钥对。

私钥保存在你的机器上（由口令保护），公钥则复制到你想要访问的服务器。现代最佳实践推荐使用 **Ed25519** 密钥，因其安全性和性能更佳；不过 **RSA 4096** 仍具有广泛的兼容性。

密钥默认存放在 **~/.ssh/** 下：私钥名为 **id_ed25519**（或 id_rsa 等），公钥带 **.pub** 扩展名。公钥需复制到远程服务器的 **~/.ssh/authorized_keys** 中用于认证。

# CAVEATS

私钥必须妥善保管——任何能访问它的人都可以冒充你进行认证。请使用强口令保护私钥。DSA 密钥已弃用，并在较新的 OpenSSH 版本中被禁用。默认的 RSA 密钥长度（3072）是安全的，但 4096 提供额外余量。密钥文件权限必须严格（私钥 600，公钥 644）。

# HISTORY

ssh-keygen 是 **OpenSSH** 的一部分。OpenSSH 起源于 **1999 年**的 OpenBSD 项目，是 SSH 的自由实现。最初的 SSH 协议由 **Tatu Ylönen** 于 **1995 年**开发。OpenSSH 随时间推移增加了对新密钥类型的支持：2011 年加入 ECDSA，2014 年加入 Ed25519。凭借安全性和高效性，Ed25519 在 OpenSSH 8.0（2019 年）中成为默认密钥类型。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add openssh-keygen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [ssh-copy-id](/man/ssh-copy-id)(1), [ssh-agent](/man/ssh-agent)(1), [sshd](/man/sshd)(8)
