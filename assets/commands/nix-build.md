# TAGLINE

构建 Nix 表达式

# TLDR

**构建 default.nix**

```nix-build```

**构建指定文件**

```nix-build [path/to/file.nix]```

**按属性构建**

```nix-build -A [attribute]```

**从表达式构建**

```nix-build -E "[with import <nixpkgs> {}; hello]"```

**不创建 result 符号链接**

```nix-build --no-out-link```

**构建并保留输出**

```nix-build -o [result-link]```

**显示构建日志**

```nix-build -v```

# SYNOPSIS

**nix-build** [_options_] [_path_]

# PARAMETERS

_PATH_
> Nix 表达式文件。

**-A** _ATTR_
> 构建指定属性。

**-E** _EXPR_
> 构建给定表达式。

**--no-out-link**
> 不创建结果链接。

**-o** _LINK_
> 输出符号链接的名称。

**-v**
> 详细模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix-build** 用于构建 Nix 表达式。它会创建派生并对其进行构建。

该工具把产物输出到 /nix/store 中，并且默认创建 result 符号链接。

# CAVEATS

属于旧版命令。可以考虑改用 nix build。必须提供 Nix 表达式。

# HISTORY

nix-build 是 **Nix** 的组成部分，提供了传统的构建命令接口。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-shell](/man/nix-shell)(1), [nix-env](/man/nix-env)(1)
