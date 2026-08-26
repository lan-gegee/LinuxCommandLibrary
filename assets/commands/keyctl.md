# TAGLINE

管理 Linux 内核密钥环设施的实用工具

# TLDR

**列出**密钥环中的密钥

```keyctl list @us```

向密钥环中**添加**密钥

```keyctl add user keyname "keyvalue" @us```

从 **stdin** 添加密钥值

```echo -n "value" | keyctl padd user keyname @us```

**读取**密钥值

```keyctl read keyid```

以管道方式输出密钥值（原始输出）

```keyctl pipe keyid```

为密钥设置**超时时间**

```keyctl timeout keyid 3600```

**吊销**密钥

```keyctl revoke keyid```

**清空**密钥环中的所有密钥

```keyctl clear @us```

# SYNOPSIS

**keyctl** _command_ [_options_] [_arguments_]

# DESCRIPTION

**keyctl** 是一个用于管理 Linux 内核密钥环设施的实用工具。它允许创建、修改和查询密钥及密钥环，这些密钥可以存储认证令牌、加密密钥和其他安全相关数据。

# PARAMETERS

**add TYPE NAME DATA KEYRING**
> 创建新密钥并将其附加到密钥环

**padd TYPE NAME KEYRING**
> 从 stdin 读取负载来添加密钥

**request TYPE NAME [DEST_KEYRING]**
> 向内核请求密钥

**update KEY DATA**
> 更新密钥的负载

**newring NAME KEYRING**
> 创建新的密钥环

**revoke KEY**
> 吊销密钥，阻止后续操作

**clear KEYRING**
> 移除密钥环中的所有密钥

**unlink KEY KEYRING**
> 从密钥环中移除某个密钥

**search KEYRING TYPE DESCRIPTION [DEST_KEYRING]**
> 在密钥环中搜索密钥

**read KEY**
> 读取并显示密钥的负载

**pipe KEY**
> 不经格式化直接输出密钥的负载

**list KEYRING**
> 列出密钥环中的密钥

**describe KEY**
> 显示密钥属性

**timeout KEY SECONDS**
> 设置密钥的过期时间

**setperm KEY MASK**
> 设置密钥权限

# CAVEATS

特殊密钥环标识符：@t（线程）、@p（进程）、@s（会话）、@u（用户）、@us（用户默认会话）。密钥会过期并被自动垃圾回收。访问密钥需要相应的权限。

# HISTORY

**keyctl** 是 **keyutils** 软件包的一部分，为内核 2.6 引入的 Linux 内核密钥管理设施提供用户空间访问接口。

# INSTALL

```apt: sudo apt install keyutils```

```dnf: sudo dnf install keyutils```

```pacman: sudo pacman -S keyutils```

```apk: sudo apk add keyutils```

```zypper: sudo zypper install keyutils```

```brew: brew install keyutils```

```nix: nix profile install nixpkgs#keyutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh-add](/man/ssh-add)(1), [gpg](/man/gpg)(1)
