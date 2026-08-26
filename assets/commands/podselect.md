# TAGLINE

从 Perl POD 文件中提取指定章节

# TLDR

**从 POD 中提取特定章节**

```podselect -section [NAME] [file.pod]```

**提取多个章节**

```podselect -section [NAME] -section [SYNOPSIS] [file.pod]```

**处理多个文件**

```podselect -section [NAME] [*.pod]```

# SYNOPSIS

**podselect** [_options_] [_files_]

# PARAMETERS

_FILES_
> 输入的 POD 文件。

**-section** _NAME_
> 要提取的章节。

# DESCRIPTION

**podselect** 从 Perl POD（Plain Old Documentation）文件中提取特定的命名章节。它会过滤 POD 内容，只输出与 **-section** 参数匹配的章节。

可以指定多个 **-section** 标志以一次提取多个章节。这适用于从较大的 POD 文档中提取 NAME、SYNOPSIS 或 DESCRIPTION 等单个章节。是标准 Perl 发行版的一部分。

# CAVEATS

Perl 特有格式。标准的 Perl 工具。

# HISTORY

podselect 是为了**选择性提取 POD** 章节而创建的。

# INSTALL

```pacman: sudo pacman -S perl-pod-parser```

```apk: sudo apk add perl-pod-parser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pod2text](/man/pod2text)(1), [podchecker](/man/podchecker)(1), [perldoc](/man/perldoc)(1)
