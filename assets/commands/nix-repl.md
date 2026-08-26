# TAGLINE

启动交互式 Nix 表达式求值器

# TLDR

**启动 Nix REPL**

```nix repl```

**将 nixpkgs 软件包集载入作用域**

```nix repl --expr 'import <nixpkgs> {}'```

**打开 REPL 并将 flake 的输出纳入作用域**

```nix repl [.#]```

**将某个 Nix 文件的属性载入作用域**

```nix repl --file [default.nix]```

# SYNOPSIS

**nix** **repl** [_options_] [_files_]

# PARAMETERS

_FILES_
> 其顶层属性将被引入作用域的 Nix 文件。

**--expr** _EXPR_
> 对给定表达式求值，并将其属性引入作用域。

**--file** _PATH_
> 从给定的 Nix 文件加载属性（旧的按位置传参写法仍然有效）。

**--arg** _NAME_ _EXPR_
> 将命名参数作为 Nix 表达式传递给所加载的文件或 flake。

**--argstr** _NAME_ _STRING_
> 将命名参数作为字符串传入。

**--help**
> 显示帮助信息。

# REPL COMMANDS

**:?**
> 显示可用的 REPL 命令列表。

**:l** _PATH_
> 加载一个 Nix 文件，并将其属性加入作用域。

**:r**
> 重新加载所有已加载的文件。

**:b** _EXPR_
> 构建一个派生并打印其输出路径。

**:e** _EXPR_
> 在 `$EDITOR` 中打开给定值所在的位置。

**:t** _EXPR_
> 显示给定表达式的类型。

**:q**
> 退出 REPL（Ctrl-D 也可以）。

# DESCRIPTION

**nix repl** 为 Nix 表达式语言启动交互式的读取-求值-打印循环（REPL）。它适合用于探索软件包属性、调试表达式以及试验配置方案。

表达式采用惰性求值。除普通的 Nix 表达式之外，REPL 还支持属性名的 Tab 补全，并接受以冒号开头的元命令（见 REPL COMMANDS）。

# CAVEATS

属于实验性的 `nix` 命令（通过 `experimental-features = nix-command flakes` 启用）。旧的独立 `nix-repl` 二进制文件已被弃用，应改用 `nix repl`。完整命令列表可在 REPL 内输入 `:?` 查看。

# HISTORY

`nix repl` 提供交互式求值功能，便于探索和调试 Nix 表达式。随着统一 `nix` 命令的推出，它取代了独立的 `nix-repl` 工具。

# SEE ALSO

[nix](/man/nix)(1), [nix-eval](/man/nix-eval)(1), [nix-instantiate](/man/nix-instantiate)(1)
