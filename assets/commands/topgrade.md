# TAGLINE

用一条命令升级系统上的一切

# TLDR

**升级一切**

```topgrade```

**只运行特定步骤**

```topgrade --only [system] --only [brew]```

**跳过特定步骤**

```topgrade --disable [flatpak] --disable [snap]```

**试运行**（显示将要执行的命令）

```topgrade --dry-run```

**对所有提示回答 yes**

```topgrade -y```

**列出可用步骤**

```topgrade --show-skipped```

**只检查更新**，不安装

```topgrade --check```

**编辑配置文件**

```topgrade --edit-config```

# SYNOPSIS

**topgrade** [_options_]

# PARAMETERS

**-y**, **--yes**
> 对所有确认提示回答 yes。

**-n**, **--dry-run**
> 打印将要运行的命令但不执行。

**--only** _STEP_
> 只运行指定的步骤。可多次传入。

**--disable** _STEP_
> 本次运行跳过指定步骤。可多次传入。

**--check**
> 只检查可用更新而不安装。

**-c**, **--cleanup**
> 升级后清理旧的软件包版本和缓存。

**--show-skipped**
> 列出当前配置下会被跳过的步骤。

**-e**, **--edit-config**
> 在 `$EDITOR` 中打开 topgrade 配置文件。

**--config** _FILE_
> 使用其他配置文件。

**--no-retry**
> 失败步骤不提示重试。

**-t**, **--tmux**
> 在新的 tmux 会话中运行 topgrade。

**-k**, **--keep**
> 执行完成后保持终端打开。

**-v**, **--verbose**
> 输出详细信息。

**--remote-host-limit** _REGEX_
> 将远程执行限制为匹配该正则表达式的主机（使用远程主机功能时）。

**-V**, **--version**
> 打印版本信息。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**topgrade** 会检测系统上安装了哪些软件包管理器、语言工具链和应用程序，并依次为每项运行相应的更新命令。缺失的工具会被静默跳过，因此同一份二进制文件和配置可以在软件组合不同的机器上复用。

支持的来源包括操作系统软件包管理器（apt、pacman、dnf、zypper、brew）、语言生态（rustup、pip、pipx、npm、gem、cargo、go）、容器工具（docker、flatpak、snap、nix）、编辑器插件（vim、neovim、emacs）、Shell 插件管理器（fisher、zinit、oh-my-zsh）、固件（fwupd）等等。

行为由位于 `$XDG_CONFIG_HOME/topgrade.toml`（或 `~/.config/topgrade.toml`）的 TOML 配置文件驱动。可以在其中默认禁用某些步骤，还可以定义自定义的前置/后置命令和远程主机。**--only** 和 **--disable** 选项会覆盖当前这次运行的配置。

# CAVEATS

完整升级可能耗时较长，且可能需要输入 `sudo` 密码。瞬时的网络或镜像问题可能导致个别步骤失败；topgrade 会继续执行并在最后报告摘要。混用多个软件来源可能导致版本冲突，某些更新可能会重启服务。

# HISTORY

**topgrade** 由 **Roey Darwish Dror**（**r-darwish**）于 **2018 年**创建，是一个 Rust 工具，目的是免去记住每个软件包管理器更新命令的麻烦。原作者退出后，项目被分叉，现由 GitHub 上社区运营的 **topgrade-rs** 组织维护。

# INSTALL

```apk: sudo apk add topgrade```

```zypper: sudo zypper install topgrade```

```brew: brew install topgrade```

```nix: nix profile install nixpkgs#topgrade```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt](/man/apt)(1), [brew](/man/brew)(1), [pacman](/man/pacman)(8), [flatpak](/man/flatpak)(1), [snap](/man/snap)(1)
