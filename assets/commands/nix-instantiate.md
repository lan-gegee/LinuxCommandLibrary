# TAGLINE

实例化 Nix 表达式，生成 store 派生（derivation）

# TLDR

**实例化表达式**

```nix-instantiate [expression.nix]```

**求值并打印**

```nix-instantiate --eval [expression.nix]```

**求值为 JSON**

```nix-instantiate --eval --json [expression.nix]```

**仅解析（检查语法）**

```nix-instantiate --parse [expression.nix]```

**使用命令行给出的表达式**

```nix-instantiate --eval -E '1 + 2'```

# SYNOPSIS

**nix-instantiate** [_options_] _files_...

# PARAMETERS

**--eval**
> 求值并打印结果。

**--json**
> 以 JSON 格式输出。

**--strict**
> 严格求值。

**--parse**
> 仅解析。

**-E** _expr_
> 对给定表达式求值。

**--arg** _name_ _value_
> 传入参数。

**-A** _attr_
> 选择属性。

# DESCRIPTION

**nix-instantiate** 实例化 Nix 表达式，生成 store 派生。配合 --eval 时，它会对表达式求值并打印结果。

这可用于调试和测试 Nix 表达式。
# Evaluate expression
nix-instantiate --eval -E 'let x = 1; in x + 1'
# Output: 2

# Get derivation
nix-instantiate '<nixpkgs>' -A hello
# Output: /nix/store/...-hello.drv
```

# CAVEATS

较新的 nix 命令（如 nix eval）已取代它的部分用途。要得到完整的值需要严格求值。属于旧版 Nix CLI。

# HISTORY

nix-instantiate 是最早的 Nix 命令之一，自 **Nix** 于 **2003 年**首次发布以来就是核心工具链的一部分。

# SEE ALSO

[nix-build](/man/nix-build)(1), [nix-store](/man/nix-store)(1), [nix-env](/man/nix-env)(1)

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->
