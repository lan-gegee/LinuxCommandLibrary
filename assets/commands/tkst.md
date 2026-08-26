# TAGLINE

从命令行跟踪并预算 Claude Code 的 token 消耗

# TLDR

创建**带预算上限的任务**

```tkst -t "[Issue-243]" -b [5]```

启动**开启成本跟踪的 Claude Code**

```tkst claude```

**列出所有任务**及其当前支出

```tkst -l```

**更新**任务的预算或名称

```tkst -u "[Issue-243]" -b [10]```

**删除**任务

```tkst -d "[Issue-243]"```

在任务之间**重新分配支出**

```tkst -ra "[old-task]" "[new-task]"```

**开启或关闭**跟踪

```tkst --enable``` 或 ```tkst --disable```

# SYNOPSIS

**tkst** [_options_] [**claude** [_claude-args_]]

# DESCRIPTION

**tkst**（Tokenyst）是一个小型 CLI，它包装 **claude** 命令，并为每个任务持续记录 token 用量、折算的美元成本和预算消耗情况。会话期间的每次提示后，它会打印每轮增量以及相对当前预算的累计支出，让你可以在超出上限之前停止。任务是用户定义的桶——通常每个工单、功能或实验一个——其中保存着预算、已记录会话列表和汇总总额。

所有状态都存储在本地 **~/.tokenyst** 下，没有云同步。受支持的 Claude 各模型变体的定价随二进制文件一起打包，并应用于 **claude** CLI 报告的 token 计数。

# PARAMETERS

**claude** [_args_]
> 在跟踪状态下启动 Claude CLI。**claude** 之后的参数原样转发。

**-t** _name_, **--task** _name_
> 以给定名称创建新任务。

**-b** _amount_, **--budget** _amount_
> 设置任务的预算上限（美元），与 **-t** 或 **-u** 配合使用。

**-l**, **--list**
> 列出每个任务的预算、总支出和最近会话。

**-u** _name_, **--update** _name_
> 更新已有任务；配合 **-b** 更改预算或配合 **--rename** 更改名称。

**-d** _name_, **--delete** _name_
> 删除指定名称的任务。

**-a**, **--allocations**
> 显示按会话和按任务的支出分配。

**-ra** _from_ _to_, **--reallocate** _from_ _to_
> 将已记录的支出从一个任务转移到另一个任务（在会话被错误归属时很有用）。

**--enable**
> 在被禁用后重新启用跟踪。

**--disable**
> 暂停跟踪；**claude** 包装器仍会透传调用。

# CONFIGURATION

**~/.tokenyst/**
> 存放任务、会话日志和计算总额的本地数据目录。

**~/.tokenyst/config.json**
> 用户可调的设置，例如默认模型定价和货币。

# CAVEATS

成本数字依赖于**内置价格表**；如果 Anthropic 调整了定价，在二进制文件更新之前这些数值只是估算值。Token 计数读取自 **claude** CLI 的输出，因此该界面的变更可能干扰跟踪。状态保存在本地，不会在机器之间**同步**——如果想要共享预算，请配合版本控制或同步的主目录使用。

# HISTORY

**Tokenyst** 由 **jher7** 于 **2026 年**发布，是为了应对多智能体 Claude Code 工作流的激增——在此之前每次提示的支出直到月底账单才可见。它以全局安装的 **npm**/**pnpm** 包形式分发，并作为 **tkst** 调用。

# SEE ALSO

[claude](/man/claude)(1), [jq](/man/jq)(1), [npm](/man/npm)(1)
