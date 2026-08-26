# TAGLINE

管理 GitLab CI/CD 流水线

# TLDR

**列出流水线**

```glab pipeline list```

查看流水线

```glab pipeline view [id]```

运行流水线

```glab pipeline run```

带变量运行

```glab pipeline run --variables [KEY:VALUE]```

显示 CI 状态

```glab pipeline ci status```

查看作业

```glab pipeline ci view```

# SYNOPSIS

**glab** **pipeline** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出流水线。

**view**
> 查看流水线详情。

**run**
> 触发流水线。

**status**
> 显示流水线状态。

**delete**
> 删除流水线。

**ci**
> CI 相关命令。

# PARAMETERS

**--variables** _vars_
> 流水线变量。

**--branch** _branch_
> 要在其上运行的分支。

# DESCRIPTION

**glab pipeline** 在命令行中管理 GitLab CI/CD 流水线。它提供查看、触发和监控流水线的子命令，还可以检查单个作业的详情和日志。

# INSTALL

```apt: sudo apt install glab```

```dnf: sudo dnf install glab```

```pacman: sudo pacman -S glab```

```apk: sudo apk add glab```

```zypper: sudo zypper install glab```

```brew: brew install glab```

```nix: nix profile install nixpkgs#glab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glab](/man/glab)(1)
