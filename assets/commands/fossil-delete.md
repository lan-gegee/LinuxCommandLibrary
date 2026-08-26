# TAGLINE

从版本控制中移除文件

# TLDR

**删除文件**

```fossil delete [file]```

**以 dry run 方式删除**

```fossil delete --dry-run [file]```

**强制删除**

```fossil delete -f [file]```

# SYNOPSIS

**fossil** **delete** [_options_] _file_...

# PARAMETERS

**-n**, **--dry-run**
> 显示将要发生的变化而不做任何修改。

**--hard**
> 同时从工作检出中删除文件，而不仅是版本控制。

**--soft**
> 保留工作检出中的文件（默认行为）。同时给出时覆盖 **--hard**。

**--case-sensitive** _BOOL_
> 文件名匹配时覆盖仓库的大小写敏感设置。

**--reset**
> 撤销先前未提交的删除——文件恢复到正常跟踪状态。不能与 **--verbose** 和 **--dry-run** 之外的标志组合使用。

**-v**, **--verbose**
> 与 **--reset** 配合，打印每个恢复的文件。

# DESCRIPTION

**fossil delete** 是 **fossil rm** 的别名。它安排文件在下次提交时从版本控制中移除。

提供此命令是为了方便和兼容性。所有选项和行为与 **fossil rm** 相同。默认情况下文件保留在磁盘上，只是从版本控制中移除。

# INSTALL

```apt: sudo apt install fossil```

```dnf: sudo dnf install fossil```

```pacman: sudo pacman -S fossil```

```apk: sudo apk add fossil```

```zypper: sudo zypper install fossil```

```brew: brew install fossil```

```nix: nix profile install nixpkgs#fossil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fossil-rm](/man/fossil-rm)(1), [fossil-add](/man/fossil-add)(1), [fossil-forget](/man/fossil-forget)(1), [fossil-commit](/man/fossil-commit)(1)
