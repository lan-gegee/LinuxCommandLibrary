# TAGLINE

系统权限授权框架

# TLDR

**列出所有已注册的 polkit 操作**

```pkaction```

**显示特定操作的详细信息**

```pkaction --verbose --action-id [org.freedesktop.login1.reboot]```

**检查进程是否有权执行某个操作**

```pkcheck --action-id [org.freedesktop.login1.reboot] --process [pid]```

**以其他用户身份执行命令**（默认：root）

```pkexec [command]```

**以指定用户身份执行命令**

```pkexec --user [username] [command]```

# SYNOPSIS

**polkit** [_options_]

# PARAMETERS

**pkexec**
> 以其他用户身份执行命令，需通过 polkit 授权。未指定用户时默认为 root。

**pkaction**
> 列出或查看已注册的 polkit 操作及其默认策略。

**pkcheck**
> 检查进程或系统总线名称是否有权执行给定操作。

**polkitd**
> 管理授权决策的 polkit 系统守护进程。以 polkitd 系统用户身份运行。

# DESCRIPTION

**polkit**（PolicyKit）是一个授权框架，允许非特权进程与特权进程进行通信。它对系统级权限提供细粒度控制，使桌面应用能够在获得用户适当授权的情况下执行管理任务。

与授予完整 root 权限的 sudo 不同，polkit 定义了具体的操作（如挂载磁盘或更改网络设置），并通过策略控制谁可以执行这些操作。该框架由 **pkexec**（执行特权命令）、**pkaction**（列出/查看操作）和 **pkcheck**（检查授权）组成。**polkitd** 守护进程以最小权限运行，并通过系统消息总线通信。

# CONFIGURATION

**/usr/share/polkit-1/actions/**
> 系统级的策略操作定义文件，采用 XML 格式。

**/etc/polkit-1/rules.d/**
> 本地授权规则，采用 JavaScript 格式（polkit >= 0.106）。

**/etc/polkit-1/localauthority/**
> 面向旧版 polkit 的 .pkla 授权文件（遗留格式）。

# CAVEATS

需要 polkitd 守护进程正在运行。桌面环境通常会提供用于图形化提示的身份验证代理。详细选项请参阅各命令的手册页。

# HISTORY

PolicyKit 由 **Red Hat** 的 **David Zeuthen** 创建，用于在 Linux 桌面系统上实现细粒度的授权控制。

# INSTALL

```dnf: sudo dnf install polkit```

```pacman: sudo pacman -S polkit```

```zypper: sudo zypper install polkit```

```brew: brew install polkit```

```nix: nix profile install nixpkgs#polkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkexec](/man/pkexec)(1), [pkaction](/man/pkaction)(1), [polkitd](/man/polkitd)(8)
