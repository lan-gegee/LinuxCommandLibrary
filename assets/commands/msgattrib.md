# TAGLINE

按消息属性过滤 gettext PO 文件

# TLDR

**提取已翻译的消息**

```msgattrib --translated [input.po] -o [output.po]```

**提取未翻译的消息**

```msgattrib --untranslated [input.po] -o [output.po]```

**提取 fuzzy 消息**

```msgattrib --fuzzy [input.po] -o [output.po]```

**清除 fuzzy 标记**

```msgattrib --clear-fuzzy [input.po] -o [output.po]```

# SYNOPSIS

**msgattrib** [_options_] _inputfile_

# PARAMETERS

**--translated**
> 只保留已翻译的消息。

**--untranslated**
> 只保留未翻译的消息。

**--fuzzy**
> 只保留 fuzzy 消息。

**--clear-fuzzy**
> 移除 fuzzy 标记。

**--set-fuzzy**
> 设置 fuzzy 标记。

**-o** _file_
> 输出文件。

# DESCRIPTION

**msgattrib** 按消息属性过滤 gettext PO 文件。根据翻译状态（已翻译、fuzzy、已废弃）提取或修改消息。属于 GNU gettext，用于国际化工作流。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgcat](/man/msgcat)(1), [msgfmt](/man/msgfmt)(1), [msgunfmt](/man/msgunfmt)(1)
