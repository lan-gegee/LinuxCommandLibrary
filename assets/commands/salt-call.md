# TAGLINE

在 minion 本地运行 Salt 模块

# TLDR

**在本地应用状态**

```salt-call state.apply```

**运行指定状态**

```salt-call state.apply [apache]```

**执行模块函数**

```salt-call cmd.run 'uname -a'```

**以本地模式运行**

```salt-call --local grains.items```

**测试模式**（试运行，不做实际更改）

```salt-call state.apply test=True```

**以 JSON 格式显示输出**

```salt-call --output json grains.items```

**以 debug 日志级别运行**

```salt-call --log-level=debug state.apply```

# SYNOPSIS

**salt-call** [_options_] _function_ [_arguments_...]

# PARAMETERS

**--local**
> 不连接 Salt master 运行。使用本地 file client。

**--grains**
> 返回 minion 的 grain 数据。

**--pillar** _data_
> 以字典形式设置 pillar 数据（如 '{"key": "value"}'）。

**--output** _format_
> 输出格式：json、yaml、nested、raw、highstate、quiet 等。

**--state-output** _mode_
> 状态输出的详细程度：full、terse、mixed、changes。

**--log-level** _level_
> 日志级别：all、garbage、trace、debug、info、warning、error、critical、quiet。

**--id** _MINION_ID_
> 指定 minion ID（覆盖已配置的 minion ID）。

**--retcode-passthrough**
> 以 Salt 命令的返回码退出，便于脚本化使用。

**--no-color**
> 禁用彩色输出。

# DESCRIPTION

**salt-call** 直接在 minion 上运行 Salt 执行模块和状态，而不经过 Salt master。这适用于测试、调试以及无 master 的 Salt 配置——此时 minion 独立应用状态。

配合 **--local** 使用时，它完全独立于 master 运行，非常适合独立的配置管理，或在将状态部署到整个基础设施之前先进行测试。

# INSTALL

```apk: sudo apk add salt-lts-minion```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[salt](/man/salt)(1), [salt-run](/man/salt-run)(1), [salt-master](/man/salt-master)(1), [salt-minion](/man/salt-minion)(1), [salt-key](/man/salt-key)(1)
