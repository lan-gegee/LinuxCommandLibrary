# TAGLINE

通过 Homebrew 安装软件包

# TLDR

**安装** formula

```brew install [formula]```

**安装** cask

```brew install --cask [cask]```

**安装**而不升级已有版本

```HOMEBREW_NO_INSTALL_UPGRADE=1 brew install [formula]```

失败时进入调试会话进行安装

```brew install --debug [formula]```

强制安装而不检查现有版本

```brew install --force [formula]```

**安装并显示**安装耗时

```brew install --display-times [formula]```

**安装最新的开发（HEAD）版本**

```brew install --HEAD [formula]```

**预览**将安装的内容而不实际安装

```brew install --dry-run [formula]```

# SYNOPSIS

**brew install** [_options_] _formula|cask_ ...

# DESCRIPTION

**brew install** 安装一个 formula 或 cask。如果该 formula 已安装但已过时，除非设置了 HOMEBREW_NO_INSTALL_UPGRADE，否则它会被升级。

安装完成后会自动对已安装的 formula 执行清理；除非设置了 HOMEBREW_NO_INSTALL_CLEANUP，否则也会每 30 天对所有 formula 清理一次。

# PARAMETERS

**--cask**
> 将所有参数视为 cask。

**--formula**
> 将所有参数视为 formula。

**--force**
> 安装时不检查之前安装过的 keg-only 或未迁移版本。

**--debug**
> 若构建失败则打开交互式调试会话。

**--display-times**
> 打印每个软件包的安装耗时。

**--verbose**
> 打印详细的构建信息。

**-s, --build-from-source**
> 从源码编译 formula 而不是使用 bottle。

**--force-bottle**
> 即使通常不会使用 bottle 也从 bottle 安装。

**--HEAD**
> 安装 HEAD 版本，从上游仓库拉取最新提交。

**-n, --dry-run**
> 只显示将安装的内容，不实际安装任何东西。

**--keep-tmp**
> 安装后保留临时构建文件。

**--include-test**
> 安装运行 brew test 所需的测试依赖。

# ENVIRONMENT

**HOMEBREW_NO_INSTALL_UPGRADE**
> 阻止自动升级过时的 formula。

**HOMEBREW_NO_INSTALL_CLEANUP**
> 阻止安装后自动清理。

**HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK**
> 跳过对过时被依赖项的检查。

# CAVEATS

可以在命令后追加特定 formula 专属选项。有 bottle（预编译二进制）时会优先使用。在 macOS 上从源码构建需要 Xcode Command Line Tools。

# SEE ALSO

[brew](/man/brew)(1), [brew-uninstall](/man/brew-uninstall)(1), [brew-upgrade](/man/brew-upgrade)(1), [brew-info](/man/brew-info)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-19 -->
