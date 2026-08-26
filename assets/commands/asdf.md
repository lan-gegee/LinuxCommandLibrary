# TAGLINE

用一个工具管理多种运行时的版本

# TLDR

**安装**插件

```asdf plugin add [nodejs]```

**列出**所有插件

```asdf plugin list```

**安装**某个版本

```asdf install [nodejs] [18.0.0]```

在当前目录设置 **local** 版本（0.16+）

```asdf set [nodejs] [18.0.0]```

在家目录设置 **global** 版本（0.16+）

```asdf set -u [nodejs] [18.0.0]```

列出已**安装**的版本

```asdf list [nodejs]```

# SYNOPSIS

**asdf** _command_ [_plugin_] [_version_]

# DESCRIPTION

**asdf** 是一个通用版本管理器，通过插件支持多种语言和工具。它为 Node.js、Python、Ruby、Go 以及数十种其他工具的版本管理提供单一界面。

版本记录在 .tool-versions 文件中，该文件可以放在家目录（全局默认）或任意项目目录（按项目覆盖）。

注意：0.16 版本用 Go 重写了 asdf，并移除了独立的 **global** 和 **local** 命令，两者统一由 **set** 取代。较早的 0.15.x 及更早版本仍使用 **asdf global** 和 **asdf local**。

# PARAMETERS

**plugin add** _name_
> 安装插件

**plugin list**
> 列出已安装的插件

**install** _plugin_ _version_
> 安装指定版本

**uninstall** _plugin_ _version_
> 移除版本

**set** [_-u_|_--home_] [_-p_|_--parent_] _plugin_ _version_
> 将版本写入 .tool-versions 文件（0.16+）。默认写入当前目录；**-u** 面向家目录（全局），**-p** 面向最近的父目录。取代旧的 **global**/**local** 命令。

**global** _plugin_ _version_
> 设置全局默认版本（0.16 中已移除；请使用 **set -u**）。

**local** _plugin_ _version_
> 设置项目版本（0.16 中已移除；请使用 **set**）。

**list** _plugin_
> 列出已安装的版本

**list all** _plugin_
> 列出所有可用版本

**latest** _plugin_
> 显示可用的最新稳定版本

**current** [_plugin_]
> 显示当前版本

**which** _command_
> 显示将被执行的可执行文件路径

**reshim** [_plugin_] [_version_]
> 重建 shim

# CONFIGURATION

**~/.asdfrc**
> asdf 的用户配置文件，例如旧式版本文件支持等设置。

**.tool-versions**
> 按项目指定工具版本的文件。放在项目根目录下。

**~/.tool-versions**
> 在找不到项目级文件时使用的全局默认工具版本。

# CAVEATS

每种工具都需要对应的插件。需要初始化 shell（~/.bashrc 或 ~/.zshrc）。安装新的可执行文件后可能需要重建 shim。

# HISTORY

**asdf** 由 @HashNuke 于 **2014** 年前后创建，旨在提供一个统一的版本管理器，取代 nvm、rbenv、pyenv 等语言专属工具。它最初是一个 Bash/shim 项目，后在 2025 年初的 **0.16** 版本中用 Go 重写。

# INSTALL

```zypper: sudo zypper install asdf```

```brew: brew install asdf```

```nix: nix profile install nixpkgs#asdf```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[nvm](/man/nvm)(1), [rbenv](/man/rbenv)(1), [pyenv](/man/pyenv)(1), [mise](/man/mise)(1), [direnv](/man/direnv)(1)

# RESOURCES

```[Source code](https://github.com/asdf-vm/asdf)```

```[Homepage](https://asdf-vm.com)```

<!-- verified: 2026-06-17 -->
