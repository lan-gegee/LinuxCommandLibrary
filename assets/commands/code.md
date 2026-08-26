# TAGLINE

Visual Studio Code 编辑器启动器

# TLDR

在当前目录**打开 VS Code**

```code .```

在 VS Code 中**打开特定文件**

```code [path/to/file]```

**在特定行列位置打开文件**

```code -g [file.txt]:[line]:[column]```

**打开新窗口**

```code -n```

**在现有窗口中打开文件**

```code -r [path/to/file]```

**以 diff 模式比较两个文件**

```code -d [file1] [file2]```

**安装扩展**

```code --install-extension [publisher.extension]```

**列出已安装的扩展**

```code --list-extensions```

# SYNOPSIS

**code** [_options_] [_paths_...]

# PARAMETERS

**-n**, **--new-window**
> 打开一个新的 VS Code 窗口。

**-r**, **--reuse-window**
> 在最近活动的窗口中打开文件。

**-g**, **--goto**
> 在指定的行和列打开文件（file:line:column）。

**-d**, **--diff**
> 以 diff 模式比较两个文件。

**-w**, **--wait**
> 等待文件关闭后再返回。

**--locale** _LOCALE_
> 设置显示语言（例如 en-US、zh-CN）。

**--install-extension** _EXT_
> 按 ID 安装 VS Code 扩展。

**--uninstall-extension** _EXT_
> 卸载 VS Code 扩展。

**--list-extensions**
> 列出所有已安装的扩展。

**--disable-extensions**
> 为本次会话禁用所有已安装的扩展。

**--user-data-dir** _DIR_
> 指定用户数据目录。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**code** 是 Visual Studio Code（Microsoft 广受欢迎的源代码编辑器）的命令行接口。它可以启动编辑器、打开文件与文件夹、管理扩展，并将 VS Code 集成到命令行工作流中。

CLI 支持在指定位置打开文件，这对于从构建工具或 linter 跳转到错误位置非常有用。diff 模式提供文件之间的可视化比较。**--wait** 标志让 VS Code 可以充当 Git 编辑器，或供其他需要等待文件编辑完成的工具使用。

通过 CLI 管理扩展可以用脚本完成 VS Code 的配置并同步开发环境。结合设置同步功能，可以在多台机器上实现可复现的编辑器配置。

# CAVEATS

必须将 **code** 命令添加到 PATH，可通过 VS Code 命令面板中的 "Install 'code' command in PATH" 选项完成。在某些系统上，Insiders 版本的命令可能是 **code-insiders**。远程开发会话使用 **code-server** 提供基于浏览器的访问。

# HISTORY

Visual Studio Code 由 **Microsoft** 于 **2015 年 4 月**发布，是一款基于 Electron 构建的免费开源编辑器，迅速成长为最流行的开发环境之一。CLI 自早期版本起就是 VS Code 的一部分，为基于终端的工作流提供了支持。

# INSTALL

```pacman: sudo pacman -S code```

```nix: nix profile install nixpkgs#code```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [nano](/man/nano)(1), [subl](/man/subl)(1), [atom](/man/atom)(1)

# RESOURCES

```[Source code](https://github.com/microsoft/vscode)```

```[Documentation](https://code.visualstudio.com/docs/editor/command-line)```

<!-- verified: 2026-06-22 -->
