# TAGLINE

显示当前线上配置与拟定配置之间的差异

# TLDR

**显示与线上配置的差异**

```kubectl diff -f [manifest.yaml]```

**比较整个目录**

```kubectl diff -f [manifests/]```

**从 stdin 比较**

```cat [manifest.yaml] | kubectl diff -f -```

# SYNOPSIS

**kubectl** **diff** [_options_]

# PARAMETERS

**-f**, **--filename** _file_
> 包含待比较配置的文件。

**-R**, **--recursive**
> 递归处理目录。

**-l**, **--selector** _selector_
> 用于过滤的标签选择器。

# DESCRIPTION

**kubectl diff** 显示当前线上配置与文件中拟定配置之间的差异。有助于在应用更改前进行预览。使用服务端试运行来计算差异。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-apply](/man/kubectl-apply)(1)
