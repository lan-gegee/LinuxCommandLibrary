# TAGLINE

文献管理器与学术社交网络

# TLDR

**启动 Mendeley Desktop**

```mendeleydesktop```

**打开指定数据库**

```mendeleydesktop --db [database.sqlite]```

**以最小化方式启动**

```mendeleydesktop --start-minimized```

# SYNOPSIS

**mendeleydesktop** [_options_]

# PARAMETERS

**--db** _file_
> 指定数据库文件。

**--start-minimized**
> 启动后最小化到托盘。

**--help**
> 显示帮助。

# DESCRIPTION

**Mendeley** 是一款文献管理器兼学术社交网络。Mendeley Desktop 帮助研究人员整理 PDF、生成引文、与他人协作并发现新的研究。

它支持跨设备同步，并与文字处理软件集成以便插入引文。

# KEY FEATURES

```
- PDF organization and annotation
- Citation generation (BibTeX, etc.)
- Word processor plugins
- Cloud sync
- Research discovery
```

# FILE LOCATIONS

```
~/.local/share/data/Mendeley Ltd./Mendeley Desktop/
```

# CAVEATS

需要 Elsevier 账户。免费版的同步存储空间有限。桌面应用正逐步被网页版取代。

# HISTORY

Mendeley 于 **2007 年**由 **Victor Henning**、**Jan Reichelt** 和 **Paul Foeckler** 在伦敦创立，**2013 年**被 **Elsevier** 收购。

# INSTALL

```nix: nix profile install nixpkgs#mendeley```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zotero](/man/zotero)(1), [jabref](/man/jabref)(1), [papis](/man/papis)(1)
