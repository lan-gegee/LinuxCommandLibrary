# TAGLINE

macOS 和 Linux 的软件包管理器

# TLDR

**安装**软件包

```brew install [wget]```

**搜索**软件包

```brew search [node]```

**更新** Homebrew

```brew update```

**升级**软件包

```brew upgrade```

**列出**已安装的软件包

```brew list```

**卸载**软件包

```brew uninstall [package]```

**显示**软件包信息

```brew info [package]```

# SYNOPSIS

**brew** _command_ [_options_] [_formula_]

# DESCRIPTION

**brew**（Homebrew）是一款面向 macOS 和 Linux 的软件包管理器。它从源码或预编译二进制文件安装软件，并管理依赖和版本。Homebrew 已成为 macOS 事实上的标准包管理器。

该工具简化了类 Unix 系统上的软件安装与维护。

# PARAMETERS

**install** _formula_
> 安装软件包。

**uninstall** _formula_
> 移除软件包。

**update**
> 更新 Homebrew 本身。

**upgrade** [_formula_]
> 升级软件包。

**search** _query_
> 搜索软件包。

**list**
> 列出已安装的软件包。

**info** _formula_
> 显示软件包信息。

**doctor**
> 检查系统问题。

**cleanup**
> 移除旧版本。

# CONCEPTS

**Formula**
> 软件包定义（如 wget、node）。

**Cask**
> macOS 图形界面应用（如 firefox、slack）。

**Tap**
> 第三方仓库。

**Cellar**
> 软件包的安装位置（/usr/local/Cellar）。

# COMMON OPERATIONS

```bash
# Install package
brew install node

# Install GUI app (macOS)
brew install --cask firefox

# Update package database
brew update

# Upgrade all packages
brew upgrade

# Show outdated
brew outdated

# Cleanup old versions
brew cleanup

# Add third-party tap
brew tap homebrew/cask-fonts
```

# SERVICES

```bash
# Start service
brew services start postgresql

# List services
brew services list

# Stop service
brew services stop redis
```

# CAVEATS

macOS 的系统更新可能破坏 Homebrew。在 macOS 上需要 Xcode Command Line Tools。可能与系统 Python 冲突。会升级所有依赖（而非最小化更新）。部分软件包下载体积较大。

# HISTORY

**Homebrew** 由 Max Howell 于 **2009** 年创建，旨在为 macOS 提供一个基于 Git 的简单包管理器，现已成为最受欢迎的 macOS 包管理器。

# SEE ALSO

[brew-install](/man/brew-install)(1), [brew-services](/man/brew-services)(1), [apt](/man/apt)(8)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-22 -->
