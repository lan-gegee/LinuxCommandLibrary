# TAGLINE

Unix Shell 与命令语言解释器

# TLDR

**运行**脚本

```bash [script.sh]```

**执行**命令

```bash -c ["echo hello"]```

**交互式**登录 Shell

```bash -l```

从标准输入**读取**

```echo "ls -la" | bash```

**调试**脚本

```bash -x [script.sh]```

仅检查**语法**

```bash -n [script.sh]```

# SYNOPSIS

**bash** [_options_] [_file_] [_arguments_]

# DESCRIPTION

**bash**（Bourne Again SHell）是 Unix Shell 和命令语言解释器。它是大多数 Linux 发行版和 macOS 的默认 Shell，提供命令执行、脚本编写、作业控制以及丰富的编程特性。

Bash 向后兼容最初的 Bourne shell (sh)，同时增加了大量改进和现代功能。

# PARAMETERS

**-c** _string_
> 从字符串执行命令

**-l**, **--login**
> 登录 Shell（读取 profile 文件）

**-i**
> 交互模式

**-x**
> 执行前打印命令（调试模式）

**-n**
> 仅检查语法（不执行）

**-e**
> 首个错误即退出

**-u**
> 未定义变量时报错

**-v**
> 详细输出模式（打印输入行）

**--noprofile**
> 不读取 profile 文件

**--norc**
> 不读取 ~/.bashrc

**--posix**
> 按 POSIX 标准行为运作

**-r**, **--restricted**
> 启动受限 Shell

**--version**
> 显示 bash 版本

# FEATURES

- 命令历史（readline）
- Tab 补全
- 作业控制（fg、bg、jobs）
- 算术求值
- 数组与关联数组
- 函数
- 模式匹配与通配符展开
- 进程替换
- Here 文档
- 条件执行
- 循环与流程控制

# STARTUP FILES

**Login shell**
> /etc/profile, ~/.bash_profile, ~/.bash_login, ~/.profile

**Interactive non-login**
> ~/.bashrc

**Non-interactive**
> $BASH_ENV

# SPECIAL VARIABLES

**$0** - 脚本名称
**$1, $2, ...** - 位置参数
**$@** - 所有参数
**$#** - 参数个数
**$?** - 上一个命令的退出状态
**$$** - 进程 ID
**$!** - 最后一个后台作业的 PID

# CONFIGURATION

**~/.bashrc**
> 面向交互式非登录 Shell 的每用户配置。别名、函数、提示符定制。

**~/.bash_profile**
> 面向登录 Shell 的每用户配置。通常会 source ~/.bashrc。

**~/.bash_logout**
> 登录 Shell 退出时执行。

**/etc/bash.bashrc**
> 面向交互式 Shell 的系统级配置。

**/etc/profile**
> 面向登录 Shell 的系统级配置。

# CAVEATS

Bash 特有功能无法移植到 POSIX sh。脚本应使用 `#!/bin/bash` 而不是 `#!/bin/sh`。未加引号的变量可能导致分词问题。建议用 `shellcheck` 校验脚本。

# HISTORY

**Bash** 由 Brian Fox 为 GNU 项目于 **1989** 年创建，作为 Bourne shell 的自由替代品，首个发布版本为 0.99。5.0 版于 **2019** 年发布。

# INSTALL

```apt: sudo apt install bash```

```dnf: sudo dnf install bash```

```pacman: sudo pacman -S bash```

```apk: sudo apk add bash```

```zypper: sudo zypper install bash```

```brew: brew install bash```

```nix: nix profile install nixpkgs#bash```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[sh](/man/sh)(1), [zsh](/man/zsh)(1), [shellcheck](/man/shellcheck)(1)
