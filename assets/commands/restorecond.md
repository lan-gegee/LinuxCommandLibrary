# TAGLINE

在文件创建时恢复 SELinux 上下文的守护进程

# TLDR

启动 **restorecond** 守护进程

```sudo restorecond```

以**详细**模式运行以查看恢复事件

```sudo restorecond -v```

以**调试**模式运行

```sudo restorecond -d```

使用**替代的**配置文件

```sudo restorecond -f [restorecond_file]```

检查 restorecond 服务的**状态**

```sudo systemctl status restorecond```

**启用** restorecond 开机自启

```sudo systemctl enable restorecond --now```

# SYNOPSIS

**restorecond** [**-d**] [**-f** _restorecond_file_] [**-u**] [**-v**]

# PARAMETERS

**-d**
> 调试模式；以前台方式运行并输出详细信息

**-f** _file_
> 使用替代的配置文件而不是 /etc/selinux/restorecond.conf

**-u**
> 监视用户主目录（~）中的文件创建

**-v**
> 详细模式；显示恢复事件

**-F**
> 强制模式；不检查设备号

# DESCRIPTION

**restorecond** 是一个 SELinux 守护进程，它使用 inotify 监视文件创建事件，并自动为新创建的文件恢复正确的 SELinux 安全上下文。对于应用程序频繁创建上下文不正确的文件的目录，该工具非常有用。

守护进程从 /etc/selinux/restorecond.conf 读取配置，其中列出了要监视的文件和目录。当创建或修改了匹配配置的文件时，restorecond 会根据 SELinux 策略应用正确的上下文。

# CONFIGURATION

**/etc/selinux/restorecond.conf**
> 列出要监视创建事件的文件路径和目录。每行一个路径；与这些路径匹配的新建文件的 SELinux 上下文会被自动恢复。

**/etc/selinux/restorecond_user.conf**
> 当 restorecond 带 **-u** 标志监视用户主目录时使用的每用户监视列表。

# CAVEATS

需要 SELinux 处于 enforcing 或 permissive 模式。系统级配置必须以 root 运行。只监视配置文件中明确列出的路径（不支持通配符展开）。在现代基于 systemd 的发行版上，**restorecond** 已在很大程度上被 **systemd file restore** 规则以及软件包安装期间的 **restorecon -R** 取代；在依赖该守护进程之前请先确认你的发行版是否仍提供它。

# HISTORY

属于 Red Hat 开发的 SELinux 策略核心工具包 **policycoreutils** 的一部分。用于解决应用程序创建安全上下文不正确的文件的问题——这类问题可能导致 SELinux 下的访问被拒绝。

# INSTALL

```apt: sudo apt install restorecond```

```zypper: sudo zypper install restorecond```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restorecon](/man/restorecon)(8), [semanage-fcontext](/man/semanage-fcontext)(8), [semanage](/man/semanage)(8)
