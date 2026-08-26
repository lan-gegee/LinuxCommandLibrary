# TAGLINE

移除 PO 文件中的重复翻译

# TLDR

**移除重复消息**

```msguniq [input.po] -o [output.po]```

**保留第一次出现的条目**

```msguniq -u [input.po] -o [output.po]```

**报告重复项**

```msguniq -d [input.po]```

**对输出排序**

```msguniq -s [input.po] -o [output.po]```

**按 msgid 和 msgctxt 去重**

```msguniq --use-first [input.po] -o [output.po]```

# SYNOPSIS

**msguniq** [_options_] [_inputfile_]

# PARAMETERS

_INPUTFILE_
> 要处理的 PO 文件。

**-o** _FILE_
> 输出文件。

**-u**
> 只保留唯一的消息。

**-d**
> 报告重复的消息。

**-s**
> 对输出排序。

**--use-first**
> 对重复项采用第一个。

**--help**
> 显示帮助信息。

# DESCRIPTION

**msguniq** 移除 PO 文件中的重复翻译。它是 GNU gettext 的一部分。

该工具统一消息条目，通过合并或选择的方式处理重复项。

# CAVEATS

属于 gettext-tools。不同的重复项会被合并，可能需要人工复核。

# HISTORY

msguniq 是 **GNU gettext** 的一部分，帮助保持翻译文件的整洁。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgcat](/man/msgcat)(1), [msgmerge](/man/msgmerge)(1), [msgfilter](/man/msgfilter)(1)
