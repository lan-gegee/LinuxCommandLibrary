# TAGLINE

控制文件系统页缓存

# TLDR

**查看文件缓存状态**

```vmtouch [file]```

**将文件加载到缓存**

```vmtouch -t [file]```

**从缓存中逐出**

```vmtouch -e [file]```

**锁定在内存中**

```vmtouch -l [file]```

**详细输出**

```vmtouch -v [file]```

**检查目录**

```vmtouch [directory/]```

# SYNOPSIS

**vmtouch** [_-t_] [_-e_] [_-l_] [_-v_] _files_

# PARAMETERS

**-t**
> 触碰（加载到缓存）。

**-e**
> 从缓存中逐出。

**-l**
> 锁定在内存中。

**-v**
> 详细输出。

**-q**
> 安静模式。

**-m** _SIZE_
> 最大内存。

# DESCRIPTION

**vmtouch** 是一个用于检查和操控 Linux 文件系统页缓存的工具。它可以报告文件或目录的哪些页当前驻留在内存中，让你了解操作系统为快速访问缓存了哪些内容。

除了检查之外，vmtouch 还能主动管理缓存：通过 touch 将文件加载进内存，通过 evict 释放已缓存的页，或把文件锁定在 RAM 中以防止内核将其换出。因此它可用于在高流量事件前预热缓存、确保关键数据常驻内存，或为基准测试清除缓存数据。

该工具既可作用于单个文件，也可作用于整个目录树，并在详细模式下显示每个文件的缓存驻留统计。将页锁定在内存需要 root 权限，且受系统内存限制约束。

# CAVEATS

加锁需要 root 权限。仅限 Linux 特有功能。只针对页缓存。

# HISTORY

**vmtouch** 由 **Doug Hoyte** 创建，用于在命令行控制文件系统缓存。

# INSTALL

```apt: sudo apt install vmtouch```

```dnf: sudo dnf install vmtouch```

```zypper: sudo zypper install vmtouch```

```brew: brew install vmtouch```

```nix: nix profile install nixpkgs#vmtouch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[free](/man/free)(1), [sync](/man/sync)(1), [dd](/man/dd)(1)
