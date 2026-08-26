# TAGLINE

提供临时搭建的开发环境

# TLDR

**快速进入软件包 Shell**

```nix-shell -p [package]```

**包含多个软件包的 Shell**

```nix-shell -p [git] [curl] [jq]```

**执行后退出**

```nix-shell -p [ripgrep] --run "rg pattern"```

**从表达式生成环境**

```nix-shell -E "with import <nixpkgs> {}; mkShell { buildInputs = [hello]; }"```

# SYNOPSIS

**nix-shell** [_options_]

# PARAMETERS

**-p** _PKG_
> 把软件包加入 Shell。

**--run** _CMD_
> 执行命令后退出。

**-E** _EXPR_
> 对给定表达式求值。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix-shell** 提供临时（ad-hoc）的开发环境。本文件是该命令的另一份文档版本。

该工具是快速配置环境的利器，且不会对系统造成永久性更改。

# CAVEATS

会下载软件包。需要网络。使用 Nix store 存放内容。

# HISTORY

nix-shell 是一款基础性的 **Nix** 工具，用于打造可复现的开发环境。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-shell](/man/nix-shell)(1), [nix-develop](/man/nix-develop)(1), [nix](/man/nix)(1)
