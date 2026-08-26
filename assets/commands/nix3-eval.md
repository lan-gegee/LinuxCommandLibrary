# TAGLINE

新一代 Nix 3

# TLDR

**求值 Nix 表达式**

```nix eval --expr '1 + 2'```

**求值 flake 属性**

```nix eval [.#packages.x86_64-linux.default]```

**求值 nixpkgs 属性**

```nix eval nixpkgs#hello.version```

**以 JSON 格式输出**

```nix eval --json nixpkgs#hello.meta```

**原始字符串输出**

```nix eval --raw nixpkgs#hello.name```

**从文件读取**

```nix eval -f [file.nix]```

# SYNOPSIS

**nix eval** [_options_] _installable_

# PARAMETERS

**--expr** _expr_
> 求值表达式。

**--json**
> 以 JSON 格式输出。

**--raw**
> 原始输出（不带引号）。

**-f** _file_
> 对文件求值。

**--apply** _expr_
> 对结果应用函数。

**--impure**
> 允许不纯求值。

# DESCRIPTION

**nix eval** 是用于求值 Nix 表达式的全新 Nix 3.x 命令。它以更简洁的接口和 flake 支持取代了 nix-instantiate --eval。

# 简单表达式
nix eval --expr 'builtins.length [1 2 3]'
# 输出：3

# flake 属性
nix eval .#packages.x86_64-linux.hello.version

# 应用函数
nix eval nixpkgs#lib --apply 'lib: lib.version'
```

# CAVEATS

属于实验性的 Nix 3.x 命令。必须启用 Flakes。语法与 nix-instantiate 不同。

# HISTORY

nix eval 作为 Nix 2.4 flakes 实验特性的一部分引入，重新设计了 Nix CLI 以提升易用性。

# SEE ALSO

[nix](/man/nix)(1), [nix-instantiate](/man/nix-instantiate)(1), [nix-build](/man/nix-build)(1)
