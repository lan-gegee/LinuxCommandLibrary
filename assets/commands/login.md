# TAGLINE

在系统上启动用户会话

# TLDR

以某用户身份**登录**

```login [user]```

**跳过身份验证**登录

```login -f [user]```

**保留环境变量**登录

```login -p [user]```

从**远程主机**登录

```login -h [host] [user]```

# SYNOPSIS

**login** [_options_] [_username_]

# DESCRIPTION

**login** 在系统上启动用户会话。它对用户进行身份验证、设置环境并启动 shell。该命令通常由 init 或终端程序调用。

# PARAMETERS

**-f**
> 跳过身份验证（针对已预认证的用户）

**-p**
> 保留环境变量

**-h HOST**
> 指定远程主机名（用于远程登录）

# CAVEATS

直接调用仅限 root 或由特定程序发起。-f 选项仅 root 可用。PAM 模块控制身份验证行为。

# HISTORY

login 命令可追溯到 **20 世纪 70 年代**贝尔实验室最初的 Unix 系统，是最基本的用户身份验证机制。

# INSTALL

```apt: sudo apt install login```

```apk: sudo apk add util-linux-login```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[su](/man/su)(1), [sudo](/man/sudo)(8), [passwd](/man/passwd)(1), [getty](/man/getty)(8)
