# TAGLINE

命令行文献管理器

# TLDR

**从文件添加文档**

```papis add [document.pdf]```

**添加文档并写入元数据**

```papis add --set author "[Name]" --set title "[Title]" [document.pdf]```

**通过 DOI 添加文档**

```papis add --from doi [10.1007/s00214-007-0422-6]```

**搜索并打开文档**

```papis open "[query]"```

**导出为 BibTeX**

```papis export --format bibtex "[query]"```

**编辑文档元数据**

```papis edit "[query]"```

**列出匹配查询的所有文档**

```papis list "[query]"```

# SYNOPSIS

**papis** _command_ [_options_] [_args_]

# PARAMETERS

**add**
> 添加文档。

**open**
> 打开文档。

**edit**
> 编辑元数据。

**export**
> 导出参考文献。

**list**
> 列出文档。

**browse**
> 在浏览器中打开。

**rm**
> 删除文档。

**rename**
> 重命名文档文件夹。

**doctor**
> 检查并修复文档元数据。

**cite**
> 获取引用信息。

**--set** _field_ _value_
> 设置元数据字段。

**-l**, **--lib** _library_
> 使用指定的库。

**--from** _importer_
> 从以下来源导入：doi、arxiv、bibtex、crossref、pmid、yaml、folder、pdf2doi。

# DESCRIPTION

**papis** 是一个命令行文献管理器。它把文档和元数据存储在文件夹结构中，支持多个库，并能与编辑器和参考文献管理器集成。

# LIBRARY STRUCTURE

```
~/Documents/papers/
├── author2023title/
│   ├── info.yaml
│   └── document.pdf
```

# CONFIGURATION

```yaml
# ~/.config/papis/config
[papers]
dir = ~/Documents/papers

[books]
dir = ~/Documents/books
```

# CAVEATS

需要 Python。支持多库管理。可与 Vim、Emacs 集成，并提供 TUI 界面。支持 DOI 和 arXiv 查询。

# HISTORY

papis 由 **Alejandro Gallo** 开发，定位为 Zotero 等 GUI 文献管理器的命令行替代品。

# INSTALL

```brew: brew install papis```

```nix: nix profile install nixpkgs#papis```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zotero](/man/zotero)(1), [jabref](/man/jabref)(1), [mendeley](/man/mendeley)(1)
