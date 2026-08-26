# TAGLINE

基于 Rust 的命令行回收站工具

# TLDR

将特定**文件**移入回收站

```trash [path/to/file]```

将**多个文件**移入回收站

```trash [path/to/file1] [path/to/file2]```

列出回收站中的项目

```trash list```

从回收站恢复特定文件

```trash restore [file]```

从回收站中删除特定文件

```trash empty [file]```

恢复回收站中的所有文件

```trash restore --all```

删除回收站中的所有文件

```trash empty --all```

# SYNOPSIS

**trash** [_command_] [_options_] [_files_...]

# PARAMETERS

**put** _files_
> 将文件移入回收站（未指定命令时的默认行为）

**list**
> 列出回收站中的项目

**restore** _files_
> 将文件从回收站恢复到原始位置

**empty** _files_
> 永久删除回收站中的文件

**--all**
> 应用于所有项目（配合 restore 或 empty 使用）

**-f**, **--force**
> 跳过确认提示

**-r**, **--recursive**
> 递归包含目录

**-v**, **--verbose**
> 显示详细输出

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**trashy** 是一个基于 Rust 的命令行回收站工具，通过将文件移入符合 XDG 回收站规范的回收站，提供了比 rm 更安全的替代方案。它实现现代、运行快速，并配有直观的子命令。

主命令 **trash** 默认将文件移入回收站。使用相应的子命令可以列出回收站中的文件、将其恢复到原始位置，或永久删除。它与桌面环境的回收站位置集成。

# CAVEATS

如果同时安装了 trash-cli，**trash** 命令名可能与之冲突。它使用的回收站目录与桌面文件管理器相同。在使用 **trash empty** 从回收站中移除文件之前，不会释放磁盘空间。

# HISTORY

由 oberblastmeister 用 **Rust** 编写，作为 trash-cli 的现代替代品。与 trash-cli 分离的多个命令相比，它的命令界面更简洁，追求速度和易用性。

# INSTALL

```nix: nix profile install nixpkgs#trashy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trash](/man/trash)(1), [rm](/man/rm)(1), [gio-trash](/man/gio-trash)(1)
