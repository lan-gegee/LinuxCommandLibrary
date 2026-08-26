# TAGLINE

列出已安装的软件包

# TLDR

**列出已安装的软件包**

```bun pm ls```

**列出所有软件包**包括嵌套的依赖

```bun pm ls --all```

# SYNOPSIS

**bun** **pm** **ls** [_options_]

# PARAMETERS

**--all**
> 显示所有依赖，包括嵌套依赖。

# DESCRIPTION

**bun pm ls** 列出当前项目中安装的软件包。默认显示顶层依赖。使用 **--all** 可显示完整的依赖树，包括传递依赖。

此命令等同于 **bun list**。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-pm](/man/bun-pm)(1), [bun-list](/man/bun-list)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
