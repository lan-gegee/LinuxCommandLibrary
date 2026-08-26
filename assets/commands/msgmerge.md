# TAGLINE

合并两个 Uniforum 风格的 PO 文件

# TLDR

**将翻译与模板合并**

```msgmerge [old.po] [new.pot] -o [merged.po]```

**就地更新 PO 文件**

```msgmerge -U [existing.po] [template.pot]```

**合并时不使用模糊匹配**

```msgmerge -N [old.po] [new.pot] -o [merged.po]```

模糊匹配时**保留先前的 msgid**

```msgmerge --previous [old.po] [new.pot] -o [merged.po]```

更新前**进行备份**

```msgmerge -U --backup=numbered [file.po] [template.pot]```

**使用翻译汇编库**

```msgmerge -C [compendium.po] [old.po] [new.pot] -o [merged.po]```

**安静模式**

```msgmerge -q [old.po] [new.pot] -o [merged.po]```

# SYNOPSIS

**msgmerge** [_options_] _def.po_ _ref.pot_

# PARAMETERS

_DEF.PO_
> 已有的翻译文件。

_REF.POT_
> 参考模板文件。

**-o** _FILE_
> 输出文件。

**-U**, **--update**
> 就地更新 def.po。

**-N**, **--no-fuzzy-matching**
> 不使用模糊匹配。可显著加快运行速度。

**--previous**
> 添加 fuzzy 标记时保留已翻译消息先前的 msgid。

**-C** _FILE_, **--compendium**=_FILE_
> 额外的消息翻译库。可多次指定。

**--backup**=_CONTROL_
> -U 的备份控制方式：**none**、**numbered**、**existing** 或 **simple**。

**--suffix**=_SUFFIX_
> 覆盖常规的备份后缀。

**-q**, **--quiet**
> 抑制进度指示信息。

**-v**, **--verbose**
> 提高详细程度级别。

**--no-wrap**
> 不对长的消息行折行。

**-s**, **--sort-output**
> 生成排序后的输出。

**-F**, **--sort-by-file**
> 按文件位置排序输出。

# DESCRIPTION

**msgmerge** 将两个 Uniforum 风格的 .po 文件合并在一起。它是 **GNU gettext** 的一部分。

_def.po_ 文件是已有的 PO 翻译文件，其中仍然匹配的翻译会被带入新创建的文件。_ref.pot_ 文件是最近生成的、带有最新源码引用的 PO 模板文件。_def.po_ 中的注释会被保留。找不到精确匹配时会采用模糊匹配以获得更好的结果（除非指定了 **-N**）。

# CAVEATS

属于 **gettext-tools** 软件包。模糊匹配会以 **#, fuzzy** 注释标出，应人工复核。**-U** 标志会就地修改输入文件；更新前请用 **--backup** 创建备份。

# HISTORY

msgmerge 是 **GNU gettext** 的一部分，对于在软件更新过程中维护翻译文件不可或缺。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msginit](/man/msginit)(1), [msgfmt](/man/msgfmt)(1), [msgcat](/man/msgcat)(1), [xgettext](/man/xgettext)(1)
