# TAGLINE

带进度条的现代快速文件复制工具

# TLDR

**复制**单个文件

```cpx [source.txt] [dest.txt]```

**递归复制**目录

```cpx -r [source_dir/] [dest_dir/]```

**按排除模式复制**

```cpx -r -e "node_modules" -e ".git" [project/] [/backup/]```

**恢复**中断的传输

```cpx -r --resume [large_dataset/] [/backup/]```

**保留**所有文件属性

```cpx -r -p=all [photos/] [/backup/photos/]```

使用 8 线程**并行**复制

```cpx -r -j 8 [source/] [dest/]```

# SYNOPSIS

**cpx** [_OPTIONS_] _SOURCE_... _DESTINATION_

# PARAMETERS

**-r**, **--recursive**
> 递归复制目录。

**-j** _N_
> 并行操作的数量（默认：4）。

**--resume**
> 通过校验和验证恢复中断的传输。

**-f**, **--force**
> 若目标不可用则删除并重试。

**-i**, **--interactive**
> 覆盖前提示确认。

**-t**, **--target-directory** _DIR_
> 将所有源文件复制到指定目录。

**-e**, **--exclude** _PATTERN_
> 排除匹配的文件（glob 模式，逗号分隔）。

**-s**, **--symbolic-link** [_MODE_]
> 创建符号链接而非复制（auto/absolute/relative）。

**-l**, **--link**
> 创建硬链接而非复制。

**-P**, **--no-dereference**
> 从不跟随源符号链接。

**-L**, **--dereference**
> 总是跟随源符号链接。

**-p**, **--preserve** [_ATTRS_]
> 保留属性（default/all/mode/timestamps/ownership/links/xattr）。

**-b**, **--backup** [_MODE_]
> 备份已有文件（none/simple/numbered/existing）。

**--reflink** [_WHEN_]
> 若支持则写时复制（auto/always/never）。

**--parents**
> 保留完整的源路径结构。

**--no-config**
> 忽略所有配置文件。

# DESCRIPTION

**cpx** 是传统 **cp** 命令的现代替代品，以 Rust 编写，注重性能与安全。它提供并行文件复制（基准测试中最高可达标准 cp 的 5 倍速度）、可视化进度条、借助校验和验证恢复中断传输的能力、优雅的 Ctrl+C 处理与恢复提示，以及 gitignore 风格的排除模式。

# CONFIGURATION

支持三个层级的配置（按优先级排序）：**./cpxconfig.toml**（项目级）、**~/.config/cpx/cpxconfig.toml**（用户级）、**/etc/cpx/cpxconfig.toml**（系统级）。可通过 **cpx config init**、**cpx config show** 和 **cpx config path** 管理。

# CAVEATS

目前仅完整支持 Linux（建议内核 4.5 及以上）。macOS 和 Windows 支持已在计划中但尚未提供。**--resume** 功能依赖校验和，会给小文件带来额外开销。并非在所有边缘情况下都能作为 **cp** 的直接替代别名。

# HISTORY

**cpx** 由 **Bhuminjay Soni** 创建，于 **2026 年 1 月**前后公开发布。使用 Rust 编写，采用 MIT 许可证。最新版本为 v0.1.4（2026 年 2 月）。可通过 Cargo、AUR（名为 cpx-copy）、Nix 以及预编译二进制获取。

# INSTALL

```nix: nix profile install nixpkgs#cpx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cp](/man/cp)(1), [rsync](/man/rsync)(1), [mv](/man/mv)(1), [pv](/man/pv)(1)
