# TAGLINE

列出已安装且不是依赖的顶层软件包

# TLDR

**列出顶层软件包（非依赖）**

```brew leaves```

**仅列出手动安装的叶子包**

```brew leaves -r```

**仅列出作为依赖安装的叶子包**

```brew leaves -p```

**显示叶子包的依赖树**

```brew deps --tree $(brew leaves)```

# SYNOPSIS

**brew leaves** [_options_]

# DESCRIPTION

**brew leaves** 列出那些不被任何其他已安装 formula 或 cask 依赖的 formula。这些就是你显式安装的"顶层"软件包。

该命令显示 Homebrew 依赖图的叶子节点——即可以安全卸载而不会破坏其他软件包的包。

# PARAMETERS

**-r**, **--installed-on-request**
> 仅列出用户手动安装的叶子包。

**-p**, **--installed-as-dependency**
> 仅列出作为其他 formula 的依赖安装的叶子包。

# CAVEATS

与"手动安装"不完全等同——它显示的是没有被其他包依赖的软件包。某个手动安装的包可能被别的包依赖，因此不会出现。要查看真正手动安装的包，请使用 -r 标志。

# SEE ALSO

[brew](/man/brew)(1), [brew-list](/man/brew-list)(1), [brew-autoremove](/man/brew-autoremove)(1)
