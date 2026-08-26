# TAGLINE

通过 FUSE 以不同的所有者和权限挂载目录

# TLDR

**将目录挂载**到另一个位置

```sudo bindfs /path/to/source /path/to/mount```

以**用户映射**方式挂载

```sudo bindfs --map=user1/user2 /path/to/source /path/to/mount```

强制所有文件显示为属于指定的**用户和组**

```sudo bindfs --force-user=user --force-group=group /path/to/source /path/to/mount```

以修改过的**权限**挂载

```sudo bindfs --perms=0755 /path/to/source /path/to/mount```

以**只读**方式挂载

```bindfs -o ro /path/to/source /path/to/mount```

**卸载**

```sudo umount /path/to/mount```

# SYNOPSIS

**bindfs** [_OPTIONS_] _source_ _mountpoint_

# DESCRIPTION

**bindfs** 将一个目录挂载到另一位置，并赋予不同的所有者和权限。它使用 FUSE 创建一个经过权限修改的目录树视图。

# PARAMETERS

**--map=** _user1/user2_
> 将所有权从 user1 映射为 user2。

**--force-user=** _user_
> 强制所有文件显示为属于 user。

**--force-group=** _group_
> 强制所有文件显示为属于 group。

**--perms=** _mode_
> 为所有文件设置权限位（八进制或符号形式）。

**--create-as-user**
> 将新文件的所有者/组改为调用者的 uid/gid。

**--resolve-symlinks**
> 解析源目录中的符号链接。

**--enable-ioctl**
> 将 ioctl 调用转发到底层文件系统。

**-r**, **-o ro**
> 以只读方式挂载。

**-o** _options_
> 传递 FUSE 挂载选项。

**--multithreaded**
> 以多线程模式运行 bindfs。

# CAVEATS

所有权映射的更改是双向的——新创建的文件会被映射回原状。需要 FUSE 支持。使用 umount 卸载 bindfs 文件系统。

# HISTORY

**bindfs** 是一个 FUSE 文件系统，用于以修改后的权限挂载目录。

# INSTALL

```apt: sudo apt install bindfs```

```dnf: sudo dnf install bindfs```

```zypper: sudo zypper install bindfs```

```brew: brew install bindfs```

```nix: nix profile install nixpkgs#bindfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [fusermount](/man/fusermount)(1)
