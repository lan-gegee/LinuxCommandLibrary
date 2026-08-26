# TAGLINE

用 Rust 编写的快速 Node.js 版本管理器

# TLDR

**安装特定 Node.js 版本**

```fnm install [18.17.0]```

**安装最新的 LTS 版本**

```fnm install --lts```

**将当前 Shell 切换到某个版本**

```fnm use [18]```

**设置默认全局版本**

```fnm default [18]```

**列出已安装的版本**

```fnm list```

**列出可下载的版本**

```fnm list-remote```

**启用 cd 时自动切换并执行 shell 初始化**

```eval "$(fnm env --use-on-cd)"```

# SYNOPSIS

**fnm** _command_ [_options_] [_arguments_]

# PARAMETERS

**install** [_VERSION_] [**--lts**]
> 下载并安装 Node.js 版本。接受完整版本号（18.17.0）、主版本号（18）、`latest`，或 `--lts` 表示最新 LTS。

**use** _VERSION_ [**--install-if-missing**]
> 将当前 Shell 切换到 _VERSION_。使用 `--install-if-missing` 时，若该版本不存在则先安装。

**default** _VERSION_
> 设置新 Shell 中使用的默认全局 Node.js 版本。

**current**
> 打印当前激活的 Node.js 版本。

**list**, **ls**
> 列出所有本地已安装的版本。

**list-remote**, **ls-remote**
> 列出分发镜像上所有可用的版本。

**uninstall** _VERSION_
> 移除已安装的 Node.js 版本。

**alias** _VERSION_ _NAME_
> 为某个版本创建命名别名。

**unalias** _NAME_
> 移除命名别名。

**exec** **--using=**_VERSION_ _CMD_
> 以特定 Node.js 版本运行 _CMD_，不切换当前 Shell。

**env** [**--shell**=_SHELL_] [**--use-on-cd**]
> 打印待 eval 的 Shell 配置；在当前 Shell 中启用 fnm，并可在目录切换时自动切换版本。

**completions** **--shell**=_SHELL_
> 输出 bash、zsh、fish 或 PowerShell 的补全脚本。

**--node-dist-mirror** _URL_
> 使用替代的 Node.js 分发镜像。

**--fnm-dir** _PATH_
> 覆盖 fnm 的安装目录（默认 `~/.fnm`）。

**--log-level** _LEVEL_
> 控制日志详细程度（quiet、error、info）。

**--version**, **-V**
> 显示版本信息。

**--help**, **-h**
> 显示帮助信息。

# DESCRIPTION

**fnm**（Fast Node Manager）是一个用 Rust 编写的 Node.js 版本管理器。它以极小的开销提供快速的 Node.js 版本安装与切换。

该工具读取 .node-version 或 .nvmrc 文件实现自动版本切换。Shell 集成支持按目录选择版本，无需手动执行命令。

fnm 凭借 Rust 实现强调速度，并支持包括 Windows 在内的跨平台环境。

# CONFIGURATION

**.node-version**
> 指定当前目录使用的 Node.js 版本。

**.nvmrc**
> 与 nvm 兼容的替代版本文件格式。

# CAVEATS

要使用 `fnm use`、`cd` 时自动切换版本以及保持 PATH 同步，必须通过 `eval "$(fnm env --use-on-cd)"` 进行 Shell 集成。fnm 并非 **nvm** 的完全替代品：它不会加载 bash profile，也不提供 nvm 的全部子命令。已安装的 Node 版本存储在 `$FNM_DIR` 下（默认 `~/.fnm`）；激活版本通过符号链接进入每个 Shell 专属目录，因此不同 Shell 可以有不同的激活版本。

# HISTORY

fnm 作为 **nvm**（最早的 Node Version Manager）的快速替代方案而诞生。基于 Rust 实现，其安装与切换速度相比基于 Shell 的方案大幅提升。

# INSTALL

```pacman: sudo pacman -S fnm```

```zypper: sudo zypper install fnm```

```brew: brew install fnm```

```nix: nix profile install nixpkgs#fnm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvm](/man/nvm)(1), [node](/man/node)(1), [volta](/man/volta)(1)
