# TAGLINE

永久清空回收站

# TLDR

**清空所有回收站文件**

```trash-empty```

**清空 N 天前移入回收站的文件**

```trash-empty [days]```

**跳过确认提示**

```trash-empty -f```

**清空特定卷上的回收站**

```trash-empty --trash-dir=[/path/to/.Trash]```

# SYNOPSIS

**trash-empty** [_options_] [_days_]

# PARAMETERS

_days_
> 只删除超过指定天数前移入回收站的文件。

**-f**
> 删除前不要求确认。

**-i**, **--interactive**
> 删除每个文件前进行提示。

**--trash-dir** _DIR_
> 清空指定的回收站目录，而非默认的每用户/每卷位置。

**-v**, **--verbose**
> 删除时列出文件。

**--dry-run**
> 显示将要删除的内容，但不实际删除任何东西。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**trash-empty** 是 **trash-cli** 套件的一部分，用于永久删除回收站中的文件。不带参数时会清空所有回收站文件。若给定一个天数，则只删除早于该阈值的回收站文件，从而可以通过 cron 定期清理，同时保留近期项目以便恢复。

它作用于标准的 FreeDesktop.org 回收站位置，包括每用户和每卷的回收站目录。

# INSTALL

```dnf: sudo dnf install trash-cli```

```pacman: sudo pacman -S trash-cli```

```apk: sudo apk add trash-cli```

```zypper: sudo zypper install trash-cli```

```brew: brew install trash-cli```

```nix: nix profile install nixpkgs#trash-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trash](/man/trash)(1), [trash-list](/man/trash-list)(1), [trash-restore](/man/trash-restore)(1)
