# TAGLINE

列出容器镜像仓库的标签

# TLDR

**列出仓库中的标签**

```gcrane ls [gcr.io/project/repo]```

**递归列出**标签和子仓库

```gcrane ls -r [gcr.io/project]```

**以 JSON 格式列出**

```gcrane ls --json [gcr.io/project/repo]```

# SYNOPSIS

**gcrane** **ls** [_options_] _repository_

# PARAMETERS

**-r**, **--recursive**
> 遍历子仓库。

**--json**
> 以 JSON 格式输出清单信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**gcrane ls** 列出 Google Container Registry 和 Artifact Registry 中的标签、清单和子仓库。与标准的 crane ls 不同，它提供更丰富的输出，包括详细的清单信息和递归的仓库浏览。

该命令可以以人类可读格式或 JSON 格式（便于脚本处理）显示结果。递归模式（-r）会遍历子仓库。gcrane ls 是发现可用镜像、审计仓库内容和构建自动化脚本的重要工具。

# INSTALL

```zypper: sudo zypper install gcrane```

```nix: nix profile install nixpkgs#gcrane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcrane](/man/gcrane)(1), [crane-ls](/man/crane-ls)(1)
