# TAGLINE

修改进程的调度优先级

# TLDR

**设置运行中进程的绝对优先级**

```renice -n [3] -p [pid]```

**提高运行中进程的优先级**（需要 root）

```sudo renice -n [-4] -p [pid]```

**降低某用户所有进程的优先级**

```renice -n [4] -u [user]```

**设置进程组内所有进程的优先级**

```sudo renice -n [-5] -g [process_group]```

# SYNOPSIS

**renice** [**-n**] _priority_ [**-g**|**-p**|**-u**] _identifier_...

# PARAMETERS

**-n** _priority_
> 指定要设置的调度优先级。取值范围为 -20（最高）到 19（最低）。

**-p** _pid_
> 将参数解释为进程 ID（默认）。

**-u** _user_
> 将参数解释为用户名或 UID。

**-g** _pgrp_
> 将参数解释为进程组 ID。

# DESCRIPTION

**renice** 修改运行中进程的调度优先级（nice 值）。nice 值范围从 **-20**（最高优先级，对进程最有利）到 **19**（最低优先级，对进程最不利）。

普通用户只能提高自己进程的 nice 值（降低优先级）。超级用户可以降低 nice 值（提高优先级）并修改任何进程。

# CAVEATS

降低 nice 值（提高优先级）需要 root 权限。实际的调度效果取决于系统的调度器和负载。设置极端的优先级可能影响系统响应能力。

# HISTORY

**renice** 命令起源于 4.0BSD，此后一直是标准的 Unix 工具。它与 **nice** 命令互补，后者在启动新进程时设置优先级。

# INSTALL

```apt: sudo apt install bsdutils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nice](/man/nice)(1), [top](/man/top)(1), [ps](/man/ps)(1), [ionice](/man/ionice)(1)
