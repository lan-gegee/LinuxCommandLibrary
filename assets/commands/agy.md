# TAGLINE

Google Antigravity IDE 启动器与命令行客户端

# TLDR

在当前目录**启动 Antigravity**

```agy .```

在 Antigravity 中**打开指定的项目文件夹**

```agy [path/to/project]```

**打开指定文件**进行编辑

```agy [path/to/file]```

**在指定行打开文件**

```agy --goto [path/to/file]:[line]```

**启动新窗口**而不复用现有窗口

```agy --new-window [path/to/project]```

**显示已安装版本**

```agy --version```

# SYNOPSIS

**agy** [_options_] [_path_ ...]

# PARAMETERS

**-n**, **--new-window**
> 打开新窗口而不是复用现有窗口。

**-r**, **--reuse-window**
> 复用最近处于活动状态的窗口。

**-g**, **--goto** _file:line[:column]_
> 在指定行（及可选列）打开文件。

**-d**, **--diff** _file1 file2_
> 打开比较两个文件的 diff 编辑器。

**-a**, **--add** _folder_
> 把文件夹加入最近活动的窗口。

**-w**, **--wait**
> 等文件关闭后再返回。

**--user-data-dir** _DIR_
> 为用户数据使用自定义目录。

**--extensions-dir** _DIR_
> 为已安装的扩展使用自定义位置。

**--list-extensions**
> 列出已安装的扩展并退出。

**--install-extension** _EXT_
> 安装或更新给定的扩展。

**--uninstall-extension** _EXT_
> 卸载给定的扩展。

**-v**, **--version**
> 打印版本信息并退出。

**-h**, **--help**
> 打印帮助并退出。

# DESCRIPTION

**agy** 是 **Google Antigravity** 的命令行启动器。Antigravity 是一款构建在 Visual Studio Code 基础上的 AI 优先开发环境。它可以在 Antigravity 编辑器中打开文件、文件夹和工作区，并提供通往其代理式编码功能的入口，包括由 **Gemini** 驱动的代理面板以及用于协调多个 AI 代理的 Manager 界面。

该启动器遵循 VS Code 风格 CLI 的惯例：作为位置参数传入的路径会按文件或文件夹打开，各类标志则控制窗口行为、扩展与用户数据目录。在 macOS 上，通常通过 Antigravity 内部的 “Install 'agy' command in PATH” 操作来安装；在部分 Linux 发行版上，二进制可能以 **antigravity** 之名出现，此时常借助诸如 **/usr/local/bin/agy → /usr/bin/antigravity** 的符号链接，以满足那些按 **agy** 名称检测 Antigravity 的工具的需要。

除了打开图形界面，**agy** 还是 Gemini CLI 以及其他将编辑或会话委托给 Antigravity 的工具的集成点。它本身并不运行无头代理；这项能力由 Antigravity 提供的独立配套二进制承担。

# CAVEATS

在某些 Linux 安装上，二进制名为 **antigravity**；如果其他工具（例如 Gemini CLI）期望的是 **agy** 这个名字，请创建相应的符号链接。该 CLI 处于活跃开发之中，标志行为与 VS Code 高度一致，因此各版本之间可能出现细微差别。

# HISTORY

Antigravity 由 **Google** 于 **2025 年 11 月**发布，是 Visual Studio Code 的一个“代理优先” IDE 分支，**agy** 启动器随面向 Linux、macOS 和 Windows 的桌面应用一并交付。该工具与 Gemini 模型家族联系紧密，也是 Google 在代理式开发者工具上更大规模投入的一环。

# SEE ALSO

[code](/man/code)(1), [gemini](/man/gemini)(1), [claude](/man/claude)(1)
