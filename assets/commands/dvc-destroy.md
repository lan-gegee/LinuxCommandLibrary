# TAGLINE

从项目中移除 DVC 初始化

# TLDR

**从项目中移除 DVC**

```dvc destroy```

**强制销毁而不确认**

```dvc destroy -f```

# SYNOPSIS

**dvc** **destroy** [_options_]

# PARAMETERS

**-f**, **--force**
> 强制销毁而不进行确认。

# DESCRIPTION

**dvc destroy** 从项目中完全移除 DVC 初始化，相当于从仓库中卸载 DVC。它会删除 .dvc 目录（包含缓存、配置和内部状态），以及整个项目中所有的 .dvc 元数据文件。

需要注意的是，DVC 跟踪的实际数据文件会被保留下来。被移除的只是 DVC 的跟踪基础设施。这意味着你的大型数据集和模型文件仍留在工作区中，只是不再具有版本控制状态。

该命令不可逆，应谨慎使用。在销毁之前，如果之后可能需要恢复 DVC 跟踪，请确保已将重要数据推送到远程存储。销毁后，DVC 添加到 .gitignore 中的条目仍然存在，可能需要手动清理。

# CAVEATS

此操作不可逆。销毁前请务必备份数据或推送到远程存储。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc-init](/man/dvc-init)(1), [dvc](/man/dvc)(1)

# RESOURCES

```[Source code](https://github.com/iterative/dvc)```

```[Homepage](https://dvc.org/)```

```[Documentation](https://dvc.org/doc/command-reference/destroy)```

<!-- verified: 2026-07-14 -->
