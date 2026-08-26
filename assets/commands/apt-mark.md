# TAGLINE

更改软件包的安装状态。

# TLDR

将软件包标记为**自动安装**

```sudo apt-mark auto [package]```

将软件包标记为**手动安装**

```sudo apt-mark manual [package]```

将软件包**锁定（hold）**在当前版本

```sudo apt-mark hold [package]```

**允许**软件包再次被更新

```sudo apt-mark unhold [package]```

显示**手动安装的**软件包

```apt-mark showmanual```

显示**自动安装的**软件包

```apt-mark showauto```

显示被**锁定的**软件包

```apt-mark showhold```

# SYNOPSIS

**apt-mark** [_options_] _command_ _package_...

# DESCRIPTION

**apt-mark** 是一个更改已安装软件包状态的实用工具。它可以将软件包标记为自动安装（使其成为 autoremove 的候选）、手动安装，或锁定在当前版本。

# PARAMETERS

**auto package**
> 将软件包标记为自动安装

**manual package**
> 将软件包标记为手动安装

**hold package**
> 将软件包锁定在当前版本，阻止升级

**unhold package**
> 解除锁定，允许软件包被升级

**showmanual**
> 显示手动安装的软件包列表

**showauto**
> 显示自动安装的软件包列表

**showhold**
> 显示被锁定的软件包列表

**showinstall**
> 显示标记为待安装的软件包列表

**showremove**
> 显示标记为待移除的软件包列表

**showpurge**
> 显示标记为待清除的软件包列表

**minimize-manual**
> 将所有依赖软件包标记为 auto，仅保留直接需要的软件包为 manual

**-f, --file filename**
> 从指定文件读写软件包状态，而不是默认位置

**-v, --verbose**
> 详细输出

**-c, --config-file**
> 指定要使用的配置文件

**-o, --option**
> 设置配置选项（语法：-o Foo::Bar=bar）

# CAVEATS

锁定软件包可能在系统升级期间引发依赖问题。请谨慎使用。

# HISTORY

属于为基于 Debian 的系统开发的 **APT**（Advanced Package Tool）工具套件的一部分。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [dpkg](/man/dpkg)(1)
