# TAGLINE

注重隐私、无 Microsoft 遥测的 VS Code

# TLDR

**在 VSCodium 中打开当前目录**

```codium .```

**打开指定文件**

```codium [file1.js] [file2.js]```

**打开文件并定位到指定行**和列

```codium -g [file.js:25:10]```

**以 diff 视图比较两个文件**

```codium -d [file1.js] [file2.js]```

**安装扩展**

```codium --install-extension [ms-python.python]```

**列出已安装的扩展**

```codium --list-extensions```

**在新窗口中打开**

```codium -n [path/to/project]```

# SYNOPSIS

**codium** [_options_] [_paths_...]

# PARAMETERS

**-n**, **--new-window**
> 打开一个新的 VSCodium 窗口。

**-r**, **--reuse-window**
> 复用最近活动的窗口。

**-g**, **--goto** _file:line[:column]_
> 打开文件并定位到指定行及可选的列位置。

**-d**, **--diff** _file1_ _file2_
> 打开 diff 编辑器比较两个文件。

**-m**, **--merge** _path1_ _path2_ _base_ _result_
> 执行三方合并。

**-w**, **--wait**
> 等待文件关闭后再返回。

**--locale** _locale_
> 设置显示语言。

**--user-data-dir** _dir_
> 指定用户数据目录；可启用相互隔离的实例。

**--extensions-dir** _dir_
> 设置扩展的根路径。

**--disable-extensions**
> 禁用所有已安装的扩展。

**--disable-gpu**
> 禁用 GPU 硬件加速。

**--inspect-extensions** _port_
> 在指定端口调试扩展。

**-s**, **--status**
> 输出进程占用情况与诊断信息。

**--verbose**
> 输出详细日志。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# EXTENSION COMMANDS

**--install-extension** _id_
> 按 ID 从 Open VSX Registry 安装或更新扩展。

**--uninstall-extension** _id_
> 移除已安装的扩展。

**--list-extensions**
> 显示所有已安装的扩展。

**--show-versions**
> 与 --list-extensions 配合使用时显示扩展版本号。

**--update-extensions**
> 更新所有已安装的扩展。

# DESCRIPTION

**codium** 是 VSCodium 的命令行接口。VSCodium 是 Visual Studio Code 的社区驱动、自由许可的二进制发行版，不含 Microsoft 遥测和跟踪功能，在增强隐私的同时提供与 VS Code 相同的功能。

该 CLI 在功能上与 VS Code 的 **code** 命令完全一致。所有文件、文件夹和多根工作区特性都以同样的方式工作。扩展默认从 **Open VSX Registry** 而非 Microsoft 应用市场获取。

设置存储在 Linux 上的 **~/.config/VSCodium/User/settings.json** 中，扩展则存放在 **~/.vscode-oss**。这种与 VS Code 的分离使得两个编辑器可以同时运行而互不冲突。

VSCodium 提供 Windows、macOS 和 Linux 的原生软件包，也有 Flatpak 和 Snap 包。独立 CLI 还单独分发，适用于无头和远程场景。

# CAVEATS

一些专有的 VS Code 扩展（如 Remote Development、Live Share 以及部分 GitHub 集成）无法从 Open VSX Registry 获取。扩展必须从 Open VSX 安装，或手动通过 VSIX 文件安装。某些 Microsoft 特有功能的表现可能不完全一致。

# HISTORY

VSCodium 诞生于 **2018 年**，是对 Visual Studio Code 中 Microsoft 遥测问题担忧的回应。该项目基于开源的 **vscode** 仓库构建 VS Code，但移除了 Microsoft 品牌、遥测和许可限制。它采用 **MIT 许可证**，如今已成为追求完全开源 VS Code 体验的开发者的首选。

# SEE ALSO

[code](/man/code)(1), [neovim](/man/neovim)(1), [vim](/man/vim)(1)
