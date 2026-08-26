# TAGLINE

在 PO 文件中搜索消息

# TLDR

**搜索消息**

```msggrep -K -e "[pattern]" [input.po] -o [output.po]```

**在译文中搜索**

```msggrep -T -e "[pattern]" [input.po]```

**在源码引用中搜索**

```msggrep -N "[file.c]" [input.po]```

**反转匹配结果**

```msggrep -v -K -e "[pattern]" [input.po]```

**不区分大小写搜索**

```msggrep -K -e "[pattern]" -i [input.po]```

# SYNOPSIS

**msggrep** [_options_] [_inputfile_]

# PARAMETERS

_INPUTFILE_
> 要搜索的 PO 文件。

**-K**
> 在 msgid（键）中搜索。

**-T**
> 在 msgstr（译文）中搜索。

**-e** _PATTERN_
> 正则表达式模式。

**-N** _FILE_
> 按源码引用搜索。

**-v**
> 反转匹配结果。

**--help**
> 显示帮助信息。

# DESCRIPTION

**msggrep** 在 PO 文件中搜索消息。它是 GNU gettext 的一部分。

该工具按模式过滤消息，并将匹配的条目提取到新的 PO 文件中。

# CAVEATS

属于 gettext-tools。使用正则表达式语法。用 -K 搜索键，用 -T 搜索译文。

# HISTORY

msggrep 是 **GNU gettext** 的一部分，为翻译文件提供搜索功能。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgfilter](/man/msgfilter)(1), [msgconv](/man/msgconv)(1), [grep](/man/grep)(1)
