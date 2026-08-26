# TAGLINE

带自动文件系统挂载的增强版 chroot

# TLDR

在新根目录中启动**交互式 Shell**

```arch-chroot [path/to/new_root]```

指定运行 Shell 的**用户**

```arch-chroot -u [user] [path/to/new_root]```

在新根目录中运行**自定义命令**

```arch-chroot [path/to/new_root] [command] [arguments]```

指定其他 **Shell**

```arch-chroot [path/to/new_root] zsh```

# SYNOPSIS

**arch-chroot** [_-u user_] _new_root_ [_command_]

# DESCRIPTION

**arch-chroot** 是一个增强的 chroot 封装工具，旨在简化 Arch Linux 的安装与恢复过程。与普通的 chroot 不同，它会在进入 chroot 环境前自动挂载必要的 API 文件系统（/proc、/sys、/dev、/dev/pts 和 /run），并在退出时干净地卸载它们。

这大大简化了在已挂载根文件系统上执行系统管理任务的过程，例如安装软件包、配置引导加载程序，或从 live 环境修复损坏的系统。它还可以运行单条命令后退出，或以指定用户身份启动交互式 Shell。

# PARAMETERS

**new_root**
> 用作新根文件系统的目录路径

**-u** _user_[:_group_]
> 以指定的非 root 用户及可选组运行 Shell 或命令。

**-N**
> Unshare 模式：用 unshare 创建新的挂载命名空间和用户命名空间，允许非 root 用户运行 arch-chroot。

**command**
> 可选命令，用于替代默认 Shell（Bash）

# CAVEATS

属于 **arch-install-scripts** 软件包。自动挂载 /proc、/sys、/dev、/dev/pts 和 /run。目标目录必须包含有效的 Linux 根文件系统。

# HISTORY

属于为 **Arch Linux** 开发的 **arch-install-scripts** 软件包，旨在简化安装过程和系统恢复任务。

# INSTALL

```dnf: sudo dnf install arch-install-scripts```

```pacman: sudo pacman -S arch-install-scripts```

```apk: sudo apk add arch-install-scripts```

```zypper: sudo zypper install arch-install-scripts```

```nix: nix profile install nixpkgs#arch-install-scripts```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[chroot](/man/chroot)(1), [systemd-nspawn](/man/systemd-nspawn)(1), [pacstrap](/man/pacstrap)(8)
