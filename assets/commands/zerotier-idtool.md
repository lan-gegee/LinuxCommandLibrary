# TAGLINE

管理 ZeroTier 加密身份

# TLDR

**生成新身份**

```zerotier-idtool generate [identity.secret]```

**从私钥获取公钥身份**

```zerotier-idtool getpublic [identity.secret]```

**签署文件**

```zerotier-idtool sign [identity.secret] [file]```

**验证签名**

```zerotier-idtool verify [identity.public] [file] [signature]```

**显示身份地址**

```zerotier-idtool info [identity.secret]```

# SYNOPSIS

**zerotier-idtool** _command_ [_args_]

# SUBCOMMANDS

**generate** _secret_file_
> 生成新身份并写入文件

**getpublic** _secret_file_
> 从私钥输出生成的公钥身份

**sign** _secret_file_ _file_to_sign_
> 用身份对文件签名

**verify** _public_file_ _file_ _signature_
> 针对公钥身份验证签名

**info** _identity_file_
> 显示身份信息（地址、类型）

**initmoon** _identity_file_
> 初始化 moon（自定义根服务器）定义

**genmoon** _moon_json_
> 从 JSON 定义生成 moon.d 文件

# DESCRIPTION

**zerotier-idtool** 管理 ZeroTier 加密身份。身份由一个私钥（保密保存）和一个公钥组成，公钥可派生出 10 位 ZeroTier 地址。

该工具可以生成新身份、提取公钥，以及执行签名和验证等加密操作。这对备份、迁移和创建自定义网络基础设施很有用。

zerotier-one 首次启动时会自动生成身份，存储在 ZeroTier 主目录中（通常为 /var/lib/zerotier-one/）。

对于高级用户，该工具还支持创建 "moon"——用于私有 ZeroTier 基础设施的自定义根服务器。

# CAVEATS

**identity.secret** 文件必须妥善保管。任何拿到该文件的人都可以冒充对应的 ZeroTier 节点。

重新生成身份会产生新地址。已有的网络成员资格必须重新授权。

创建 moon 需要理解 ZeroTier 的根服务器架构。

# SEE ALSO

[zerotier-cli](/man/zerotier-cli)(1), [zerotier-one](/man/zerotier-one)(8)
