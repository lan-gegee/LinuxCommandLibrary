# TAGLINE

kubectl（Kubernetes 命令行工具）的插件管理器

# TLDR

**更新插件索引**

```kubectl krew update```

**搜索插件**

```kubectl krew search [keyword]```

**安装插件**

```kubectl krew install [plugin-name]```

**列出已安装的插件**

```kubectl krew list```

**显示插件信息**

```kubectl krew info [plugin-name]```

**升级所有插件**

```kubectl krew upgrade```

**升级指定插件**

```kubectl krew upgrade [plugin-name]```

**卸载插件**

```kubectl krew uninstall [plugin-name]```

**添加自定义插件索引**

```kubectl krew index add [index-name] [git-url]```

# SYNOPSIS

**kubectl krew** _command_ [_options_]

# COMMANDS

**install** _plugin_
> 安装 kubectl 插件。

**uninstall** _plugin_
> 移除已安装的插件。

**upgrade** [_plugin_]
> 升级已安装的插件。未指定插件时升级全部。

**update**
> 更新插件索引的本地副本。

**search** [_keyword_]
> 搜索可用的插件。

**list**
> 列出已安装的 kubectl 插件。

**info** _plugin_
> 显示插件的详细信息。

**index** _subcommand_
> 管理自定义插件索引。

**version**
> 显示 krew 版本和诊断信息。

**completion** _shell_
> 生成 Shell 补全脚本。

**help**
> 关于任意命令的帮助。

# PARAMETERS

**-v**, **--v** _level_
> 日志详细级别（0-4）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**krew** 是 kubectl（Kubernetes 命令行工具）的插件管理器。它简化了在 macOS、Linux 和 Windows 上发现、安装和管理 kubectl 插件的过程。

Krew 维护着一个可用插件的中央索引。使用 **kubectl krew update** 将本地索引与远程仓库同步。**search** 命令按名称或关键字查找插件，**info** 显示插件的详细描述和用法。

插件安装到 **~/.krew/bin**，该目录必须包含在你的 PATH 中。安装后，插件以 **kubectl plugin-name** 的方式调用（不带 "krew" 前缀）。

Krew 本身也是一个 kubectl 插件，可以通过 **kubectl krew upgrade krew** 自我更新。自定义插件索引可以用 **kubectl krew index add** 添加，以便使用私有或第三方插件仓库。

流行的插件包括 **ctx**（切换上下文）、**ns**（切换命名空间）、**neat**（精简 YAML 输出）和 **tree**（资源层级可视化）。

# CAVEATS

需要 kubectl v1.12 或更高版本。~/.krew/bin 目录必须在安装后手动加入 PATH。插件更新需要显式执行 **upgrade** 命令，不会自动更新。某些插件可能有额外的依赖。

# HISTORY

Krew 由 **Kubernetes SIG CLI** 团队创建，目的是满足标准化的 kubectl 插件分发机制的需求。它的灵感来自 Homebrew 和 apt 等软件包管理器。该项目已发展到托管数百个社区贡献的插件，成为 kubectl 插件管理的事实标准。

# INSTALL

```pacman: sudo pacman -S krew```

```brew: brew install krew```

```nix: nix profile install nixpkgs#krew```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k9s](/man/k9s)(1), [helm](/man/helm)(1)
