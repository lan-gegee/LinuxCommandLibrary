# TAGLINE

FUSE 文件系统挂载管理器

# TLDR

**卸载 FUSE 文件系统**

```fusermount -u [mountpoint]```

**强制卸载**（延迟卸载）

```fusermount -uz [mountpoint]```

**显示版本**

```fusermount -V```

**列出所有 FUSE 挂载**

```mount -t fuse```

**带选项卸载**

```fusermount -u -o [option] [mountpoint]```

# SYNOPSIS

**fusermount** [_options_] _mountpoint_

# DESCRIPTION

**fusermount** 是一个用于挂载和卸载 FUSE（用户空间文件系统）的工具。它主要用于卸载操作，因为挂载通常由文件系统程序自身完成。

该工具让非 root 用户也能挂载和卸载文件系统，前提是拥有适当的权限和配置。

# PARAMETERS

**-u**
> 卸载文件系统。

**-z**
> 延迟卸载（类似 umount -l）。

**-q**
> 安静模式。

**-o** _options_
> 挂载选项。

**-V**
> 显示版本。

**-h**
> 显示帮助。

# CONFIGURATION

**/etc/fuse.conf**
> 控制系统级 FUSE 设置，包括 user_allow_other 和 mount_max。

# CAVEATS

延迟卸载可能使文件系统仍处于使用状态。普通用户需要适当的权限。某些选项需要 root。挂载必须来自 fusermount 或启用了 user_allow_other。

# HISTORY

**fusermount** 属于 **FUSE**（用户空间文件系统）项目，由 **Miklos Szeredi** 于 **2001 年**前后创建。FUSE 让用户空间程序能够向内核导出文件系统，彻底改变了 Linux 上的文件系统开发方式。

# INSTALL

```apt: sudo apt install fuse3```

```dnf: sudo dnf install fuse3```

```pacman: sudo pacman -S fuse3```

```apk: sudo apk add fuse```

```zypper: sudo zypper install fuse3```

```nix: nix profile install nixpkgs#fuse3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(1), [umount](/man/umount)(1), [sshfs](/man/sshfs)(1), [encfs](/man/encfs)(1)

# RESOURCES

```[Source code](https://github.com/libfuse/libfuse)```

<!-- verified: 2026-07-15 -->
