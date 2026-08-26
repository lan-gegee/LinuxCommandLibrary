# TAGLINE

Arch Linux 软件包管理器 pacman 的缓存清理工具

# TLDR

**从缓存中只保留最近 3 个软件包版本**

```sudo paccache -r```

**设置要保留的软件包版本数**

```sudo paccache -rk [num_versions]```

**执行试运行并列出待删除的候选软件包**

```paccache -d```

**移除已卸载软件包的所有缓存版本**

```sudo paccache -ruk0```

**将候选软件包移动到目录而不是删除**

```sudo paccache -m [path/to/directory]```

**带详细输出的试运行**

```paccache -dv```

# SYNOPSIS

**paccache** [_options_] [_targets_...]

# PARAMETERS

**-r**, **--remove**
> 从缓存中移除候选软件包

**-d**, **--dryrun**
> 执行试运行，仅列出候选对象

**-k**, **--keep** _num_
> 每个软件包保留 _num_ 个版本（默认：3）

**-m**, **--move** _dir_
> 将候选对象移动到 _dir_ 而不是删除

**-u**, **--uninstalled**
> 仅针对已卸载的软件包

**-c**, **--cachedir** _dir_
> 指定备用缓存目录

**-a**, **--arch** _arch_
> 按架构过滤软件包

**-v**, **--verbose**
> 显示被移除或移动的软件包

**-q**, **--quiet**
> 尽量减少输出

**-f**, **--force**
> 对 mv 和 rm 操作施加强制。

**-i** _pkgs_, **--ignore** _pkgs_
> 指定要忽略的软件包，以逗号分隔。使用 "-" 表示从标准输入读取。

**--nocolor**
> 输出中不使用颜色。

**--notime** _time_
> 保留 atime/mtime 不早于 _time_ 的软件包，即使超出 **--keep** 的数量。

**-z**, **--null**
> 输出使用 null 分隔符。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**paccache** 是 pacman（Arch Linux 软件包管理器）的缓存清理工具。它会从 pacman 缓存目录（/var/cache/pacman/pkg/）中移除旧版本的软件包，同时保留较新的版本以便可能需要回滚时使用。

默认情况下，每个软件包保留最近的 3 个版本。这样既能回收磁盘空间，又保留了在需要时降级软件包的能力。该工具可以针对所有缓存的软件包，也可以只针对系统中已不再安装的那些。

# CAVEATS

修改 pacman 缓存需要相应权限（通常是 root）。激进清理后，降级软件包可能需要重新下载旧版本。对于关键软件包，建议至少保留 1-2 个版本。

# HISTORY

属于 **pacman-contrib**，这是一组为 pacman 编写的脚本集合，之前包含在主 pacman 软件包中。后来被拆分为独立的软件包，以保持 pacman 核心的精简。对 Arch Linux 系统维护而言必不可少，因为缓存会随时间显著增长。

# SEE ALSO

[pacman](/man/pacman)(8), [pactree](/man/pactree)(8), [pacdiff](/man/pacdiff)(8)
