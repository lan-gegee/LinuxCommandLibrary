# TAGLINE

Shell 历史年度回顾摘要生成器

# TLDR

**生成你的命令行年度总结**（当前统计数据）

```cmd-wrapped```

**显示特定年份的统计信息**

```cmd-wrapped [2024]```

**分析特定 Shell 的历史记录**

```cmd-wrapped -s [zsh|bash|fish|nu|atuin]```

# SYNOPSIS

**cmd-wrapped** [**-s** _shell_] [_year_]

# PARAMETERS

**-s** _shell_
> 指定要分析哪个 Shell 的历史记录：zsh、bash、fish、nu（nushell）或 atuin。

_year_
> 用于选择特定年份（如 2024）的位置参数。省略时显示当前统计数据。

# DESCRIPTION

**cmd-wrapped** 是一款命令行工具，可为你的终端命令历史生成类似 "Spotify Wrapped" 风格的总结。它分析你的 Shell 历史，产出关于最常用命令、最繁忙时段以及随时间变化的命令模式的统计数据。

该工具读取检测到（或指定）的 Shell 的历史记录，并以彩色格式化输出展示排名靠前的命令、执行的命令总数、使用过的唯一命令数以及时间维度的使用模式。

cmd-wrapped 支持 Zsh、Bash、Fish、Nushell 和 Atuin。传入年份作为位置参数可将报告限定于该年份，或使用 `-s` 选择要分析哪个 Shell 的历史记录。

# CAVEATS

准确性取决于你的 Shell 历史配置。如果历史记录大小受限、忽略了重复项，或某些命令被排除在历史之外，命令数可能被低估。Fish shell 使用不同的历史格式，需要专门的解析方式。

# HISTORY

cmd-wrapged 是一个受 **Spotify Wrapped**（广受欢迎的年度音乐收听总结）启发的趣味年终工具。它诞生于开发者社区对个人数据分析的兴趣以及各平台 "wrapped" 总结的流行趋势。

# INSTALL

```nix: nix profile install nixpkgs#cmd-wrapped```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[history](/man/history)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1)

# RESOURCES

```[Source code](https://github.com/YiNNx/cmd-wrapped)```

<!-- verified: 2026-06-22 -->
