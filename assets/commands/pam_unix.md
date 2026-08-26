# TAGLINE

提供标准 Unix 认证

# TLDR

**标准 Unix 认证**

```auth required pam_unix.so```

**密码管理**

```password required pam_unix.so sha512 shadow```

**会话管理**

```session required pam_unix.so```

**空密码检查**

```auth required pam_unix.so nullok```

# SYNOPSIS

**pam_unix.so** [_options_]

# PARAMETERS

**nullok**
> 允许空密码。

**sha512**
> 使用 SHA-512 哈希。

**shadow**
> 使用影子密码。

**remember=**_N_
> 记住最近 N 个密码。

**try_first_pass**
> 先使用先前输入的密码。

# DESCRIPTION

**pam_unix** 提供标准 Unix 认证。使用 /etc/passwd 和 shadow 文件。

该模块处理基础认证。是 PAM 的核心组件。

# CAVEATS

核心 PAM 模块。配置至关重要。需注意哈希算法的选择。

# HISTORY

pam_unix 通过 passwd/shadow 提供**传统 Unix 认证**。

# SEE ALSO

[pam](/man/pam)(8), [passwd](/man/passwd)(5)
