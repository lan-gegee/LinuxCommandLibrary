# TAGLINE

将工作树缩减为已跟踪文件的一个子集

# TLDR

**启用稀疏检出并设置目录**（cone 模式）

```git sparse-checkout set [dir1] [dir2]```

**向稀疏检出添加更多目录**

```git sparse-checkout add [dir]```

**列出当前的稀疏模式**

```git sparse-checkout list```

**配置更改后重新应用稀疏模式**

```git sparse-checkout reapply```

**禁用稀疏检出**并恢复所有文件

```git sparse-checkout disable```

**检查哪些路径符合稀疏规则**

```echo "[path/to/file]" | git sparse-checkout check-rules```

**预览稀疏定义之外**会被移除的文件

```git sparse-checkout clean --dry-run```

# SYNOPSIS

**git** **sparse-checkout** (_init_ | _list_ | _set_ | _add_ | _reapply_ | _disable_ | _check-rules_ | _clean_) [_options_]

# SUBCOMMANDS

**init**
> 已弃用。请改用 set 来启用并配置稀疏检出。

**set**
> 定义工作树中要包含哪些目录/模式。

**add**
> 向稀疏检出添加更多目录/模式。

**list**
> 列出当前的稀疏检出模式。

**disable**
> 禁用稀疏检出并恢复所有文件。

**reapply**
> 手动修改配置后重新应用模式。

**check-rules**
> 检查路径是否符合当前的稀疏规则。

**clean**
> 移除稀疏检出定义之外的文件。除非 clean.requireForce 为 false，否则需要 -f。

# PARAMETERS

**--cone**
> 使用基于目录模式的 cone 模式（默认，速度更快）。

**--no-cone**
> 使用完整模式匹配，支持任意 gitignore 风格的模式。

**--sparse-index**
> 启用稀疏索引格式以提升性能。

**--no-sparse-index**
> 禁用稀疏索引格式，以兼容外部工具。

**--stdin**
> 从 stdin 读取模式（每行一个），而不是从参数读取。

**-f**, **--force**
> 允许在没有 clean.requireForce 配置的情况下执行清理（用于 clean 子命令）。

**--dry-run**
> 预览 clean 将移除的内容，但不实际删除任何东西。

**--rules-file** _file_
> 与指定文件中的规则进行匹配，而不是当前规则（用于 check-rules）。

**-z**
> stdin 输入和输出使用以 NUL 结尾的路径（用于 check-rules）。

# DESCRIPTION

**git sparse-checkout** 支持部分仓库检出，即只有指定的目录和文件会出现在工作树中。对于大型 monorepo，这能显著减小工作目录的体积。

cone 模式（默认）将模式限定为按目录包含，比完整模式匹配更快也更简单。在 cone 模式下，set 和 add 子命令接受的是目录名而非任意 gitignore 模式。非 cone 模式（--no-cone）允许任意 gitignore 风格的模式，但由于性能差、语义令人困惑，已被弃用。

该命令是实验性的。其行为未来可能发生变化。

# CONFIGURATION

**.git/info/sparse-checkout**
> 存放稀疏检出模式的文件，控制哪些路径会被检出。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-read-tree](/man/git-read-tree)(1), [git-checkout](/man/git-checkout)(1), [git-clone](/man/git-clone)(1), [git-worktree](/man/git-worktree)(1)
