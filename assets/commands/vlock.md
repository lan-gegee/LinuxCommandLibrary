# TAGLINE

锁定 Linux 虚拟控制台会话

# TLDR

**锁定**当前控制台

```vlock```

通过选项锁定**当前**控制台

```vlock -c```

锁定**所有**控制台

```vlock -a```

显示**帮助**

```vlock -h```

显示**版本**

```vlock -v```

# SYNOPSIS

**vlock** [_OPTIONS_]

# PARAMETERS

**-c, --current**
> 仅锁定当前虚拟控制台

**-a, --all**
> 锁定所有虚拟控制台

**-h, --help**
> 显示帮助信息

**-v, --version**
> 显示版本信息

# DESCRIPTION

**vlock** 用于锁定虚拟控制台会话，解锁时需要输入密码。它既可以锁定当前控制台，也可以锁定系统上的所有虚拟控制台。

这为文本模式的控制台会话提供了物理安全保障，类似于图形环境中的屏幕锁定。

# CAVEATS

锁定所有控制台后，没有密码将无法访问任何控制台。root 仍可解锁。仅适用于虚拟控制台，不适用于伪终端。

# INSTALL

```apt: sudo apt install vlock```

```apk: sudo apk add kbd-vlock```

```nix: nix profile install nixpkgs#vlock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[physlock](/man/physlock)(1)
