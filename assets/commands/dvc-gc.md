# TAGLINE

清理未使用的 DVC 缓存文件

# TLDR

**清理缓存但保留**工作区文件

```dvc gc -w```

**清理时保留所有**分支

```dvc gc -a```

**清理时保留所有**标签和分支

```dvc gc -a -T```

**试运行**（显示将被删除的内容）

```dvc gc -w --dry```

**强制清理**云端远程存储而不确认

```dvc gc -w -c -f```

**清理时保留最近 N 个**提交的数据

```dvc gc -n [5]```

# SYNOPSIS

**dvc gc** [_options_]

# PARAMETERS

**-w**, **--workspace**
> 保留当前工作区使用的文件。

**-a**, **--all-branches**
> 保留所有 Git 分支顶端使用的文件。

**-T**, **--all-tags**
> 保留所有 Git 标签使用的文件。

**-A**, **--all-commits**
> 保留所有 Git 提交使用的文件。

**--all-experiments**
> 保留所有实验使用的文件。

**-c**, **--cloud**
> 除本地缓存外，也对远程存储执行垃圾回收。

**-r** _NAME_, **--remote** _NAME_
> 指定要执行垃圾回收的远程存储。

**-n** _NUM_, **--num** _NUM_
> 保留最近 NUM 个提交的数据（默认：1）。

**--rev** _COMMIT_
> 保留指定 Git 提交的数据文件。

**--date** _YYYY-MM-DD_
> 保留指定日期之后各提交的缓存数据。

**--not-in-remote**
> 保留远程存储中不存在的数据。

**-f**, **--force**
> 跳过确认提示。

**-j** _NUM_, **--jobs** _NUM_
> 云端操作的并发任务数。

**--dry**
> 预览将要删除的内容而不实际执行。

**-p** _PATHS_, **--projects** _PATHS_
> 在共享缓存目录时包含指定的项目。

# DESCRIPTION

**dvc gc** 从 DVC 缓存中移除未使用的文件，释放磁盘空间。必须至少指定一个范围选项（**-w**、**-a**、**-T**、**-A**、**--all-experiments**、**-n**、**--rev** 或 **--date**），以定义要保留哪些数据。

缓存会积累所有被跟踪版本的文件。垃圾回收会识别并移除不再被任何指定提交、分支或标签引用的文件。

云选项（**-c**）将清理范围扩展到远程存储，移除指定范围之外不需要的文件。

# CAVEATS

不可逆操作——被删除的缓存文件必须重新下载或重新计算。为了协作方便可考虑保留所有分支。云端垃圾回收可能影响其他用户对数据的访问。必须提供范围选项；不带范围选项运行会产生错误。

# HISTORY

dvc gc 为 **DVC** 缓存实现垃圾回收，类似于 git gc 但针对版本化数据文件，为机器学习项目提供存储管理能力。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc](/man/dvc)(1), [dvc-init](/man/dvc-init)(1), [dvc-add](/man/dvc-add)(1), [git-gc](/man/git-gc)(1)
