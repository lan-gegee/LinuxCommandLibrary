# TAGLINE

通过 Homebrew 安装和管理 macOS 图形界面应用

# TLDR

**安装应用**

```brew install --cask [firefox]```

**列出**已安装的 cask

```brew list --cask```

**搜索** cask

```brew search --cask [application-name]```

获取某个 cask 的**信息**

```brew info --cask [firefox]```

**升级** cask

```brew upgrade --cask [firefox]```

**升级全部 cask**，包括会自行更新的应用

```brew upgrade --cask --greedy```

**卸载** cask

```brew uninstall --cask [firefox]```

**卸载并删除**所有关联文件

```brew uninstall --cask --zap [firefox]```

**安装到自定义目录**

```brew install --cask --appdir=[~/Applications] [firefox]```

# SYNOPSIS

**brew** [_--cask_] _command_ [_cask-name_] [_options_]

# DESCRIPTION

**brew --cask**（前身为 Homebrew Cask）管理以二进制包（.dmg、.pkg、.app）分发的 macOS 应用程序的安装。它自动完成下载、安装到 /Applications 以及移除图形界面应用的流程。

Cask 将 Homebrew 的命令行工作流程扩展到了浏览器、编辑器和实用工具等桌面应用，这些应用通常需要手动拖拽安装。

# COMMANDS

**install --cask**
> 安装 cask 应用。

**uninstall --cask**
> 移除 cask 应用。

**upgrade --cask**
> 升级已安装的 cask。

**list --cask**
> 列出已安装的 cask。

**info --cask**
> 显示某个 cask 的信息。

**search --cask**
> 搜索可用的 cask。

**outdated --cask**
> 列出有可用更新的 cask。

# PARAMETERS

**--appdir** _path_
> 将应用安装到指定目录（默认：/Applications）。

**--fontdir** _path_
> 将字体安装到指定目录。

**--greedy**
> 在升级时包含会自行更新的应用。

**--zap**
> 删除与该 cask 关联的所有文件（包括偏好设置）。

**--force**
> 即使已安装也强制安装。

**--no-quarantine**
> 禁用 macOS 隔离属性。

# CAVEATS

许多应用会自行更新，默认情况下被 **brew upgrade** 排除在外；使用 **--greedy** 可将它们包含进来。**--zap** 选项可能删除与其他应用共享的文件。部分 cask 安装时需要管理员权限。

# HISTORY

Homebrew Cask 由 **phinze** 于 **2012** 年作为独立项目创建，用于将 Homebrew 扩展到 macOS 图形界面应用。它在 **2020** 年被并入 Homebrew 核心，命令形式也从 **brew cask install** 改为 **brew install --cask**。

# SEE ALSO

[brew](/man/brew)(1), [brew-bundle](/man/brew-bundle)(1)
