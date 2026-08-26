# TAGLINE

从系统中删除用户账户

# TLDR

**移除**用户

```sudo userdel username```

连同**主目录**和邮件池一并移除用户

```sudo userdel -r username```

即使用户已登录也**强制**移除

```sudo userdel -f username```

在 **chroot** 环境中移除用户

```sudo userdel -R /path/to/chroot username```

# SYNOPSIS

**userdel** [_options_] _LOGIN_

# DESCRIPTION

**userdel** 删除用户账户，并从系统文件中清除相关条目。在 Debian 系统上，人们通常更倾向于使用更高层的 **deluser** 命令。

# PARAMETERS

**-f, --force**
> 强制移除，即使用户已登录；并且无论属主是谁都会删除主目录和邮件池

**-r, --remove**
> 移除主目录和邮件池

**-R, --root CHROOT_DIR**
> 在 chroot 环境中应用更改

**-P, --prefix PREFIX_DIR**
> 在前缀目录中应用更改

**-Z, --selinux-user**
> 移除该用户的全部 SELinux 用户映射

**--selinux-range**
> 移除该用户的 SELinux MLS 范围映射

**-h, --help**
> 显示帮助信息

# CAVEATS

**-f** 选项非常危险，可能使系统处于不一致状态。主目录之外的用户文件不会被自动删除。删除前应先终止该用户拥有的正在运行的进程。

# HISTORY

**userdel** 属于 **shadow-utils** 软件包。在 Debian 系统上，**deluser** 还提供了创建备份等额外功能。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[deluser](/man/deluser)(8), [useradd](/man/useradd)(8), [usermod](/man/usermod)(8), [groupdel](/man/groupdel)(8)
