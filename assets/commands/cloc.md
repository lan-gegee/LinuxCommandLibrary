# TAGLINE

源代码行数统计工具

# TLDR

**统计目录中的行数**

```cloc [directory]```

**统计文件中的行数**

```cloc [file.cpp]```

**统计并生成按文件划分的报告**

```cloc --by-file [directory]```

**统计归档文件**

```cloc [archive.tar.gz]```

**比较两个版本**

```cloc --diff [old/] [new/]```

**以 CSV 输出**

```cloc --csv [directory]```

**以 JSON 输出**

```cloc --json [directory]```

**排除目录**

```cloc --exclude-dir=[test,vendor] [directory]```

**列出支持的语言**

```cloc --show-lang```

# SYNOPSIS

**cloc** [_options_] _file|directory|archive_...

# DESCRIPTION

**cloc**（Count Lines of Code）可统计超过 200 种编程语言的空行、注释行和源代码物理行。它能分析单个文件、整个目录树和压缩归档，生成按语言或按文件细分汇总的报告。

该工具包含 diff 模式，可以比较两个代码库并报告新增、删除、修改和未更改的行数。输出可以生成为纯文本、CSV、JSON、SQL 或 XML 格式，便于与其他工具和报告系统集成。

cloc 用 Perl 编写且不依赖外部模块，安装简单，可在任何有 Perl 解释器的平台上运行。它能正确处理多语言文件，并使用特定于语言的注释检测规则进行准确统计。它还可以直接操作 git 仓库，比较分支或提交。

# PARAMETERS

**--by-file**
> 按源文件报告结果

**--by-file-by-lang**
> 按文件和语言报告

**--diff**
> 比较两个代码库

**--csv**
> 以 CSV 格式输出

**--json**
> 以 JSON 格式输出

**--sql**=_file_
> 以 SQL insert 语句输出

**--exclude-dir**=_list_
> 要排除的目录（逗号分隔）

**--exclude-lang**=_list_
> 要排除的语言（逗号分隔）

**--include-lang**=_list_
> 只统计指定语言

**--include-ext**=_list_
> 只统计具有给定扩展名（逗号分隔）的文件。

**--max-file-size**=_MB_
> 跳过大于 _MB_ 兆字节的文件（默认：100）。

**--show-lang**
> 列出可识别的语言后退出。

**--git**
> 强制将输入解释为 git 目标（提交哈希、分支名）。

**--vcs**=_VCS_
> 使用 _VCS_ 获取要统计的文件列表（如 git、svn）。

**--xml**
> 以 XML 格式输出。

**--yaml**
> 以 YAML 格式输出。

**--quiet**
> 不显示进度输出。

**--force-lang**=_LANG_
> 用指定的语言计数器处理所有文件。

**--config** _FILE_
> 从 _FILE_ 读取命令行开关，而非使用默认值。

# OUTPUT FIELDS

Language, files, blank lines, comment lines, code lines

# CAVEATS

不分析语义层面的代码复杂度。多语言文件的某些边缘情况可能被误计。需要 Perl 但无外部模块依赖。支持 250 多种编程语言。

# HISTORY

**cloc** 由 **Al Danial** 创建，最初发布在 SourceForge 上，后来迁至 GitHub。它已成为使用最广泛的开源代码统计工具之一。

# INSTALL

```dnf: sudo dnf install cloc```

```pacman: sudo pacman -S cloc```

```apk: sudo apk add cloc```

```brew: brew install cloc```

```nix: nix profile install nixpkgs#cloc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wc](/man/wc)(1), [sloccount](/man/sloccount)(1), [tokei](/man/tokei)(1)
