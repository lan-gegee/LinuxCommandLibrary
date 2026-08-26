# TAGLINE

检测文件系统变化以实现入侵检测

# TLDR

**初始化**数据库

```sudo aide -i```

**检查**数据库是否存在不一致

```sudo aide -C```

根据配置文件**比较**两个数据库

```sudo aide -E```

以非交互方式**更新**数据库

```sudo aide -u```

定义一个**配置文件**以覆盖默认的 aide.conf

```sudo aide -c [path/to/config_file]```

使用**正则表达式**将 AIDE 限制到特定字符串

```sudo aide -l [regex]```

设置**日志级别**

```sudo aide -L [warning] -C```

# SYNOPSIS

**aide** [_parameters_] _command_

# DESCRIPTION

**AIDE**（Advanced Intrusion Detection Environment）是一个用于入侵检测的文件和目录完整性检查器。它构建一个文件属性数据库，包括权限、inode 编号、时间戳、文件大小、链接计数，以及使用 SHA-256 和 SHA-512 等算法计算的校验和。

初始数据库创建后，AIDE 可以将文件系统的当前状态与存储的快照进行比较，以检测未经授权的修改、新增文件或被删除的文件。配置文件中的规则定义了要监视哪些目录，以及每个路径要检查哪些属性。

# PARAMETERS

**-i, --init**
> 初始化数据库；必须先将其移动到合适的位置才能使用 --check

**-C, --check**
> 检查数据库是否存在不一致；需要一个已初始化的数据库（这是默认命令）

**-u, --update**
> 以非交互方式检查并更新数据库；输入数据库和输出数据库必须不同

**-E, --compare**
> 按配置文件中的定义比较两个数据库

**-n, --dry-init**
> 遍历文件系统并报告匹配的条目，但不写数据库

**-D, --config-check**
> 读取配置文件后立即停止以检查错误

**-c, --config file**
> 指定备用配置文件（使用 '-' 表示标准输入）

**-l, --limit regex**
> 将操作限制在匹配正则表达式模式的条目上

**-L, --log-level level**
> 设置日志级别，覆盖配置文件（取代已被移除的 --verbose 选项）

**-B, --before**
> 在读取文件之前设置配置参数

**-A, --after**
> 在读取文件之后设置配置参数

**-v, --version**
> 输出版本信息并退出

# CONFIGURATION

**/etc/aide/aide.conf**
> 主配置文件，定义要监视的文件、数据库位置和检查规则。

# CAVEATS

退出码组合表示：1（有新文件）、2（有文件被删除）、4（有文件被更改）。数据库必须安全存放，最好放在只读介质上。**-r/--report** 和 **-V/--verbose** 选项已在 AIDE 0.17 中移除；请改用 **report_url** 和 **report_level** 配置选项（或 **-L/--log-level**）。

# HISTORY

最初开发时是 Tripwire 等专有文件完整性检查器的开源替代品。自 0.17 版本起，report 和 verbose 命令行标志被配置指令和 **-L/--log-level** 选项取代。

# INSTALL

```apt: sudo apt install aide```

```dnf: sudo dnf install aide```

```aur: yay -S aide```

```zypper: sudo zypper install aide```

```brew: brew install aide```

```nix: nix profile install nixpkgs#aide```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[tripwire](/man/tripwire)(8), [md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1)

# RESOURCES

```[Source code](https://github.com/aide/aide)```

```[Homepage](https://aide.github.io/)```

<!-- verified: 2026-06-11 -->
