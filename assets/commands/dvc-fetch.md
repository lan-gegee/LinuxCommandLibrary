# TAGLINE

将被跟踪的文件下载到本地缓存

# TLDR

**获取所有被跟踪的数据**

```dvc fetch```

**获取特定文件**

```dvc fetch [data.csv.dvc]```

**从特定远程存储获取**

```dvc fetch -r [remote_name]```

**获取所有修订版本**

```dvc fetch --all-commits```

**使用多个任务并行获取**

```dvc fetch -j [4]```

# SYNOPSIS

**dvc** **fetch** [_options_] [_targets_...]

# PARAMETERS

**-r**, **--remote** _name_
> 远程存储名称。

**-j**, **--jobs** _number_
> 并行下载任务数。

**--all-commits**
> 为所有 Git 提交获取数据。

**--all-branches**
> 为所有分支获取数据。

**--all-tags**
> 为所有标签获取数据。

**-R**, **--recursive**
> 递归地获取。

**--run-cache**
> 获取 DVC 流水线阶段的运行历史。

**-v**, **--verbose**
> 增加输出的详细程度。

**-q**, **--quiet**
> 抑制输出。

# DESCRIPTION

**dvc fetch** 从远程存储下载 DVC 跟踪的数据到本地 DVC 缓存，而不影响工作区。这适用于预先准备数据以供后续使用，而不立即填充工作目录。

这种两阶段流程（先 fetch 再 checkout）让你可以控制磁盘空间和时机。fetch 将数据带入缓存（通常是 .dvc/cache），并以去重的方式高效存储。之后当你真正需要这些文件时，再由 dvc checkout 从缓存创建链接或副本到工作区。

这种分离在 CI/CD 流水线或切换分支时尤其有价值：你可以预先获取所有必要的数据，然后在需要时快速检出不同的版本，而无需重复下载。--all-commits、--all-branches 和 --all-tags 选项有助于批量预取多个修订版本的数据。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc](/man/dvc)(1), [dvc-checkout](/man/dvc-checkout)(1), [dvc-gc](/man/dvc-gc)(1), [dvc-add](/man/dvc-add)(1)
