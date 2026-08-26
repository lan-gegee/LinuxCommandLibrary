# TAGLINE

在 master 上执行 Salt runner 模块

# TLDR

**列出已连接的 minion**

```salt-run manage.up```

**列出已断开的 minion**

```salt-run manage.down```

**运行编排任务**

```salt-run state.orchestrate [orch.deploy]```

**查看作业状态**

```salt-run jobs.lookup_jid [job_id]```

**检查 minion 版本**

```salt-run manage.versions```

# SYNOPSIS

**salt-run** [_options_] _function_ [_arguments_...]

# PARAMETERS

**manage.up**
> 列出在线的 minion。

**manage.down**
> 列出离线的 minion。

**state.orchestrate** _sls_
> 运行编排状态。

**jobs.list_jobs**
> 列出最近的作业。

**jobs.lookup_jid** _jid_
> 按 JID 获取之前运行的作业结果。

**jobs.active**
> 显示当前在所有 minion 上运行的作业。

**--out**, **--output** _format_
> 输出格式（json、yaml、highstate 等）。

**-c** _DIR_, **--config-dir** _DIR_
> 使用自定义的 Salt master 配置目录。

# DESCRIPTION

**salt-run** 在 Salt master 上执行 runner 模块。Runner 负责 master 侧的操作，如编排、作业管理和集群级任务。属于 SaltStack 配置管理的一部分。

# INSTALL

```apk: sudo apk add salt-lts-master```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[salt](/man/salt)(1), [salt-call](/man/salt-call)(1)
