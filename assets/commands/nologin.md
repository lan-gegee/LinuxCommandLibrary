# TAGLINE

礼貌地拒绝登录尝试的特殊 Shell

# TLDR

将用户的**登录 Shell 设置为 nologin** 以阻止其登录

```chsh -s nologin [user]```

为登录 Shell 为 nologin 的用户**自定义提示消息**

```echo "[declined_login_message]" > /etc/nologin.txt```

# SYNOPSIS

**nologin** [_options_]

# PARAMETERS

**-c**, **--command** _command_
> 被忽略（仅为与 shell 兼容而接受）。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本信息并退出。

其他 shell 选项（**-i**、**-l**、**--noprofile**、**--norc**、**--posix**、**--rcfile**、**-r**）也会被接受并忽略，这样调用 shell 的程序就不会崩溃。

# DESCRIPTION

**nologin** 显示一条账户不可用的消息并以非零状态退出。它被设计为那些不应能交互式登录的账户的替代 Shell。

当被设置为用户的登录 Shell 后，任何以该用户身份登录的尝试（通过 SSH、控制台或 **su**）都会被拒绝。它通常用于系统账户（daemon、nobody、www-data），或在不删除账户的情况下临时禁用用户账户。

如果存在 **/etc/nologin.txt**，nologin 会显示其内容而非默认消息。在 Linux（util-linux）上，该尝试还会被写入 **syslog**。

注意：针对单个账户的 **nologin**（本工具）不同于 **pam_nologin** PAM 模块，后者会通过 **/etc/nologin** 或 **/var/run/nologin** 在全系统范围内禁用所有非 root 登录。

# CAVEATS

以 nologin 为 Shell 的用户仍可通过 **su -s /bin/bash username** 运行命令，前提是调用者拥有足够的权限。要完全锁定账户，还需用 **passwd -l** 锁定密码。nologin 的路径因系统而异：**/usr/sbin/nologin** 或 **/sbin/nologin**。

# INSTALL

```apt: sudo apt install login```

```apk: sudo apk add util-linux-login```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chsh](/man/chsh)(1), [passwd](/man/passwd)(1), [usermod](/man/usermod)(8), [login](/man/login)(1)
