# TAGLINE

Haskell 的交互式 REPL 环境

# TLDR

**启动交互式会话**

```ghci```

**加载文件**

```ghci [file.hs]```

**在会话中加载模块**

```:load [file.hs]```

**获取表达式类型**

```:type [expression]```

**重新加载当前模块**

```:reload```

# SYNOPSIS

**ghci** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要加载的 Haskell 文件。

**:load** _FILE_
> 加载模块。

**:reload**
> 重新加载当前各模块。

**:type**, **:t** _EXPR_
> 显示表达式的类型。

**:kind**, **:k** _TYPE_
> 显示类型的 kind。

**:info** _NAME_
> 显示该名称的信息，包括定义和实例。

**:browse** _MODULE_
> 列出某模块导出的标识符。

**:set** _OPTION_
> 为会话设置 GHCi 或编译器选项。

**:main** _ARGS_
> 以给定参数运行程序的 `main`。

**:quit**, **:q**
> 退出 GHCi。

**-i** _DIR1:...:DIRn_
> 将目录加入源文件搜索路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ghci** 是 GHC（Glasgow Haskell Compiler）的交互式环境。它提供一个 REPL，可用于求值 Haskell 表达式、加载模块，以及交互式地探索类型。

GHCi 支持 GHC 的所有语言扩展，并能即时编译模块。它提供内省命令，用于检查类型、kind 和文档。Tab 补全和命令历史进一步提升了易用性。

# CONFIGURATION

**~/.ghci**
> 用户级启动文件，GHCi 启动时加载，内含默认设置、导入和自定义命令。

**./.ghci**
> 项目级启动文件，在用户文件之后加载（必须具备安全权限才会被读取）。

# CAVEATS

某些已编译代码在解释器中的行为可能不同。大型表达式可能导致内存占用增长。重启会清空解释器状态。

# HISTORY

GHCi 随 **2001 年**发布的 **GHC 5.0** 推出，在批处理编译器之外提供了交互式的 Haskell 求值能力。

# INSTALL

```apt: sudo apt install ghc```

```dnf: sudo dnf install ghc```

```pacman: sudo pacman -S ghc```

```apk: sudo apk add ghc```

```zypper: sudo zypper install ghc```

```brew: brew install ghc```

```nix: nix profile install nixpkgs#ghc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghc](/man/ghc)(1), [ghcid](/man/ghcid)(1), [cabal](/man/cabal)(1), [stack](/man/stack)(1), [runghc](/man/runghc)(1)
