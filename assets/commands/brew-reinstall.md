# TAGLINE

卸载并重装 Homebrew 软件包

# TLDR

**重装** formula

```brew reinstall [formula]```

**重装** cask

```brew reinstall --cask [cask]```

带调试输出进行**重装**

```brew reinstall --debug [formula]```

**重装并从源码构建**

```brew reinstall --build-from-source [formula]```

**重装且不加隔离标记**（仅限 cask）

```brew reinstall --no-quarantine [cask]```

交互式**重装**

```brew reinstall --interactive [formula]```

# SYNOPSIS

**brew** **reinstall** [_options_] _formula_|_cask_ [...]

# PARAMETERS

**--cask**
> 将所有命名参数视为 cask。

**--formula**
> 将所有命名参数视为 formula。

**--build-from-source** **-s**
> 即使存在 bottle 也从源码编译 formula。

**--debug** **-d**
> 在安装过程中启用调试模式。

**--interactive** **-i**
> 打开交互式 shell 以调试构建过程。

**--no-quarantine**
> 对 cask 禁用 macOS 隔离属性。

**--force**
> 安装时不检查之前安装的版本。

**--verbose** **-v**
> 打印详细的安装输出。

# DESCRIPTION

**brew reinstall** 先卸载再安装一个 formula 或 cask。它适用于修复损坏的安装、应用新的构建选项，或将软件包刷新到当前版本。

在重装已链接 keg 的 formula 时，该命令会保留配置文件。

# CAVEATS

重装可能中断依赖该 formula 的服务。从重装后的 cask 运行的应用可能需要重启。

# SEE ALSO

[brew](/man/brew)(1), [brew-install](/man/brew-install)(1), [brew-uninstall](/man/brew-uninstall)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-22 -->
