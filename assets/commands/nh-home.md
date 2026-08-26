# TAGLINE

管理 home-manager 配置

# TLDR

**切换 home 配置**

```nh home switch```

**仅构建不切换**

```nh home build```

**使用 flake 切换**

```nh home switch --flake [.#username]```

# SYNOPSIS

**nh home** _command_ [_options_]

# PARAMETERS

**switch**
> 构建并激活 home 配置。

**build**
> 仅构建配置。

**--flake** _ref_
> Flake 引用。

**--dry**
> 试运行。

**--ask**
> 激活前先询问。

# DESCRIPTION

**nh home** 管理 home-manager 配置，是 home-manager 的友好封装，输出更清晰并支持 flake。属于 nh（nix helper）工具集。

# INSTALL

```nix: nix profile install nixpkgs#nh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nh](/man/nh)(1), [home-manager](/man/home-manager)(1)
