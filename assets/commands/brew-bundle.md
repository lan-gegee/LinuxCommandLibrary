# TAGLINE

用 Brewfile 以声明式方式管理 Homebrew 软件包

# TLDR

从 Brewfile **安装所有依赖**

```brew bundle install```

从指定的 Brewfile **安装**

```brew bundle --file=[path/to/Brewfile]```

将已安装的软件包**导出**到 Brewfile

```brew bundle dump```

导出时以注释形式附带**描述**

```brew bundle dump --describe```

**检查所有依赖**是否已安装

```brew bundle check```

**卸载**不在 Brewfile 中的软件包

```brew bundle cleanup```

**预览清理结果**而不实际移除

```brew bundle cleanup --dry-run```

**使用全局 Brewfile**（~/.Brewfile）

```brew bundle --global```

# SYNOPSIS

**brew bundle** [_subcommand_] [_options_]

# DESCRIPTION

**brew bundle** 提供一个声明式接口，通过 Brewfile 管理 Homebrew 软件包。它可以从 Homebrew formula、Cask、Mac App Store、tap 以及其他来源安装、升级并跟踪软件包。

Brewfile 描述了已安装软件包的期望状态，便于复制开发环境或在多台机器间保持一致的配置。

# SUBCOMMANDS

**install**
> 从 Brewfile 安装/升级所有依赖（默认）。

**dump**
> 将已安装的软件包写入 Brewfile。

**cleanup**
> 卸载不在 Brewfile 中的软件包。

**check**
> 校验 Brewfile 是否与已安装的软件包一致。

**list**
> 列出 Brewfile 中的全部依赖。

**exec**
> 在隔离的 Brewfile 环境中运行命令。

# PARAMETERS

**--file** _path_
> 使用指定的 Brewfile 位置。

**--global**
> 使用全局 Brewfile（~/.Brewfile 或 XDG 位置）。

**--describe**
> 导出时添加描述性注释。

**--force**
> 即使存在依赖也强制执行 cleanup/dump。

**--dry-run**
> 只显示将要发生的操作，不做更改。

**--verbose**
> 输出详细信息。

**--no-upgrade**
> 不升级已安装的软件包。

# BREWFILE SYNTAX

```
tap "homebrew/cask"
brew "git"
brew "node", args: ["--HEAD"]
cask "firefox"
mas "Xcode", id: 497799835
vscode "ms-python.python"
```

# CAVEATS

Mac App Store 软件包（mas）需要 mas CLI 并已登录 App Store。cleanup 会移除不在 Brewfile 中的软件包；请先使用 **--dry-run**。部分 cask 可能需要管理员权限。

# SEE ALSO

[brew](/man/brew)(1), [brew-cask](/man/brew-cask)(1)
