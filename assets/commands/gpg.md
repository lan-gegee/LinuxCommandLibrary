# TAGLINE

GNU Privacy Guard 加密与签名工具

# TLDR

**生成新的密钥对**

```gpg --gen-key```

在公钥环中**列出所有密钥**

```gpg --list-keys```

为特定接收者**加密文件**

```gpg -e -r [recipient_email] [file]```

**解密文件**

```gpg -d [file.gpg]```

用自己的私钥**签名文件**

```gpg --sign [file]```

**验证签名**

```gpg --verify [file.sig]```

**导出公钥**到文件

```gpg --export -a "[user_id]" > [public.key]```

**导入公钥**

```gpg --import [public.key]```

# SYNOPSIS

**gpg** [_--homedir dir_] [_--options file_] [_options_] _command_ [_args_]

# PARAMETERS

**-e**, **--encrypt**
> 将数据加密给一个或多个接收者

**-d**, **--decrypt**
> 解密数据（输入看起来是密文时为默认行为）

**-s**, **--sign**
> 生成签名

**--verify**
> 验证签名

**-c**, **--symmetric**
> 使用口令进行对称加密

**-r** _name_, **--recipient** _name_
> 为指定的接收者加密

**-u** _name_, **--local-user** _name_
> 使用指定密钥作为签名所用密钥

**-a**, **--armor**
> 生成 ASCII 封装的输出

**-o** _file_, **--output** _file_
> 将输出写入指定文件

**--gen-key**
> 生成新的密钥对

**--full-gen-key**
> 通过对话框逐项设置所有选项来生成新的密钥对

**--list-keys**
> 列出公钥环中的所有密钥

**--list-secret-keys**
> 列出私钥环中的所有密钥

**--import**
> 从文件导入密钥

**--export**
> 从密钥环导出密钥

**--delete-keys** _name_
> 从公钥环移除密钥

**--delete-secret-keys** _name_
> 从私钥环移除密钥

**--fingerprint**
> 列出密钥及其指纹

**--keyserver** _url_
> 指定要使用的密钥服务器

**--send-keys** _keyids_
> 将密钥发送到密钥服务器

**--recv-keys** _keyids_
> 从密钥服务器导入密钥

**--batch**
> 批处理模式，从不请求输入

**--yes**
> 对大多数问题默认回答 yes

**--passphrase** _string_
> 使用指定的口令

# DESCRIPTION

**gpg**（GNU Privacy Guard）是对 RFC 4880 定义的 OpenPGP 标准的完整自由实现。它可以加密和签名数据，具备功能全面的密钥管理系统，并提供访问公钥目录的模块。

GPG 同时支持对称（基于密码）和非对称（公钥/私钥）加密。常见用途包括加密敏感文件、签名电子邮件、验证软件包的真实性以及建立安全通信通道。

# CONFIGURATION

**~/.gnupg/gpg.conf**
> 用户配置文件，用于设置默认选项、密钥服务器和算法偏好。

**~/.gnupg/pubring.kbx**
> 公钥环数据库，存储已导入和已生成的公钥。

**~/.gnupg/trustdb.gpg**
> 信任模型所用的信任数据库。

# CAVEATS

密钥管理至关重要；丢失私钥或忘记口令意味着永久无法访问加密数据。信任网络（web of trust）模型要求仔细验证密钥以防中间人攻击。随着密码学标准的演进，应定期审查默认算法和密钥长度。

# HISTORY

GPG 由 **Werner Koch** 于 **1997 年**首次发布（版本 0.0.0），首个稳定版（1.0.0）于 **1999 年**发布，是 PGP（Pretty Good Privacy）的自由软件替代品。它作为 GNU 计划的一部分开发，此后成为类 Unix 系统上电子邮件加密的事实标准。GPG 2.0 于 **2006 年**引入模块化架构，2.2 版本改进了默认算法和密钥服务器处理。该项目至今仍在积极维护，并被世界各地的记者、活动人士和安全意识较强的用户广泛使用。

# INSTALL

```apt: sudo apt install gpg```

```apk: sudo apk add gpg```

```brew: brew install gpg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [openssl](/man/openssl)(1), [age](/man/age)(1), [sha256sum](/man/sha256sum)(1)
