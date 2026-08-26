# TAGLINE

通过命令过滤 PO 文件的翻译

# TLDR

**通过命令过滤翻译**

```msgfilter [sed -e 's/old/new/g'] < [input.po] > [output.po]```

**对消息应用过滤器**

```msgfilter -i [input.po] -o [output.po] [tr a-z A-Z]```

**保留文件头**

```msgfilter --keep-header [command] < [input.po]```

**处理特定消息**

```msgfilter --msgid [command] < [input.po]```

# SYNOPSIS

**msgfilter** [_options_] _filter-command_

# PARAMETERS

_FILTER-COMMAND_
> 用于过滤消息的命令。

**-i** _FILE_
> 输入的 PO 文件。

**-o** _FILE_
> 输出的 PO 文件。

**--keep-header**
> 保留 PO 文件头。

**--msgid**
> 过滤 msgid 而不是 msgstr。

**--help**
> 显示帮助信息。

# DESCRIPTION

**msgfilter** 通过命令过滤 PO 文件的翻译。它是 GNU gettext 的一部分。

该工具让每条 msgstr 经过一个过滤器处理，适合批量转换场景。

# CAVEATS

属于 gettext-tools。过滤器会作用于每条消息。可能破坏原有格式。

# HISTORY

msgfilter 是 **GNU gettext** 的一部分，可实现翻译的自动化转换。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgconv](/man/msgconv)(1), [msggrep](/man/msggrep)(1), [msguniq](/man/msguniq)(1)
