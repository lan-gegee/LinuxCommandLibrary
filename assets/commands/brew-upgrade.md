# TAGLINE

将已安装的 Homebrew 软件包升级到新版本

# TLDR

**升级所有已安装的 formula 和 cask**

```brew upgrade```

**升级指定的 formula**

```brew upgrade [formula]```

**升级指定的 cask**

```brew upgrade --cask [cask]```

预演显示将被升级的内容而不实际升级

```brew upgrade --dry-run```

同时升级自行管理更新或跟踪最新版本的 cask

```brew upgrade --greedy```

以详细输出升级，显示校验与安装后步骤

```brew upgrade --verbose [formula]```

# SYNOPSIS

**brew upgrade** [_options_] [_formula|cask_] ...

# DESCRIPTION

**brew upgrade** 使用软件包最初安装时的相同选项，升级过时的 cask 以及过时且未被固定的 formula。不带参数时升级所有已安装软件包；带参数时只升级指定的软件包。

除非设置了 **$HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK**，对链接损坏或过时的被依赖项，会分别运行 **brew upgrade** 或 **brew reinstall**。

除非设置了 **$HOMEBREW_NO_INSTALL_CLEANUP**，升级完成后会对其运行 **brew cleanup**，并且每 30 天对所有 formula 清理一次。

# PARAMETERS

**--formula**, **--formulae**
> 将所有命名参数视为 formula。未指定命名参数时，仅升级过时的 formula。

**--cask**, **--casks**
> 将所有命名参数视为 cask。未指定命名参数时，仅升级过时的 cask。

**-n**, **--dry-run**
> 显示将要升级的内容，但不实际升级任何东西。

**-v**, **--verbose**
> 打印校验和安装后的步骤。

**-q**, **--quiet**
> 让部分输出更安静。

**-d**, **--debug**
> 若构建失败，打开交互式调试会话，可访问 IRB 或临时构建目录中的 shell。

**--display-times**
> 运行结束时打印每个软件包的安装耗时。若设置了 **$HOMEBREW_DISPLAY_INSTALL_TIMES** 则默认启用。

**--ask**
> 在下载和升级 formula 前请求确认，并打印 bottle 及其依赖的下载大小、安装大小和净安装大小。若设置了 **$HOMEBREW_ASK** 则默认启用。

**-f**, **--force**
> 安装 formula 时不检查之前安装过的 keg-only 或未迁移版本。安装 cask 时覆盖现有文件（二进制文件和符号链接除外，除非原本来自同一 cask）。

**-g**, **--greedy**
> 同时包含 **auto_updates true** 或 **version :latest** 的 cask。若设置了 **$HOMEBREW_UPGRADE_GREEDY** 则默认启用。

**--greedy-latest**
> 同时包含 **version :latest** 的 cask。

**--greedy-auto-updates**
> 同时包含 **auto_updates true** 的 cask。

**--fetch-HEAD**
> 拉取上游仓库，检测 formula 的 HEAD 安装是否过时。否则只有在新稳定版或开发版发布时才会检查仓库 HEAD 的更新。

**-s**, **--build-from-source**
> 即使存在 bottle 也从源码编译 formula。

**--force-bottle**
> 只要当前或最新的 macOS 版本有对应的 bottle 就从 bottle 安装，即使通常不会使用它安装。

**--skip-cask-deps**
> 跳过安装 cask 依赖。

**--overwrite**
> 链接时删除 prefix 中已存在的文件。

**--keep-tmp**
> 保留安装过程中创建的临时文件。

# ENVIRONMENT

**HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK**
> 跳过升级过时及链接损坏的被依赖项。

**HOMEBREW_NO_INSTALL_CLEANUP**
> 升级后跳过自动清理。

**HOMEBREW_DISPLAY_INSTALL_TIMES**
> 默认启用 **--display-times**。

**HOMEBREW_ASK**
> 默认启用 **--ask**。

**HOMEBREW_UPGRADE_GREEDY**
> 默认启用 **--greedy**。

# CAVEATS

升级前先运行 **brew update** 以获取最新的软件包定义。cask 的升级可能采用卸载/重装或内容替换策略，具体取决于 cask 本身。被固定的 formula 永远不会被升级；使用 **brew unpin** 可解除固定。

# SEE ALSO

[brew](/man/brew)(1), [brew-update](/man/brew-update)(1), [brew-outdated](/man/brew-outdated)(1), [brew-install](/man/brew-install)(1), [brew-reinstall](/man/brew-reinstall)(1), [brew-cleanup](/man/brew-cleanup)(1)
