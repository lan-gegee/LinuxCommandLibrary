# TAGLINE

从栈中移除栈顶值

# TLDR

**从栈中弹出值（Forth）**

```pop```

**在 dc 计算器中弹出**

```echo "1 2 3 R p" | dc```

# SYNOPSIS

**pop** [_options_]

# PARAMETERS

栈操作命令。

# DESCRIPTION

**pop** 移除并丢弃栈顶的值。它是基于栈的编程语言和计算器（如 Forth 和 dc）中的基础操作。

在 shell 环境中，相关的 **popd** 命令对 shell 的目录栈执行类似的操作。pop 操作是 push 的逆操作。

# CAVEATS

取决于具体环境。是基于栈的语言的一部分。

# HISTORY

pop 是计算机科学中的基础**栈操作**。

# INSTALL

```zypper: sudo zypper install pop```

```brew: brew install pop```

```nix: nix profile install nixpkgs#pop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dc](/man/dc)(1), [forth](/man/forth)(1), [pushd](/man/pushd)(1)
