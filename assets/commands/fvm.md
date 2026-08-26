# TAGLINE

Flutter 版本管理器

# TLDR

**安装 Flutter 版本**

```fvm install [3.0.0]```

在项目中**使用指定版本**

```fvm use [3.0.0]```

**列出已安装的版本**

```fvm list```

**设置全局默认版本**

```fvm global [3.0.0]```

**显示可用发行版**

```fvm releases```

# SYNOPSIS

**fvm** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作：install、use、list、global、remove 等。

**install** _VERSION_
> 安装 Flutter 版本。

**use** _VERSION_
> 设置项目使用的 Flutter 版本。

**global** _VERSION_
> 设置全局默认版本。

**list**
> 列出已安装的版本。

**releases**
> 显示可用版本。

**remove** _VERSION_
> 卸载某个版本。

**--help**
> 显示帮助信息。

# CONFIGURATION

**.fvmrc**（fvm 3+）或 **.fvm/fvm_config.json**（旧版）
> 项目级的 Flutter 版本锁定文件，随源代码一起提交。

**~/fvm/versions**
> 存放缓存的 Flutter SDK 检出的目录（项目通过 `.fvm/flutter_sdk` 符号链接到它）。

# DESCRIPTION

**fvm**（Flutter Version Management）用于管理多个 Flutter SDK 版本。它支持按项目锁定版本，避免需要不同 Flutter 版本的多个项目之间发生冲突。

该工具会下载并缓存 Flutter 版本，通过创建符号链接实现快速切换。项目设置保存在 .fvm 目录中。IDE 集成让开发体验无缝衔接。

对于维护多个 SDK 要求不同的 Flutter 项目来说，fvm 必不可少。

# CAVEATS

每个版本都需要可观的磁盘空间。集成需要在 IDE 中进行配置。某些版本可能已被弃用。

# HISTORY

fvm 的诞生是为了解决开发者在处理多个项目或团队中不同 SDK 需求时面临的 Flutter 版本管理难题。

# INSTALL

```pacman: sudo pacman -S fvm```

```brew: brew install fvm```

```nix: nix profile install nixpkgs#fvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flutter](/man/flutter)(1), [dart](/man/dart)(1)
