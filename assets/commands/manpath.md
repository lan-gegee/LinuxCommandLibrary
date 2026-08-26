# TAGLINE

确定并显示用于查找手册页的搜索路径

# TLDR

显示**搜索路径**

```manpath```

显示**全局** manpath

```manpath --global```

# SYNOPSIS

**manpath** [_options_]

# DESCRIPTION

**manpath** 确定并显示用于查找手册页的搜索路径。它会检查配置文件和环境变量来构建该路径。

# PARAMETERS

**-g, --global**
> 显示完整的全局 manpath

**-d, --debug**
> 打印调试信息

**-q, --quiet**
> 抑制警告

**-c, --catpath**
> 显示 catpath 而不是 manpath

**-V, --version**
> 显示版本信息

**-h, --help**
> 显示帮助

# ENVIRONMENT

**MANPATH**：覆盖默认搜索路径
**PATH**：在未设置 MANPATH 时用于推导 manpath

# CAVEATS

如果已设置 **MANPATH**，**manpath** 通常会原样返回其值（或按配置文件进行补充）。否则它会从 **/etc/manpath.config** 和 **PATH** 推导路径。

# INSTALL

```apt: sudo apt install man-db```

```dnf: sudo dnf install man-db```

```pacman: sudo pacman -S man-db```

```apk: sudo apk add man-db```

```brew: brew install man-db```

```nix: nix profile install nixpkgs#man-db```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [mandb](/man/mandb)(8)
