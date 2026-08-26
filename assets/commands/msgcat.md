# TAGLINE

拼接和合并 gettext PO 文件

# TLDR

**拼接 PO 文件**

```msgcat [file1.po] [file2.po] -o [combined.po]```

**合并并处理重复消息**

```msgcat --use-first [file1.po] [file2.po] -o [output.po]```

**对消息排序**

```msgcat --sort-output [input.po] -o [sorted.po]```

**移除重复项**

```msgcat --unique [input.po] -o [output.po]```

# SYNOPSIS

**msgcat** [_options_] _inputfile_...

# PARAMETERS

**-o** _file_
> 输出文件。

**--use-first**
> 对重复消息采用第一个翻译。

**--sort-output**
> 按字母顺序排列消息。

**--unique**
> 移除重复消息。

**-t** _encoding_
> 输出编码。

# DESCRIPTION

**msgcat** 用于拼接和合并 gettext PO 文件。它组合多个翻译文件、处理重复项并规范化输出。属于 GNU gettext，用于管理国际化目录。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgattrib](/man/msgattrib)(1), [msgfmt](/man/msgfmt)(1), [msgunfmt](/man/msgunfmt)(1)
