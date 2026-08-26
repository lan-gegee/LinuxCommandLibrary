# TAGLINE

从项目中移除软件包

# TLDR

**移除一个软件包**

```bun remove [package]```

**移除多个软件包**

```bun remove [package1] [package2]```

**移除全局软件包**

```bun remove -g [package]```

# SYNOPSIS

**bun** **remove** [_options_] _packages..._

# PARAMETERS

**-g**, **--global**
> 从全局软件包中移除。

**-d**, **--dev**
> 从 devDependencies 中移除。

# DESCRIPTION

**bun remove** 从项目中卸载软件包并将其从 package.json 中移除。这等同于 **npm uninstall** 或 **yarn remove**。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-rm](/man/bun-rm)(1), [bun-install](/man/bun-install)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
