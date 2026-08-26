# TAGLINE

管理 NixOS 系统配置

# TLDR

**切换到新配置**

```nh os switch```

**仅构建不切换**

```nh os build```

**测试配置**

```nh os test```

**将新配置设为启动默认**

```nh os boot```

# SYNOPSIS

**nh os** _command_ [_options_]

# PARAMETERS

**switch**
> 构建并激活配置。

**build**
> 仅构建配置。

**test**
> 构建并临时激活。

**boot**
> 构建并设为启动默认项。

**--flake** _ref_
> Flake 引用。

**--dry**
> 试运行。

**--ask**
> 激活前先询问。

# DESCRIPTION

**nh os** 管理 NixOS 系统配置，是 nixos-rebuild 的友好封装，输出更清晰并支持 flake。属于 nh（nix helper）工具集。

# INSTALL

```nix: nix profile install nixpkgs#nh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nh](/man/nh)(1), [nixos-rebuild](/man/nixos-rebuild)(1)
