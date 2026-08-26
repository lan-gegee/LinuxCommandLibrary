# TAGLINE

环境快照与差异比较工具

# TLDR

**捕获**当前环境状态

```envdiff capture```

将当前环境与快照进行**比较**

```envdiff diff [snapshot.json]```

**列出**所有已捕获的快照

```envdiff list```

**比较**两个快照

```envdiff diff [snapshot1.json] [snapshot2.json]```

# SYNOPSIS

**envdiff** [_command_] [_options_] [_snapshots_]

# PARAMETERS

**capture** [_NAME_]
> 捕获当前环境状态

**diff** [_SNAPSHOT1_] [_SNAPSHOT2_]
> 比较环境（只指定一个时默认与当前环境比较）

**list**
> 列出所有已保存的快照

**delete** _NAME_
> 删除一个快照

**--format** _FORMAT_
> 输出格式：text、json、yaml（默认：text）

**--include** _VARS_
> 要包含的变量列表，逗号分隔

**--exclude** _VARS_
> 要排除的变量列表，逗号分隔

**--sensitive**
> 包含敏感变量（默认会被掩码处理）

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**envdiff** 是一个用于捕获和比较环境变量状态的工具。它允许用户对环境做快照、比较不同状态，并跟踪随时间发生的变化。

该工具适用于调试与环境相关的问题、验证不同系统间配置的一致性，以及记录环境的搭建方式。

# CAVEATS

敏感数据默认会被掩码，但仍可能被捕获。庞大的环境变量集合会生成很大的快照文件。系统专属变量在不同平台上可能不一致。

# HISTORY

**envdiff** 的诞生是为了帮助开发者排查与环境相关的问题，提供一种随时间跟踪和比较环境状态的手段。

# INSTALL

```aur: yay -S envdiff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[env](/man/env)(1), [printenv](/man/printenv)(1), [export](/man/export)(1)
