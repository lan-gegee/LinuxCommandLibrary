# TAGLINE

为 yadm 文件提供透明加密

# TLDR

**初始化 transcrypt**

```yadm transcrypt -c aes-256-gcm```

**解锁文件**

```yadm transcrypt --display```

**配置 transcrypt**

```yadm transcrypt -p [password]```

# SYNOPSIS

**yadm** **transcrypt** [_options_]

# PARAMETERS

**-c** _cipher_
> 加密算法。

**-p** _password_
> 设置密码。

**--display**
> 显示配置。

# DESCRIPTION

**yadm transcrypt** 封装 transcrypt 以提供透明的文件加密。它根据 .gitattributes 模式在推送时加密文件。是 yadm encrypt 之外的另一种加密方式。

# SEE ALSO

[yadm](/man/yadm)(1), [transcrypt](/man/transcrypt)(1)
