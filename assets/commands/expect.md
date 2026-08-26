# TAGLINE

以脚本化应答自动操作交互式应用程序

# TLDR

从文件**执行** expect 脚本

```expect [path/to/file]```

执行**指定的** expect 脚本

```expect -c "[commands]"```

进入**交互式** REPL

```expect -i```

# SYNOPSIS

**expect** [_options_] [_script_] [_arguments_]

# DESCRIPTION

**expect** 通过脚本化的应答来自动操作交互式应用程序。它会启动进程，并基于模式匹配对其输出作出响应。

该工具使用 Tcl 脚本语言以及 spawn、expect、send 等 expect 特有命令。脚本可以处理多种响应模式、超时和条件逻辑。这使得需要交互输入（如密码、确认或菜单选择）的程序也能被自动化。

常用于自动化 SSH 登录、FTP 会话、数据库初始化脚本以及其他交互式程序。虽然功能强大，但出于安全考虑，现在更推荐使用 SSH 密钥、API 令牌和配置管理工具等现代替代方案。

# PARAMETERS

**-c** _commands_
> 在脚本运行前执行给定的 Tcl/Expect 命令。

**-i**
> 交互模式（REPL）。当 stdin 是终端时也会隐式启用。

**-f** _FILE_
> 从 FILE 读取命令脚本。

**-b** _FILE_
> 逐行读取脚本（缓冲模式）——对非常长的脚本很有用。

**-d**
> 启用诊断输出（命令跟踪）。

**-D** [_N_]
> 进入交互式调试器（在第一个提示符处或在 N 次 expect 调用后）。

**-v**
> 输出 Expect 版本并退出。

**--** 
> 选项结束；之后的参数将以 `$argv` 的形式传给脚本。

# CAVEATS

使用 Tcl 脚本语言。在脚本中发送密码存在安全隐患。可能的情况下请考虑 SSH 密钥或其他身份验证方式。

# INSTALL

```apt: sudo apt install expect```

```dnf: sudo dnf install expect```

```pacman: sudo pacman -S expect```

```apk: sudo apk add expect```

```zypper: sudo zypper install expect```

```brew: brew install expect```

```nix: nix profile install nixpkgs#expect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[autoexpect](/man/autoexpect)(1), [tcl](/man/tcl)(1), [ssh](/man/ssh)(1)
