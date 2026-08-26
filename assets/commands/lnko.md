# TAGLINE

简易的 stow 风格 dotfile 链接工具

# TLDR

**将软件包链接到主目录**

```lnko link [package1] [package2]```

**从指定源目录链接软件包到目标目录**

```lnko link -d [~/dotfiles] -t [~] [package_name]```

**取消某个包的链接**

```lnko unlink [package_name]```

**预览变更而不创建符号链接**

```lnko link -n [package_name]```

**显示所有包的状态**

```lnko status```

**移除孤儿符号链接**

```lnko clean```

**强制覆盖冲突文件**

```lnko link -f [package_name]```

# SYNOPSIS

**lnko** _command_ [_options_] [_package_ ...]

# PARAMETERS

**link**
> 从源包向目标目录创建相对符号链接。

**unlink**
> 移除指定包的符号链接。

**status**
> 显示所有包及其符号链接的当前状态。

**clean**
> 移除指向不存在目标的孤儿符号链接。

**-d**, **--dir** _dir_
> 指定包含包的源目录（默认：当前目录）。

**-t**, **--target** _dir_
> 指定符号链接的目标目录（默认：$HOME）。

**-n**, **--dry-run**
> 预览变更而不创建符号链接。

**-v**, **--verbose**
> 输出详细的调试信息。

**-b**, **--backup**
> 通过将已有文件备份到 .lnko-backup/ 来自动解决冲突。

**-s**, **--skip**
> 通过跳过冲突文件来自动解决冲突。

**-f**, **--force**
> 通过强制覆盖自动解决冲突。

**--ignore** _pattern_
> 排除匹配模式的文件（可重复使用）。

**--no-folding**
> 阻止将目录折叠为单个符号链接。

# DESCRIPTION

**lnko** 是一个简易的 stow 风格 dotfile 链接工具，它从包含包的源目录向目标目录创建相对符号链接。每个包是一个目录，其内容镜像目标目录的结构。

它支持目录树折叠、忽略模式、dry-run 模式以及多种冲突解决策略。检测到冲突时，若未指定自动解决标志，lnko 会提供交互式提示，可选择备份、跳过、覆盖和 diff。与已有的 GNU Stow 符号链接兼容。

# CAVEATS

需要安装 Lua 和 LuaFileSystem。

# HISTORY

**lnko** 由 **luanvil** 创建，采用 **Lua** 编写。

# SEE ALSO

[stow](/man/stow)(8), [ln](/man/ln)(1)
