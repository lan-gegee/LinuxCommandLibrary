# TAGLINE

通过社区插件扩展 CLI 功能

# TLDR

**安装扩展**

```gh extension install [owner]/[repo]```

**列出已安装的扩展**

```gh extension list```

**升级所有扩展**

```gh extension upgrade --all```

**移除扩展**

```gh extension remove [name]```

**创建新扩展**

```gh extension create [name]```

# SYNOPSIS

**gh extension** _command_ [_options_]

# PARAMETERS

**install** _REPO_
> 从仓库安装扩展。

**list**
> 列出已安装的扩展。

**upgrade**
> 升级已安装的扩展。

**remove** _NAME_
> 卸载扩展。

**create** _NAME_
> 搭建新扩展的脚手架。

**browse**
> 浏览可用扩展。

**--all**
> 应用于所有扩展（用于升级）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh extension** 用于管理 GitHub CLI 扩展。扩展为 gh 添加新命令，提供内建命令之外的功能，例如无障碍测试、代码审查工具或自定义工作流。

扩展是遵循 gh 扩展协议、内含可执行文件的 GitHub 仓库。它们可以用任何语言编写并通过 GitHub 分发。扩展系统让社区能够为 gh 添砖加瓦。

gh extension 提供从安装到更新、移除的完整生命周期管理。

# CONFIGURATION

**~/.local/share/gh/extensions/**
> 已安装扩展的存放与执行目录。

# CAVEATS

扩展以用户权限运行。安装前请审查扩展代码。GitHub 不对扩展提供官方支持。

# HISTORY

扩展系统于 **2021 年**加入 **GitHub CLI**，通过插件架构实现社区驱动的 gh 功能拓展。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-a11y](/man/gh-a11y)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_extension)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
