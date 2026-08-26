# TLDR

列出**共享信息**

```sshare```

以**可解析格式**输出

```sshare --parsable```

以 **JSON 格式**输出

```sshare --json```

自定义**输出格式**

```sshare -o [format_string]```

显示**特定用户**的数据

```sshare -u [user1,user2]```

显示**特定账户**的数据

```sshare -A [account1,account2]```

显示**所有用户**

```sshare -a```

# SYNOPSIS

**sshare** [_OPTIONS_...]

# PARAMETERS

**-A, --accounts** _accounts_
> 显示指定账户（逗号分隔）的数据

**-a, --all**
> 显示所有用户的信息

**-u, --users** _users_
> 显示指定用户（逗号分隔）的数据

**-U, --Users**
> 只打印用户信息（不含祖先条目）

**-M, --clusters** _names_
> 面向特定集群

**-o, --format** _format_
> 自定义字段选择

**-l, --long**
> 含归一化数据的扩展输出

**-n, --noheader**
> 省略标题行

**-p, --parsable**
> 以竖线分隔且末尾带分隔符的输出

**-P, --parsable2**
> 以竖线分隔但末尾不带分隔符的输出

**--json**
> 以 JSON 输出

**--yaml**
> 以 YAML 输出

**-m, --partition**
> 显示分区名称

**-v, --verbose**
> 详细输出

**-V, --version**
> 打印版本

# OUTPUT FIELDS

**Account**: 关联账户
**User**: 用户名
**Raw Shares**: 分配的共享数
**Norm Shares**: 归一化共享数（0.0-1.0）
**Raw Usage**: 原始使用量
**Norm Usage**: 归一化使用量
**Effectv Usage**: 考虑层级结构后的有效使用量
**FairShare**: 用于调度的公平共享因子

# DESCRIPTION

**sshare** 显示 Slurm 优先级/多因子插件的公平共享信息。它展示账户和用户如何被分配共享额度、其实际使用量，以及影响作业调度优先级的公平共享因子。

这些数据要求 slurmdbd 已配置并可正常运行。公平共享调度根据用户和项目分配的共享额度及历史使用情况，确保资源在它们之间公平分配。

# CAVEATS

需要 slurmdbd 和多因子优先级插件。共享值是层级结构内的相对值。使用量数据按计费轮询间隔更新。历史使用量的衰减取决于 PriorityDecayHalfLife 配置。

# HISTORY

**sshare** 是 **Slurm** 的一部分，自 **2002 年**起由**劳伦斯利弗莫尔国家实验室**开发。加入公平共享调度是为了在多用户 HPC 环境中支持公平的资源分配。Slurm 目前由 **SchedMD** 维护。

# INSTALL

```apt: sudo apt install slurm-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sprio](/man/sprio)(1), [sacctmgr](/man/sacctmgr)(1), [sreport](/man/sreport)(1), [scontrol](/man/scontrol)(1)

# RESOURCES

```[Source code](https://github.com/SchedMD/slurm)```

```[Homepage](https://slurm.schedmd.com/)```

```[Documentation](https://slurm.schedmd.com/sshare.html)```

<!-- verified: 2026-06-10 -->
