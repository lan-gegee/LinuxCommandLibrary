# TAGLINE

对 Nix 表达式求值

# TLDR

**求值表达式**

```nix eval --expr "[1 + 1]"```

**从 flake 求值**

```nix eval [.#packages.x86_64-linux.default]```

**求值并应用函数**

```nix eval --apply [builtins.attrNames] --expr "{a=1; b=2;}"```

**以 JSON 格式输出**

```nix eval --json --expr "[{a = 1;}]"```

**对文件求值**

```nix eval -f [file.nix]```

**输出原始字符串**

```nix eval --raw --expr "\"hello\""```

# SYNOPSIS

**nix** **eval** [_options_] [_installable_]

# PARAMETERS

_INSTALLABLE_
> 要求值的 flake 属性。

**--expr** _EXPR_
> Nix 表达式。

**--json**
> 以 JSON 格式输出。

**--raw**
> 输出原始字符串。

**--apply** _FUNC_
> 对结果应用指定函数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix eval** 对 Nix 表达式求值，并输出求值结果。

该工具用于检查 Nix 值，方便调试和查询。

# CAVEATS

属于 Nix CLI。需要注意表达式语法。既支持 flakes 也支持普通表达式。

# HISTORY

nix eval 是**新 Nix CLI** 的一部分，提供表达式求值功能。

# SEE ALSO

[nix](/man/nix)(1), [nix-repl](/man/nix-repl)(1), [nix-instantiate](/man/nix-instantiate)(1)
