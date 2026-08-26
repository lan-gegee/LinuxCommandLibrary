# TAGLINE

移除已安装的 Homebrew 软件包

# TLDR

**移除** formula

```brew rm [formula]```

**移除** cask

```brew rm --cask [cask]```

**强制移除**所有已安装的版本

```brew rm --force [formula]```

**带 zap 移除**（彻底移除 cask，包括偏好设置和缓存）

```brew rm --zap --cask [cask]```

移除多个 formula

```brew rm [formula1] [formula2] [formula3]```

**预演**将要移除的内容

```brew rm --dry-run [formula]```

# SYNOPSIS

**brew** **rm** [_options_] _formula_|_cask_ [...]

# PARAMETERS

**--cask**
> 将所有命名参数视为 cask。

**--formula**
> 将所有命名参数视为 formula。

**-f**, **--force**
> 删除 formula 的所有已安装版本。对 cask 而言，即使未安装也一并移除。

**--zap**
> 移除与 cask 关联的所有文件，包括偏好设置、缓存和其他共享资源。请谨慎使用。

**--ignore-dependencies**
> 即使仍存在依赖它的 formula，卸载也不报错。

**-n**, **--dry-run**
> 只显示将移除的内容，不实际移除任何东西。

**-d**, **--debug**
> 显示调试信息。

**-v**, **--verbose**
> 让部分输出更详细。

# DESCRIPTION

**brew rm** 是 **brew uninstall** 和 **brew remove** 的别名。它从系统中卸载一个 formula 或 cask。

这三个命令（**rm**、**remove**、**uninstall**）在功能上完全相同。移除 formula 并不会自动移除其不再使用的依赖；请使用 **brew autoremove** 进行清理。

# CAVEATS

如果其他已安装 formula 依赖于待移除的 formula，移除将失败，除非使用 **--ignore-dependencies**。**--zap** 选项可能移除其他应用使用的共享资源。已从 prefix 取消链接的 keg-only formula 同样会被移除。

# SEE ALSO

[brew](/man/brew)(1), [brew-remove](/man/brew-remove)(1), [brew-uninstall](/man/brew-uninstall)(1), [brew-autoremove](/man/brew-autoremove)(1), [brew-install](/man/brew-install)(1), [brew-cleanup](/man/brew-cleanup)(1)
