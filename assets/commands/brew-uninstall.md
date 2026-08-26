# TAGLINE

移除已安装的 Homebrew 软件包

# TLDR

**卸载** formula

```brew uninstall [formula]```

**卸载** cask

```brew uninstall --cask [cask]```

**强制移除**所有版本

```brew uninstall --force [formula]```

卸载时忽略依赖关系

```brew uninstall --ignore-dependencies [formula]```

移除并附带 zap 清理其他文件

```brew uninstall --zap [cask]```

# SYNOPSIS

**brew uninstall** [_options_] _formula|cask_ ...

# DESCRIPTION

**brew uninstall** 移除一个已安装的 formula 或 cask。它会查询 Homebrew 数据库定位软件包，并将其连同关联文件一起删除。

别名：**brew remove**、**brew rm**。

# PARAMETERS

**--force, -f**
> 强制移除，删除该 formula 的所有版本。

**--ignore-dependencies**
> 即使该 formula 是其他软件包的依赖也不报错。

**--formula**
> 将所有参数视为 formula。

**--cask**
> 将所有参数视为 cask。

**--zap**
> 移除与 cask 关联的所有文件（包括偏好设置）。

# RELATED COMMANDS

**brew autoremove**
> 卸载后移除不再使用的依赖。

**brew deps** _formula_
> 卸载前查看依赖关系。

**brew uses** _formula_
> 查看哪些包依赖某个 formula。

# CLEANUP

卸载后运行 **brew autoremove**，可以清除不再被任何已安装软件包需要的依赖。

# CAVEATS

无法卸载不受 Homebrew 管理的软件包。使用 --force 时请谨慎，它会删除所有版本。移除前请用 **brew uses** 检查依赖，避免破坏其他软件包。

# SEE ALSO

[brew](/man/brew)(1), [brew-install](/man/brew-install)(1), [brew-autoremove](/man/brew-autoremove)(1)
