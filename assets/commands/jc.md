# TAGLINE

将命令输出转换为 JSON 格式

# TLDR

**解析命令输出**

```[command] | jc --[parser]```

**解析 ps 输出**

```ps aux | jc --ps```

**解析 ls 输出**

```ls -l | jc --ls```

**解析 ifconfig**

```ifconfig | jc --ifconfig```

**以美化格式解析**

```df | jc --df -p```

**列出可用解析器**

```jc -a```

**解析文件内容**

```jc --[parser] < [file.txt]```

# SYNOPSIS

**jc** [_options_] --_parser_ [_file_]

# PARAMETERS

**--_PARSER_**
> 解析器名称（ps、ls、df、ifconfig 等）。

**-a**, **--about**
> 列出可用解析器。

**-p**, **--pretty**
> 美化 JSON 输出。

**-r**, **--raw**
> 原始解析器输出。

**-q**, **--quiet**
> 不显示警告。

**-m**, **--monochrome**
> 禁用彩色输出。

**-M**, **--meta-out**
> 在输出中包含元数据（时间戳、解析器名称、退出码）。

**-C**, **--force-color**
> 即使在管道中也强制彩色输出。

**-d**, **--debug**
> 启用调试模式（用 -dd 可获得更详细输出）。

**-y**, **--yaml-out**
> 以 YAML 格式而非 JSON 输出。

**-s**, **--slurp**
> 将多行合并为一个 JSON 数组。

**-u**, **--unbuffer**
> 禁用输出缓冲以便流式传输。

**-v**, **--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jc** 将数十种标准 Unix 命令的输出转换为结构化的 JSON 或 YAML 格式，从而可以通过管道传给 jq 等支持 JSON 的工具，实现自动化处理和脚本编写。

# CAVEATS

各解析器的准确性不一。并非支持所有命令版本。命令输出格式变化时可能需要更新解析器。

# HISTORY

jc 由 **Kelly Brazil** 创建，目的是基于传统 Unix 命令的输出实现 JSON 化的自动化。

# INSTALL

```dnf: sudo dnf install jc```

```pacman: sudo pacman -S jc```

```apk: sudo apk add jc```

```zypper: sudo zypper install jc```

```brew: brew install jc```

```nix: nix profile install nixpkgs#jc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [jo](/man/jo)(1), [gron](/man/gron)(1), [mlr](/man/mlr)(1)
