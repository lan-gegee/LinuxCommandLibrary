# TAGLINE

管理全局安装的 Pixi 软件包

# TLDR

**全局安装软件包**

```pixi global install [package]```

**列出全局安装的软件包**

```pixi global list```

**移除全局软件包**

```pixi global remove [package]```

**更新所有全局环境**

```pixi global update```

**更新指定的**全局环境

```pixi global update [package]```

将清单与已安装的环境**同步**

```pixi global sync```

**编辑**全局清单文件

```pixi global edit```

# SYNOPSIS

**pixi** **global** _command_ [_options_]

# PARAMETERS

**install** _package_
> 将软件包安装到全局可访问的位置并暴露其可执行文件。

**uninstall** _environment_
> 卸载一个全局环境。

**list**
> 列出全局环境及其依赖和暴露的命令。

**add** _package_
> 向全局环境添加依赖。

**remove** _package_
> 从全局环境移除依赖。

**update** [_environment..._]
> 更新全局环境。不带参数时更新所有环境。

**sync**
> 将全局清单与已安装的环境同步。

**edit**
> 在编辑器中打开全局清单文件。

**expose**
> 管理全局环境中二进制文件的暴露方式。

**shortcut**
> 管理机器上针对全局环境的快捷方式。

**tree**
> 显示特定全局环境的依赖树。

# DESCRIPTION

**pixi global** 用于管理全局安装的软件包，可将命令行工具安装为随处可用，类似于 Python 的 pipx。各软件包在各自的环境中相互隔离。

# INSTALL

```pacman: sudo pacman -S pixi```

```brew: brew install pixi```

```nix: nix profile install nixpkgs#pixi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pixi](/man/pixi)(1), [pipx](/man/pipx)(1), [conda](/man/conda)(1)
