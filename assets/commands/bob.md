# TAGLINE

管理并切换 Neovim 版本

# TLDR

**安装 Neovim 版本**

```bob install [stable]```

**安装 nightly 构建版本**

```bob install nightly```

**切换到某个版本**

```bob use [stable]```

**列出已安装的版本**

```bob list```

**列出可用的远程版本**

```bob list-remote```

**卸载某个版本**

```bob uninstall [nightly]```

不切换的情况下**运行指定版本**

```bob run [stable] [file.txt]```

从配置文件**同步版本**

```bob sync```

**清除所有 bob 数据**及已安装的版本

```bob erase```

# SYNOPSIS

**bob** _command_ [_version_] [_arguments_]

# DESCRIPTION

**bob** 是一个跨平台的 Neovim 版本管理器，可以从命令行轻松切换不同的 Neovim 版本。它可以安装稳定版、nightly 构建版、特定版本，甚至可以从 commit 哈希构建。

该工具管理多个 Neovim 安装，自动下载并为你的平台设置相应的二进制文件。

# SUBCOMMANDS

**install**
> 安装指定的 Neovim 版本。

**use**
> 切换到某个版本（必要时自动安装）。

**run**
> 使用参数运行指定版本。

**uninstall**
> 移除已安装的版本。

**list**
> 显示已安装和当前激活的版本。

**list-remote**
> 显示可供下载的版本。

**sync**
> 安装配置文件中固定的版本。

**update**
> 更新已安装的版本（使用 **--all** 更新所有版本）。

**rollback**
> 回滚到先前安装的 nightly 构建版本。

**erase**
> 移除所有 bob 数据和安装。

**complete**
> 生成 Shell 补全脚本。

# VERSION SPECIFIERS

**stable**
> 最新稳定版。

**nightly**
> 最新 nightly 构建。

**latest**
> 最新版本。

**v0.9.0**
> 特定的版本字符串。

**commit-hash**
> 从特定 commit 构建。

# PARAMETERS

配置从平台配置目录下的 JSON 或 TOML 文件读取（Linux 上为 **~/.config/bob/config.json** 或 **config.toml**）。环境变量 **$BOB_CONFIG** 可覆盖此位置。

# CAVEATS

下载版本需要联网。GitHub API 可能受速率限制；可设置 **GITHUB_TOKEN** 环境变量以提高限额。erase 命令会永久移除所有 bob 数据，包括已下载的版本。

# HISTORY

Bob 由 **Mordechai Hadad** 创建，是一个用于管理多个 Neovim 安装的现代跨平台方案，类似于 nvm 管理 Node.js 版本或 pyenv 管理 Python 版本的方式。

# INSTALL

```pacman: sudo pacman -S bob```

```brew: brew install bob```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvim](/man/nvim)(1), [nvm](/man/nvm)(1), [rustup](/man/rustup)(1)

# RESOURCES

```[Source code](https://github.com/MordechaiHadad/bob)```

<!-- verified: 2026-06-19 -->
