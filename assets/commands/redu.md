# TAGLINE

用于分析 restic 备份仓库磁盘占用的 TUI

# TLDR

**分析 restic 仓库**（使用 RESTIC_REPOSITORY 环境变量）

```redu```

**分析指定**仓库

```redu -r [path/to/restic/repo]```

**使用密码文件**

```redu -r [path/to/repo] --password-file [path/to/pwfile]```

**本次运行禁用缓存**

```redu --no-cache```

# SYNOPSIS

**redu** [_options_]

# PARAMETERS

**-r, --repo** _path_
> restic 仓库的路径或 URL。默认取 **RESTIC_REPOSITORY**。

**--password-file** _file_
> 从文件读取仓库密码。默认取 **RESTIC_PASSWORD_FILE**。

**--password-command** _cmd_
> 以该命令的输出作为仓库密码。

**--no-cache**
> 不使用也不写入 redu 缓存。

**-h, --help**
> 显示帮助信息。

**-V, --version**
> 显示版本信息。

# DESCRIPTION

**redu** 是一个用于分析 restic 备份仓库的终端用户界面。它聚合所有快照中的数据，找出各次备份中占用空间的文件、文件夹和条目。功能包括文件树浏览界面、跨快照的大小对比、标记要排除的文件，以及可加速后续运行的缓存系统。

# CAVEATS

需要可读的 restic 仓库。首次扫描大型仓库可能较慢；后续运行得益于 redu 的磁盘缓存会更快。

# HISTORY

**redu** 由 **drdo** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install redu```

```nix: nix profile install nixpkgs#redu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](/man/restic)(1), [ncdu](/man/ncdu)(1), [du](/man/du)(1)
