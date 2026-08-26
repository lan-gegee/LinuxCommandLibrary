# TAGLINE

将私钥身份添加到 OpenSSH 认证代理

# TLDR

**将默认 SSH 密钥添加**到代理

```ssh-add```

**将特定密钥添加**到代理

```ssh-add [~/.ssh/id_ed25519]```

**列出已加载密钥的指纹**

```ssh-add -l```

**列出已加载身份的公钥**

```ssh-add -L```

**从代理移除特定密钥**

```ssh-add -d [~/.ssh/id_rsa]```

**从代理移除所有密钥**

```ssh-add -D```

**以有限生命周期添加密钥**（秒）

```ssh-add -t [3600] [~/.ssh/id_rsa]```

# SYNOPSIS

**ssh-add** [**-CcDdKkLlNqvXx**] [**-E** _fingerprint_hash_] [**-H** _hostkey_file_] [**-h** _destination_constraint_] [**-S** _provider_] [**-t** _life_] [_file ..._]

# PARAMETERS

**-l**
> 列出代理中所有身份的指纹

**-L**
> 列出所有身份的公钥参数

**-d**
> 从代理中移除指定身份

**-D**
> 从代理中移除所有身份

**-t** _life_
> 设置所添加密钥的最长生命周期（以秒或 sshd_config 时间格式）

**-x**
> 用密码锁定代理

**-X**
> 解锁代理

**-k**
> 只处理普通私钥；跳过证书

**-K**
> 从 FIDO 认证器加载常驻密钥（resident key）

**-c**
> 使用密钥前要求确认

**-q**
> 操作成功后不输出信息

**-E** _hash_
> 指定指纹哈希算法（md5 或 sha256）

**-s** _pkcs11_
> 从 PKCS#11 共享库添加密钥

**-e** _pkcs11_
> 移除由 PKCS#11 共享库提供的密钥

**-T** _pubkey_
> 通过执行签名和验证来测试私钥是否可用

**-v**
> 用于调试的详细模式

# DESCRIPTION

**ssh-add** 将私钥身份添加到 ssh-agent 认证代理。不带参数运行时，它会尝试添加 ~/.ssh/id_rsa、~/.ssh/id_ecdsa、~/.ssh/id_ed25519 以及对应的 FIDO 密钥。

密钥加入代理后，SSH 认证无需在每次连接时输入口令。前提是代理正在运行，并且已设置 SSH_AUTH_SOCK 环境变量。

如果密钥需要口令，ssh-add 会从终端提示输入。SSH_ASKPASS 环境变量可以指定一个图形化密码提示程序。

# CAVEATS

只要代理在运行，密钥就一直驻留内存；在共享系统上请用 **-x** 锁定。代理套接字（SSH_AUTH_SOCK）必须防止其他用户访问。使用 **-t** 让密钥自动过期可增强安全性。

# HISTORY

ssh-add 是 **OpenSSH** 的一部分，由 OpenBSD 项目开发。SSH 代理的概念允许在不重复输入口令的情况下安全地管理密钥，最早源于 20 世纪 90 年代的 SSH1 实现。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add openssh-client-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh-agent](/man/ssh-agent)(1), [ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1), [ssh-copy-id](/man/ssh-copy-id)(1)
