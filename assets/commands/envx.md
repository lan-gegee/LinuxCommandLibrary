# TAGLINE

环境变量管理工具

# TLDR

从 .env 文件**加载**环境

```envx load [.env]```

将当前环境**导出**到文件

```envx export [filename.env]```

在指定环境下**运行**命令

```envx run -e [KEY=VALUE] -- [command]```

**检查**必需的变量

```envx check [REQUIRED_VAR1] [REQUIRED_VAR2]```

# SYNOPSIS

**envx** [_command_] [_options_] [_arguments_]

# PARAMETERS

**load** [_FILE_]
> 从文件加载环境变量

**export** [_FILE_]
> 将当前环境导出到文件

**run** [_options_] -- _COMMAND_
> 在修改后的环境下运行命令

**check** _VARIABLES_
> 验证必需的变量已设置

**-e, --env** _KEY=VALUE_
> 设置环境变量

**-f, --file** _FILE_
> 指定环境文件

**--expand**
> 展开值中的变量引用

**--override**
> 覆盖已有变量

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**envx** 是一个环境变量管理工具，提供加载、导出和操作环境配置的实用功能。它支持 .env 文件、变量展开以及临时性的环境修改。

该工具适合在不同环境（开发、预发布、生产）之间管理环境配置，并在运行应用前确保所需的变量都已就绪。

# CAVEATS

对不可信输入做变量展开可能带来安全风险。.env 文件格式在不同工具之间可能有所差异。某些情况下系统环境变量受保护而无法修改。

# HISTORY

**envx** 的目标是提供一种跨项目、跨环境一致的环境变量管理方式。

# INSTALL

```aur: yay -S envx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[env](/man/env)(1), [direnv](/man/direnv)(1)
