# TAGLINE

跨平台 shell 与脚本语言

# TLDR

**启动 PowerShell**

```pwsh```

**执行一条命令**

```pwsh -Command "[Get-Process]"```

**运行脚本文件**

```pwsh -File [script.ps1]```

**不加载配置文件运行**

```pwsh -NoProfile```

**执行后保持会话**

```pwsh -Command "[command]" -NoExit```

**以非交互模式运行**

```pwsh -NonInteractive -Command "[command]"```

**以特定格式输出**

```pwsh -Command "[Get-Process | ConvertTo-Json]"```

**检查版本**

```pwsh -Version```

# SYNOPSIS

**pwsh** [_-Command command_] [_-File script_] [_-NoProfile_] [_-NonInteractive_] [_options_]

# PARAMETERS

**-Command**, **-c** _COMMAND_
> 执行指定的命令字符串。

**-File**, **-f** _FILE_
> 运行脚本文件。

**-NoProfile**, **-nop**
> 不加载 profile 脚本。

**-NoLogo**, **-nol**
> 隐藏启动横幅。

**-NonInteractive**, **-noni**
> 不提示输入。

**-NoExit**, **-noe**
> 运行命令后不退出。

**-InputFormat** _FORMAT_
> 输入格式：Text、XML。

**-OutputFormat** _FORMAT_
> 输出格式：Text、XML。

**-EncodedCommand** _BASE64_
> 运行 base64 编码的命令。

**-ExecutionPolicy** _POLICY_
> 为会话设置执行策略。

**-ConfigurationName** _NAME_
> 使用特定的配置。

**-WorkingDirectory** _PATH_
> 设置初始工作目录。

**-Login**, **-l**
> 作为登录 shell 运行。

**-Version**, **-v**
> 显示版本。

**-Help**, **-?**
> 显示帮助。

# DESCRIPTION

**PowerShell**（pwsh）是微软的跨平台 shell 和脚本语言。它使用面向对象的管道而非文本流，使数据处理更加结构化。

命令（cmdlet）遵循动词-名词命名规则：Get-Process、Set-Location、Remove-Item。通过管道传递的对象保留其属性和方法，无需解析文本即可进行丰富的查询。

PowerShell 与 .NET 集成，可以访问整个 .NET 类库。变量有类型，参数按名称传递，错误处理使用 try/catch/finally 结构。

profile（Linux 上为 ~/.config/powershell/profile.ps1）用于自定义环境。在 profile 中定义的函数、别名和变量会在各会话之间持续有效。

该语言支持高级特性：类、模块、远程管理、作业（后台任务）和工作流。它既是称手的交互式 shell，也是强大的自动化脚本工具。

# CONFIGURATION

**~/.config/powershell/profile.ps1**（Linux/macOS）、**$HOME\Documents\PowerShell\profile.ps1**（Windows）
> 每次会话启动时执行的用户 profile 脚本。定义函数、别名、变量和提示符定制。

**$PROFILE.AllUsersAllHosts**
> 面向所有用户的系统级 profile，通常位于 PowerShell 安装目录中。

**PSModulePath**
> 环境变量，列出 PowerShell 搜索模块的目录。

# CAVEATS

PowerShell 7+（pwsh）与 Windows PowerShell 5.1 不同。并非所有 Windows 模块都能在 Linux 上工作。默认不区分大小写（与 bash 不同）。引号规则与 POSIX shell 不同。依赖 .NET 会带来启动开销。

# HISTORY

**PowerShell** 由微软的 **Jeffrey Snover** 创建，于 **2006 年**面向 Windows 发布。开源跨平台的 PowerShell Core 于 **2016 年**发布，后于 **2020 年**更名为 PowerShell 7。它将现代 shell 能力带入 Windows，并扩展到了 Linux/macOS。

# INSTALL

```brew: brew install powershell```

```nix: nix profile install nixpkgs#powershell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [dotnet](/man/dotnet)(1)
