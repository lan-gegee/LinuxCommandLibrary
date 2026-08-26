# TAGLINE

为其他 git 命令挑选并整理参数

# TLDR

**获取提交哈希值**

```git rev-parse HEAD```

**获取短哈希值**

```git rev-parse --short HEAD```

**获取分支名**

```git rev-parse --abbrev-ref HEAD```

**获取仓库根目录**

```git rev-parse --show-toplevel```

**检查是否在 git 仓库中**

```git rev-parse --is-inside-work-tree```

**获取 git 目录**

```git rev-parse --git-dir```

**验证**某个引用是否存在（无效时以非零值退出）

```git rev-parse --verify [ref]```

**获取**从仓库根目录到当前目录的路径

```git rev-parse --show-prefix```

# SYNOPSIS

**git** **rev-parse** [_options_] _args_...

# PARAMETERS

**--short** [_length_]
> 缩短的哈希值。

**--abbrev-ref**
> 显示短引用名。

**--verify**
> 验证对象是否存在。

**--show-toplevel**
> 显示仓库根目录。

**--git-dir**
> 显示 .git 目录。

**--is-inside-work-tree**
> 检查是否在工作树内。

**--show-prefix**
> 显示当前目录相对于仓库根目录的路径。

**--show-cdup**
> 显示从当前目录回到仓库根目录的路径。

**--is-bare-repository**
> 若仓库为裸仓库则输出 "true"，否则输出 "false"。

**--absolute-git-dir**
> 类似 --git-dir，但输出始终是绝对路径。

**--symbolic**
> 显示符号名称而不是 SHA-1。

**--symbolic-full-name**
> 类似 --symbolic，但显示完整引用名（例如 refs/heads/master）。

**--quiet**
> 仅与 --verify 搭配时有意义。失败时不输出错误信息，只以非零状态退出。

# DESCRIPTION

**git rev-parse** 将引用名、符号引用及其他参数转换为 SHA-1 哈希值。它还能提供仓库结构相关的信息，例如根目录、git 目录和当前分支。

这个底层（plumbing）命令在脚本中被广泛使用，用于解析引用和查询仓库元数据。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-rev-list](/man/git-rev-list)(1), [git-describe](/man/git-describe)(1), [git-symbolic-ref](/man/git-symbolic-ref)(1), [git-log](/man/git-log)(1)
