# TAGLINE

构建 Nix 派生并创建 result 符号链接

# TLDR

**在当前目录中构建默认表达式**

```nix-build```

**构建指定的 Nix 表达式**

```nix-build [file.nix]```

**从文件构建命名属性**

```nix-build [file.nix] -A [attribute]```

**向表达式传递类型化参数**

```nix-build --arg [name] [value]```

**向表达式传递字符串参数**

```nix-build --argstr [name] "[string]"```

**失败后继续构建其他派生**

```nix-build --keep-going```

**只显示将要构建的内容而不实际构建**

```nix-build --dry-run```

**构建但不创建 result 符号链接**

```nix-build --no-out-link```

# SYNOPSIS

**nix-build** [_options_] [_paths_...]

# PARAMETERS

_PATH_
> Nix 表达式文件或属性的路径。默认为 **default.nix**。

**-A** _attr_, **--attr** _attr_
> 从顶层表达式中选择一个属性（支持点分路径）。

**--arg** _NAME_ _VALUE_
> 将 **VALUE**（一个 Nix 表达式）作为参数 **NAME** 传入。

**--argstr** _NAME_ _VALUE_
> 将 **VALUE** 作为字符串参数 **NAME** 传入。

**--keep-going**, **-k**
> 出现失败后仍继续构建其余依赖。

**--dry-run**
> 显示哪些派生将被构建或替代获取，但不真正构建。

**--no-out-link**
> 不创建指向输出的 **result** 符号链接。

**-o** _name_, **--out-link** _name_
> 修改结果符号链接的名称（默认：**result**）。

**-j** _n_, **--max-jobs** _n_
> 并行构建的派生数量。

**--option** _NAME_ _VALUE_
> 设置任意的 Nix 配置项。

# DESCRIPTION

**nix-build** 是经典的 Nix 命令行工具之一。它把 Nix 表达式求值为一个或多个派生，然后将其实现（构建或替代获取其输出），并在当前目录创建名为 **result** 的符号链接，指向输出路径。如果产出多个输出，符号链接会依次命名为 **result**、**result-2** 等。

本 man page 变体描述的与 **nix-build(1)** 是同一个二进制程序，只是在某些发行版中被归入不同的章节发布。

# CAVEATS

**result** 符号链接是一个垃圾回收根（GC root），可以防止构建输出被垃圾回收。不再需要该输出时，请删除这个符号链接（或者一开始就用 **--no-out-link**）。基于 flake 的工作流请优先使用较新的 **nix build** 命令。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-build](/man/nix-build)(1), [nix](/man/nix)(1), [nix-env](/man/nix-env)(1), [nix-store](/man/nix-store)(1)
