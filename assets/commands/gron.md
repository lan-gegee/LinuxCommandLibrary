# TAGLINE

让 JSON 变得可 grep

# TLDR

**将 JSON 转换为 gron 格式**

```gron [file.json]```

**将 JSON 通过管道传给 gron**

```curl [api/url] | gron```

**配合 grep 过滤**

```gron [file.json] | grep [pattern]```

**转换回 JSON**

```gron [file.json] | grep [filter] | gron -u```

**彩色输出**

```gron --color [file.json]```

# SYNOPSIS

**gron** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要处理的 JSON 文件。

**-u**, **--ungron**
> 将 gron 格式转换回 JSON。

**-s**, **--stream**
> 流式处理模式。

**--color**
> 彩色输出。

**--no-sort**
> 保留原始顺序。

**-j**, **--json**
> 以 JSON 输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gron** 将 JSON 转换为离散的路径-值赋值形式，使其可以被标准 Unix 工具 grep。每个 JSON 值变成单独一行，显示其从根开始的完整路径。

结果可以用 grep 过滤，再通过 ungron 模式（**-u**）转换回有效的 JSON，从而无需专用工具即可实现强大的 JSON 查询。

# CAVEATS

大型 JSON 文件会产生大量行。路径语法可能有差异。ungron 要求输入是有效的 gron 格式。

# HISTORY

gron 由 **Tom Hudson** 创建，用于解决用传统 Unix 工具搜索复杂 JSON 结构的难题。

# INSTALL

```apt: sudo apt install gron```

```pacman: sudo pacman -S gron```

```apk: sudo apk add gron```

```zypper: sudo zypper install gron```

```brew: brew install gron```

```nix: nix profile install nixpkgs#gron```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [grep](/man/grep)(1), [json_pp](/man/json_pp)(1)

# RESOURCES

```[Source code](https://github.com/tomnomnom/gron)```

<!-- verified: 2026-07-17 -->
