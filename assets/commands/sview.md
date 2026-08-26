# TAGLINE

图形化的 Slurm 集群状态查看器

# TLDR

启动 **Slurm 图形界面**

```sview```

# SYNOPSIS

**sview**

# DESCRIPTION

**sview** 是一个用于查看和修改 Slurm 集群状态的图形用户界面。它通过基于 GTK 的交互式界面，以可视化方式访问作业、节点、分区和配置信息。

界面使用标签页在作业和分区视图之间切换，并可选显示关联资源的节点图。用户可以通过点击界面元素自定义列显示、排序方式以及展开作业步骤。

# FEATURES

- 以图形方式查看作业、分区和节点
- 对集群数据排序和过滤
- 展开作业详情查看各个步骤
- 通过右键菜单自定义可见字段
- 节点图可视化
- 管理模式用于授权修改（root）

# ADMIN MODE

root 用户可以启用管理模式来修改节点状态、作业时间限制等字段，并触发 Slurm 重新配置。文档建议完成修改后立即关闭管理模式。

# CAVEATS

需要 GTK+-2.0 库。某些 GTK 主题在显示大量条目时会出现问题。远程访问需要 X11 转发。管理模式下的修改立即生效。

# ENVIRONMENT

**SLURM_CONF**
> Slurm 配置文件的路径

# HISTORY

**sview** 是 **Slurm** 的组成部分。Slurm 由 **劳伦斯利弗莫尔国家实验室** 自 **2002 年**开始开发。这款 GUI 工具为监控集群状态提供了命令行工具之外的易用选择。Slurm 目前由 **SchedMD** 维护。

# INSTALL

```apt: sudo apt install sview```

```nix: nix profile install nixpkgs#sview```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[squeue](/man/squeue)(1), [sinfo](/man/sinfo)(1), [scontrol](/man/scontrol)(1), [sacct](/man/sacct)(1), [sbatch](/man/sbatch)(1)
