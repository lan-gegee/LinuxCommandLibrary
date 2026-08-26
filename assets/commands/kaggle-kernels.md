# TAGLINE

从命令行管理 Kaggle Notebook

# TLDR

**列出 kernel**

```kaggle kernels list```

**将 kernel 推送到 Kaggle**

```kaggle kernels push -p [path]```

**从 Kaggle 拉取 kernel**

```kaggle kernels pull [owner/kernel-name]```

**获取 kernel 输出**

```kaggle kernels output [owner/kernel-name]```

**检查 kernel 状态**

```kaggle kernels status [owner/kernel-name]```

# SYNOPSIS

**kaggle** **kernels** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出可用的 kernel。

**push** **-p** _path_
> 将 kernel 推送到 Kaggle。

**pull** _kernel_
> 下载 kernel 文件。

**output** _kernel_
> 下载 kernel 输出。

**status** _kernel_
> 检查 kernel 运行状态。

**init** **-p** _path_
> 初始化 kernel 元数据。

# DESCRIPTION

**kaggle kernels** 用于在命令行管理 Kaggle notebook（kernel）。它是 Kaggle CLI 的一部分，可以对用于数据科学项目的计算 notebook 进行推送、拉取和监控。

# INSTALL

```nix: nix profile install nixpkgs#kaggle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kaggle](/man/kaggle)(1), [kaggle-datasets](/man/kaggle-datasets)(1)
