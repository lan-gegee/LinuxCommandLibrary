# TAGLINE

从 flake 构建 derivation

# TLDR

**在当前目录中构建 flake 的默认软件包**

```nix build```

**构建当前 flake 的特定输出**

```nix build .#[package]```

**从 nixpkgs 构建**

```nix build nixpkgs#[hello]```

**构建但不创建 result 符号链接**

```nix build --no-link```

**构建并打印完整构建日志**

```nix build -L [installable]```

**构建并打印输出存储路径**

```nix build --print-out-paths [installable]```

**试运行**而不实际构建

```nix build --dry-run [installable]```

# SYNOPSIS

**nix build** [_options_] [_installable_...]

# PARAMETERS

_INSTALLABLE_
> 要构建的 flake 引用、属性路径或存储路径（例如 _.#default_、_nixpkgs#hello_）。

**--no-link**
> 不创建 result 符号链接。

**-o** _PATH_, **--out-link** _PATH_
> 使用 _PATH_ 作为 result 符号链接的前缀（默认：_result_）。

**--rebuild**
> 重新构建一个已构建过的 derivation 并比较输出。

**--print-out-paths**
> 将生成的存储路径打印到标准输出。

**-L**, **--print-build-logs**
> 在标准错误上显示完整构建日志。

**--json**
> 以 JSON 格式打印构建结果。

**--dry-run**
> 显示将会构建或拉取的内容，但不实际执行。

**--impure**
> 允许对不纯表达式进行求值（例如引用环境变量）。

**--refresh**
> 将所有先前下载的文件视为过期。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nix build**（在本手册的命名空间中调用为 **nix3-build**，以区别于旧版的 **nix-build**）会构建指定的 installable，它们可以是 flake 引用、属性路径或存储路径。成功时，它会创建一个名为 _result_ 的符号链接（其他额外输出为 _result-N_），指向 Nix store 中的构建产物。

当给定多个 installable 时，会在配置的构建并发数范围内并行构建每一个。

# CAVEATS

属于新版 **nix** CLI 的一部分；需要启用 _nix-command_ 和 _flakes_ 实验特性（通过 _nix.conf_ 或 _--extra-experimental-features_）。行为可能随 Nix 版本更迭而变化。

# HISTORY

nix3 指的是 **Nix 3.x CLI**，其中 build 是主要的编译命令。

# SEE ALSO

[nix](/man/nix)(1), [nix-build](/man/nix-build)(1), [nix3-develop](/man/nix3-develop)(1)
