# TAGLINE

以一致的缩进格式化 LaTeX 源代码

# TLDR

**格式化 LaTeX 文件**

```latexindent [document.tex]```

**格式化并原地保存**

```latexindent -w [document.tex]```

**使用本地设置格式化**

```latexindent -l [document.tex]```

**指定输出文件**

```latexindent [input.tex] -o [output.tex]```

**静默输出**

```latexindent -s [document.tex]```

**将备份和日志文件发送到其他目录**

```latexindent -c [path/to/cruft/dir/] [document.tex]```

**仅在内容变化时覆盖**

```latexindent -wd [document.tex]```

# SYNOPSIS

**latexindent** [_options_] _file_

# PARAMETERS

**-w**, **--overwrite**
> 覆盖原文件（会先创建备份）。

**-wd**, **--overwriteIfDifferent**
> 仅当缩进后的文本有所不同时才覆盖原文件。

**-o** _file_
> 输出到指定文件。

**-l** [_file_]
> 使用本地设置 YAML 文件（默认：localSettings.yaml）。

**-s**, **--silent**
> 静默模式；不产生终端输出。

**-c** _dir_
> 将备份文件和 indent.log 放入指定目录而不是当前目录。

**-m**, **--modifylinebreaks**
> 根据设置修改换行。

**-g** _file_
> 指定日志文件的位置。

**--replacement**
> 启用字符串/正则替换模式。

**-y** _yaml_
> 以内联方式提供 YAML 设置（例如 -y="defaultIndent: '  '"）。

# DESCRIPTION

**latexindent** 以一致的缩进格式化 LaTeX 源代码。它能够智能地处理环境、命令和特殊结构。

该工具通过 YAML 文件进行配置，允许自定义缩进大小、环境以及各种特殊情况的处理规则。

# LOCAL SETTINGS

```yaml
# localSettings.yaml
defaultIndent: "  "
removeTrailingWhitespace: 1
noAdditionalIndent:
  document: 1
```

# CAVEATS

基于 Perl；需要 Perl 和 YAML::Tiny。在某些极端情况下可能会改变语义。默认会创建备份文件。复杂的文档可能需要自定义规则。

# HISTORY

latexindent 由 **Chris Hughes** 编写，是一个用于格式化 LaTeX 代码的 Perl 脚本。它随 TeX Live 一同发布，常用来保持 LaTeX 代码风格的一致。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

```brew: brew install latexindent```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[latex](/man/latex)(1), [latexmk](/man/latexmk)(1), [prettier](/man/prettier)(1)
