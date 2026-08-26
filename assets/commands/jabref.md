# TAGLINE

开源文献参考管理器

# TLDR

**启动 JabRef**

```jabref```

**打开文献库文件**

```jabref [library.bib]```

**从文件导入**

```jabref -i [refs.ris]```

**导出到文件**

```jabref -i [library.bib] -o [output.html]```

**通过在线抓取器获取条目**

```jabref --fetch=[arxiv]:[query]```

**以无界面模式运行**

```jabref --nogui -i [library.bib] -o [output.html]```

# SYNOPSIS

**jabref** [_options_] [_file_...]

# PARAMETERS

_file_
> 要打开的 BibTeX 文件。

**-i**, **--import** _file_[,_format_]
> 导入或加载文件，可指定格式。

**-o**, **--output** _file_[,_format_]
> 导出到文件，可指定格式。

**-m**, **--exportMatches** _[field]searchTerm,outputFile_
> 保存数据库中与搜索条件匹配的条目。

**-f**, **--fetch** _fetcher_:_query_
> 查询在线抓取器（如 arxiv、doi、pubmed）并导入结果。

**-a**, **--aux** _infile,outfile_ _base-file_
> 从 LaTeX .aux 文件提取子数据库。

**-g**, **--generateCitationKeys**
> 重新生成已打开文献库中的所有引用键。

**-b**, **--blank**
> 启动时不打开任何文件。

**-n**, **--nogui**
> 不显示 GUI，处理完命令后退出。

**-v**, **--version**
> 显示版本号。

**--debug**
> 启用调试级别日志。

**-h**, **--help**
> 显示帮助并列出支持的导入/导出格式。

# DESCRIPTION

**JabRef** 是一款开源文献参考管理器。它原生使用 BibTeX/BibLaTeX 格式，并可与 TeXstudio、Emacs 和 VS Code 等 LaTeX 编辑器集成。

JabRef 可以从多种格式（RIS、EndNote、PubMed）导入、从在线数据库抓取参考文献以及管理 PDF 附件。它支持分组、搜索和自动生成引用键。

# FEATURES

- BibTeX/BibLaTeX 原生格式
- 网络搜索（DOI、arXiv、PubMed）
- PDF 和文件管理
- 重复条目检测
- 自定义条目类型
- 共享数据库

# CAVEATS

需要 Java 运行时。大型文献库可能较慢。部分在线抓取器有速率限制。

# HISTORY

JabRef 由 **Morten O. Alver** 于 **2003 年**启动开发，作为商业参考管理器的开源替代品。它由开发者社区维护，在学术界颇受欢迎。

# INSTALL

```nix: nix profile install nixpkgs#jabref```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bibtex](/man/bibtex)(1), [zotero](/man/zotero)(1), [mendeley](/man/mendeley)(1)
