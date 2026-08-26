# TAGLINE

跨平台 PowerShell shell

# TLDR

**启动 PowerShell**

```pwsh```

**执行一条命令**

```pwsh -Command "[Get-Process]"```

**运行脚本文件**

```pwsh -File [script.ps1]```

**不加载 profile 运行**

```pwsh -NoProfile -Command "[command]"```

**以非交互方式运行以实现自动化**

```pwsh -NonInteractive -Command "[command]"```

**运行 base64 编码的命令**

```pwsh -EncodedCommand [base64_string]```

**在指定的工作目录中启动**

```pwsh -WorkingDirectory [/path/to/dir]```

**显示版本**

```pwsh -Version```

# SYNOPSIS

**pwsh** [_options_] [-File _file_ [_args_]] [-Command { - | _script-block_ | _string_ }]

# PARAMETERS

**-Command** | **-c** _CMD_
> 执行命令字符串或脚本块。

**-File** | **-f** _FILE_
> 执行脚本文件。必须是最后一个参数。

**-NonInteractive** | **-noni**
> 禁用交互式提示；适合自动化场景。

**-NoProfile** | **-nop**
> 不加载 PowerShell profile。

**-NoLogo** | **-nol**
> 隐藏交互式会话启动时的横幅。

**-NoExit** | **-noe**
> 运行完启动命令后不退出。

**-Login** | **-l**
> 以登录 shell 方式启动（仅限 Linux/macOS）。必须是第一个参数。

**-EncodedCommand** | **-e** _BASE64_
> 接受 base64 编码的 UTF-16LE 命令字符串。

**-ExecutionPolicy** | **-ep** _POLICY_
> 为会话设置执行策略（仅限 Windows）。

**-WorkingDirectory** | **-wd** _DIR_
> 设置初始工作目录。

**-CommandWithArgs** | **-cwa** _CMD_ [_args_]
> 执行命令，参数填充到 $args 中。

**-ConfigurationFile** _FILE_
> 指定会话配置（.pssc）文件路径。

**-OutputFormat** | **-o** {Text | XML}
> 输出格式。默认为 Text。

**-InputFormat** | **-if** {Text | XML}
> 发送给 PowerShell 的数据格式。

**-SettingsFile** _FILE_
> 在会话中覆盖系统级的 powershell.config.json。

**-Interactive** | **-i**
> 显示交互式提示。-NonInteractive 的反向操作。

**-Version** | **-v**
> 显示版本。

# DESCRIPTION

**pwsh** 是 PowerShell 的可执行文件。PowerShell 是 Microsoft 的跨平台 shell 和脚本语言，可运行于 Linux、macOS 和 Windows。它提供面向对象的管道，命令输出的是结构化的 .NET 对象而非纯文本，无需解析即可进行丰富的数据处理。

PowerShell 包含一整套用于系统管理、文件管理和进程控制的 cmdlet。脚本使用 **.ps1** 扩展名，支持模块、远程操作和错误处理等高级特性。**-Command** 标志执行内联命令，**-File** 运行脚本文件，而 **-NonInteractive** 模式适用于自动化和 CI/CD 管道。

# CONFIGURATION

**~/.config/powershell/profile.ps1**
> 启动时执行的用户 profile 脚本，用于定义别名、函数和环境自定义。

**~/.config/powershell/Microsoft.PowerShell_profile.ps1**
> 仅在默认 PowerShell 主机中加载的主机专用 profile。

**$PROFILE**
> 内置变量，指向当前用户在活动主机下的 profile 路径。

# CAVEATS

在 Linux/macOS 上需要单独安装。与 Windows PowerShell 5.1（powershell.exe）不同。所有参数不区分大小写。

# HISTORY

PowerShell Core 由 **Microsoft** 发布，作为跨平台 shell。

# INSTALL

```apk: sudo apk add powershell```

```brew: brew install powershell```

```nix: nix profile install nixpkgs#powershell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [sh](/man/sh)(1), [fish](/man/fish)(1)
