# TAGLINE

切换 Bash shell 行为选项

# TLDR

**列出所有 shell 选项**及其状态

```shopt```

**启用某个 shell 选项**

```shopt -s [optname]```

**禁用某个 shell 选项**

```shopt -u [optname]```

**检查某选项是否已启用**（安静模式）

```shopt -q [optname] && echo "enabled"```

**启用扩展 glob 匹配**

```shopt -s extglob```

**启用大小写不敏感的 glob 匹配**

```shopt -s nocaseglob```

**让 glob 模式包含点文件**

```shopt -s dotglob```

**以便于复用的格式打印选项**

```shopt -p```

# SYNOPSIS

**shopt** [_-pqsu_] [_-o_] [_optname ..._]

# PARAMETERS

**-p**
> 以可作为输入复用的格式打印 shell 选项

**-q**
> 安静模式；抑制输出，只返回状态码

**-s**
> 设置（启用）指定选项

**-u**
> 取消设置（禁用）指定选项

**-o**
> 仅限于也可用 set -o 设置的选项

# COMMON OPTIONS

**cdspell**
> 自动纠正 cd 参数中的轻微拼写错误

**dotglob**
> 让 glob 模式包含以 . 开头的文件

**extglob**
> 启用扩展模式匹配运算符

**globstar**
> 启用 ** 递归目录匹配

**histappend**
> 追加到历史文件而不是覆盖

**nocaseglob**
> 文件名 glob 匹配时不区分大小写

**nullglob**
> 未匹配到内容的 glob 模式展开为空而不是保持原样

**expand_aliases**
> 启用别名展开（交互式 Shell 默认开启）

# DESCRIPTION

**shopt** 是一个 Bash 内建命令，用于为当前会话启用或禁用 shell 选项。这些选项会修改 shell 的行为，包括 glob 匹配、历史记录处理、目录导航和命令补全。

不带参数时，shopt 会列出所有选项及其当前状态。使用 **-s** 启用、**-u** 禁用特定选项。**-q** 标志静默测试选项：已启用则退出状态码为 0，已禁用则为 1。

通过 shopt 设置的选项仅在当前会话有效。如需永久配置，可将 shopt 命令添加到 **~/.bashrc**。

# CAVEATS

shopt 是 Bash 特有的，在 zsh、dash、ksh 等其他 shell 中不可用，它们有各自的选项机制。**-o** 标志用于兼容 set 内建命令的选项。

# HISTORY

shopt 是 **Bash 2.0**（1996 年）引入的内建命令，相比 set 内建命令为 shell 选项提供了更清晰的接口。它至今仍是配置 Bash 行为的主要方式。

# SEE ALSO

[set](/man/set)(1), [bash](/man/bash)(1)
