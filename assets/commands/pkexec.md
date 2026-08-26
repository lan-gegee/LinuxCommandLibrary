# TAGLINE

通过 PolicyKit 权限提升执行程序

# TLDR

以 **root** 身份运行命令

```pkexec [command]```

切换到 **root** Shell

```pkexec```

以**指定用户**身份运行

```pkexec --user [username] [command]```

# SYNOPSIS

**pkexec** [**--user** _username_] [**--disable-internal-agent**] [_command_] [_arguments_...]

# PARAMETERS

**--user _username_**
> 以指定用户而非 root 身份运行

**--disable-internal-agent**
> 不使用内置的身份验证代理

**--keep-cwd**
> 保持当前工作目录不变

# DESCRIPTION

**pkexec** 通过 PolicyKit 以权限提升的方式以其他用户身份执行程序。与 sudo 不同，它与桌面环境集成，在可用时可以显示图形化的身份验证对话框。

授权决策基于 PolicyKit 策略，可以精细控制哪些用户能以提升的权限运行哪些程序。可以将操作配置为需要身份验证，或允许免认证执行。

# CONFIGURATION

**/usr/share/polkit-1/actions/**
> 控制授权规则的 PolicyKit 操作定义文件。

**/etc/polkit-1/rules.d/**
> 覆盖默认策略的本地授权规则。

# CAVEATS

需要 polkitd 守护进程正在运行。图形化提示需要身份验证代理（通常取决于具体桌面环境）。环境变量默认会被清理。它并非 sudo 的直接替代品。

# HISTORY

**pkexec** 是 **PolicyKit**（polkit）的一部分，由 Red Hat 的 **David Zeuthen** 开发。它提供一种与桌面环境集成的现代权限提升机制，并支持细粒度的授权策略。

# INSTALL

```apt: sudo apt install pkexec```

```apk: sudo apk add polkit-common```

```zypper: sudo zypper install pkexec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sudo](/man/sudo)(8), [doas](/man/doas)(1), [run0](/man/run0)(1), [polkit](/man/polkit)(8)
