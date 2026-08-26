# TAGLINE

移除已安装的 Homebrew 软件包

# TLDR

**移除** formula

```brew remove [formula]```

**移除** cask

```brew remove --cask [cask]```

移除与 cask 关联的所有文件（包括偏好设置和缓存）

```brew remove --zap [cask]```

即使有其他 formula 依赖它也**强制移除**

```brew remove --force [formula]```

移除并忽略依赖关系

```brew remove --ignore-dependencies [formula]```

# SYNOPSIS

**brew** **remove** [_options_] _formula_|_cask_ [...]

# PARAMETERS

**--cask**
> 将所有命名参数视为 cask。

**--formula**
> 将所有命名参数视为 formula。

**--force**, **-f**
> 删除 formula 的所有已安装版本。对 cask 而言，即使未安装也执行卸载、覆盖现有文件并忽略错误。

**--zap**
> 移除与 cask 关联的所有文件。可能删除应用程序之间共享的文件。

**--ignore-dependencies**
> 存在依赖它的 formula 时卸载也不报错。

# DESCRIPTION

**brew remove** 卸载一个 formula 或 cask。它是 **brew uninstall** 的别名。它移除已安装的文件，但默认保留配置文件，也不会移除依赖。

对于 cask，使用 **--zap** 可进行更彻底的移除，包括应用偏好设置和缓存。

# CAVEATS

如果其他 formula 依赖于待移除的 formula，移除将失败，除非使用 **--ignore-dependencies**。cask 的 **--zap** 选项可能删除用户数据。

# SEE ALSO

[brew](/man/brew)(1), [brew-uninstall](/man/brew-uninstall)(1), [brew-rm](/man/brew-rm)(1), [brew-autoremove](/man/brew-autoremove)(1), [brew-cleanup](/man/brew-cleanup)(1)
