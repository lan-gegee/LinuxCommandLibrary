# TAGLINE

从项目中移除软件包的别名

# TLDR

**移除一个软件包**

```bun rm [package]```

**移除多个软件包**

```bun rm [package1] [package2]```

**移除全局软件包**

```bun rm -g [package]```

# SYNOPSIS

**bun** **rm** [_options_] _packages..._

# PARAMETERS

**-g**, **--global**
> 从全局软件包中移除。

# DESCRIPTION

**bun rm** 是 **bun remove** 的别名。它从项目中卸载软件包并将其从 package.json 中移除。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-remove](/man/bun-remove)(1), [bun-install](/man/bun-install)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
