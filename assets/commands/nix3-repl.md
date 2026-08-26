# TAGLINE

启动交互式 Nix Shell

# TLDR

**启动 REPL**

```nix3 repl```

**加载 nixpkgs**

```nix3 repl '<nixpkgs>'```

**加载 flake**

```nix3 repl [.#]```

# SYNOPSIS

**nix3** **repl** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要加载的文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix3 repl** 启动交互式 Nix Shell。是 nix repl 的别名。

该工具对表达式进行求值。支持 Tab 补全和历史记录。

# CAVEATS

nix repl 的别名。输入 :? 获取帮助。用于表达式求值。

# HISTORY

nix3 repl 为 Nix 表达式提供**交互式求值**与探索能力。

# SEE ALSO

[nix](/man/nix)(1), [nix-repl](/man/nix-repl)(1), [nix3-eval](/man/nix3-eval)(1)
