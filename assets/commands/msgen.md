# TAGLINE

创建英语翻译 PO 文件

# TLDR

**创建英语翻译文件**

```msgen [input.pot] -o [en.po]```

**从 PO 文件生成**

```msgen [source.po] -o [output.po]```

**强制输出**

```msgen --force-po [input.pot] -o [output.po]```

**指定语言**

```msgen --lang=[en] [input.pot] -o [output.po]```

# SYNOPSIS

**msgen** [_options_] [_inputfile_]

# PARAMETERS

_INPUTFILE_
> 输入的 POT 或 PO 文件。

**-o** _FILE_
> 输出文件。

**--force-po**
> 即使为空也写出 PO 文件。

**--lang** _LANG_
> 设置语言代码。

**--help**
> 显示帮助信息。

# DESCRIPTION

**msgen** 创建英语翻译 PO 文件。它将 msgid 复制到 msgstr，用于同语言的翻译。

该工具生成基础英语文件。属于 GNU gettext，用于 i18n 工作流。

# CAVEATS

属于 gettext-tools。仅适用于英语目标。用于 en_* 语言环境。

# HISTORY

msgen 是 **GNU gettext** 的一部分，为简化英语语言环境文件的生成而创建。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgconv](/man/msgconv)(1), [msgfmt](/man/msgfmt)(1), [msgmerge](/man/msgmerge)(1)
