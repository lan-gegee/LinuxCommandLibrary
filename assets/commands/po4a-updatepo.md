# TLDR

# TAGLINE

让 PO 文件与变更后的文档保持同步

# TLDR

根据源文件的修改**更新** PO 文件

```po4a-updatepo --format [text] --master [path/to/master.txt] --po [path/to/result.po]```

**列出**可用格式

```po4a-updatepo --help-format```

根据各自源文件的修改**更新**多个 PO 文件

```po4a-updatepo --format [text] --master [path/to/master.txt] --po [path/to/po1.po] --po [path/to/po2.po]```

# SYNOPSIS

**po4a-updatepo** [_options_] **-f** _format_ **-m** _master_ **-p** _po_ [**-p** _po2_ ...]

# PARAMETERS

**-f, --format _format_**
> 主文档的格式（text、pod、man、sgml、xml 等）

**-m, --master _file_**
> 主（原始）文档的路径

**-p, --po _file_**
> 要更新的 PO 文件的路径（可多次指定）

**--help-format**
> 列出可用的文档格式

**-M, --master-charset _charset_**
> 主文档的字符集

**--previous**
> 在 PO 文件中保留先前的 msgid 字符串以供参考

**--no-deprecation**
> 不添加弃用注释

# DESCRIPTION

**po4a-updatepo** 在原始主文档发生变化时更新翻译用的 PO 文件。它从当前主文档中提取可翻译字符串并与现有译文合并，适当地标记过时、模糊和新出现的字符串。

该工具是 **po4a**（PO for anything）套件的一部分，便于使用 gettext 方法论进行文档翻译。当源文档被修改时，译者使用此工具同步其 PO 文件，并查看哪些翻译需要更新。

# CAVEATS

运行此工具会直接修改 PO 文件。如有需要，请在运行前备份 PO 文件。略有改动的字符串会被标记为 fuzzy，需要译者审阅。主文档格式必须与创建 PO 文件时使用的格式一致。

# INSTALL

```dnf: sudo dnf install po4a```

```pacman: sudo pacman -S po4a```

```apk: sudo apk add po4a```

```zypper: sudo zypper install po4a```

```brew: brew install po4a```

```nix: nix profile install nixpkgs#po4a```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[po4a](/man/po4a)(1), [po4a-gettextize](/man/po4a-gettextize)(1), [po4a-translate](/man/po4a-translate)(1), [msgmerge](/man/msgmerge)(1)
