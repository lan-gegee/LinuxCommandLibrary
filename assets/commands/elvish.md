# TAGLINE

具有现代编程特性的富表现力 Shell

# TLDR

**启动 Elvish Shell**

```elvish```

**运行 Elvish 脚本**

```elvish [script.elv]```

**运行命令字符串**

```elvish -c "[echo hello]"```

**以指定配置启动**

```elvish --rc [config.elv]```

# SYNOPSIS

**elvish** [_options_] [_script_] [_args_]

# PARAMETERS

_SCRIPT_
> 要执行的脚本文件。

**-c** _CODE_
> 执行命令字符串。

**--rc** _FILE_
> 配置文件。

**--norc**
> 不加载 rc 文件。

**-i**
> 即使输入不是终端也强制进入交互模式。

**--compileonly**
> 解析并编译代码但不执行，同时报告错误。

**--json**
> 将 --compileonly 的输出打印为 JSON。

**--version**
> 打印 Elvish 版本并退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Elvish** 是一门富有表现力的编程语言，也是类 Unix 系统上功能强大的 Shell。它将 shell 特性与现代编程语言相结合，包括命名空间、lambda 和结构化数据。

该 shell 提供传递结构化数据（而不只是字符串）的管道、内置文件管理器（Ctrl-N），以及包含目录历史（Ctrl-L）在内的完善历史记录。其语法比传统 shell 更简洁。

Elvish 提供实时语法高亮、智能补全，并为交互使用和脚本编写提供一致的编程模型。

# CONFIGURATION

**~/.config/elvish/rc.elv** 或 **~/.elvish/rc.elv**
> shell 启动时加载的主配置文件。

**~/.config/elvish/lib/**
> 存放 Elvish 模块和库的目录。

# CAVEATS

不兼容 POSIX。脚本无法移植到 bash/zsh。社区比主流 shell 小。某些传统 shell 模式无法使用。

# HISTORY

Elvish 由 **Qi Xiao** 自 **2014 年**前后开始创建，是一款从零设计、以现代语言特性而非 POSIX 兼容性为主要目标的 shell。

# INSTALL

```apt: sudo apt install elvish```

```dnf: sudo dnf install elvish```

```pacman: sudo pacman -S elvish```

```apk: sudo apk add elvish```

```brew: brew install elvish```

```nix: nix profile install nixpkgs#elvish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [nushell](/man/nushell)(1)

# RESOURCES

```[Source code](https://github.com/elves/elvish)```

```[Homepage](https://elv.sh/)```

```[Documentation](https://elv.sh/ref/)```

<!-- verified: 2026-07-14 -->
