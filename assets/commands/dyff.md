# TAGLINE

面向配置文件的 YAML/JSON diff 工具

# TLDR

**比较**两个 YAML/JSON 文件

```dyff between [file1.yaml] [file2.yaml]```

**比较** Kubernetes 清单

```dyff between -k [manifest1.yaml] [manifest2.yaml]```

**以指定输出格式显示**差异

```dyff between -o json [file1] [file2]```

**递归比较**目录

```dyff between -r [dir1] [dir2]```

# SYNOPSIS

**dyff** [_command_] [_options_] [_files_]

# PARAMETERS

**between** _FILE1_ _FILE2_
> 比较两个文件

**-k, --kubernetes**
> 比较 Kubernetes 清单（忽略元数据时间戳）

**-r, --recursive**
> 递归比较目录

**-o, --output** _FORMAT_
> 输出格式：human、json、yaml、tap（默认：human）

**--chroot** _PATH_
> 将两个输入都限制在指定路径下

**--ignore-order-changes**
> 忽略列表顺序的变化

**--ignore-value-changes** _PATH_
> 忽略特定路径处的值变化

**--no-table-style**
> 禁用表格输出样式

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**dyff** 是一个专为 YAML 和 JSON 配置文件设计的 diff 工具。与传统的基于行的 diff 工具不同，它能理解 YAML/JSON 文档的结构，并在语义层面展示有意义的差异。

该工具特别适合比较 Kubernetes 清单、配置文件以及键序无关但值重要的结构化数据。它可以忽略某些类型的更改（如元数据时间戳），并提供多种输出格式。

# COMMANDS

**between** _FILE1_ _FILE2_
> 比较两个文件并显示差异

**json** _FILE_
> 解析并校验 JSON 文件

**yaml** _FILE_
> 解析并校验 YAML 文件

**version**
> 显示版本信息

# CAVEATS

复杂的嵌套结构可能产生冗长的输出。大文件比较可能较慢。除非明确启用，顺序敏感的比较可能遗漏重排。某些特殊 YAML 特性可能不被完全支持。

# HISTORY

**dyff** 由 Homeport 团队创建，旨在满足对 Kubernetes 和配置文件进行语义化 diff 的需求。在处理结构化配置数据时，它比传统 diff 工具的输出更有意义。

# INSTALL

```zypper: sudo zypper install dyff```

```brew: brew install dyff```

```nix: nix profile install nixpkgs#dyff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [kubectl](/man/kubectl)(1), [yq](/man/yq)(1), [dyff](/man/dyff)(1)
