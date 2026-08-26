# TAGLINE

探索和限制 Linux 能力（capabilities）

# TLDR

**显示当前能力状态**

```capsh --print```

**说明某项能力的作用**

```capsh --explain=[cap_net_admin]```

**解码能力的十六进制值**

```capsh --decode=[0x20]```

**丢弃所有能力并运行 Shell**

```capsh --drop=all -- -c "[command]"```

**以指定能力运行命令**

```capsh --caps="[cap_net_raw+ep]" -- -c "[command]"```

**检查系统是否支持某项能力**

```capsh --supports=[cap_sys_admin]```

**chroot 后运行命令**

```capsh --chroot=[/path] -- -c "[command]"```

# SYNOPSIS

**capsh** [_options_]

# DESCRIPTION

**capsh** 是一个能力 shell 包装器，用于探索和约束 Linux 能力支持。它为 Linux 进程能力提供测试、调试和环境创建功能。属于 libcap 软件包。

# PARAMETERS

**--print**
> 显示当前生效的能力及相关状态

**--current**
> 显示包含 1e 能力和 IAB 向量的能力状态

**--explain**=_cap_xxx_
> 描述某项能力提供的特权

**--decode**=_N_
> 解码十六进制能力向量（如 /proc/1/status 中的）

**--supports**=_cap_xxx_
> 验证系统上是否存在该能力

**--drop**=_cap_xxx_
> 从边界集中移除某项能力

**--caps**=_cap-set_
> 将能力设置为指定的文本值

**--inh**=_cap-set_
> 设置可继承能力

**--chroot**=_path_
> 更改根目录（需要 CAP_SYS_CHROOT）

**--uid**=_id_
> 设置真实与有效用户 ID

**--gid**=_id_
> 设置真实与有效组 ID

**--**
> 用后续参数执行 /bin/bash

# EXIT STATUS

成功返回 0，出错返回 1。

# CAVEATS

许多操作需要具备特定能力才能执行。要有效使用本工具，必须理解 Linux 能力机制。

# INSTALL

```apt: sudo apt install libcap2-bin```

```apk: sudo apk add libcap-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getcap](/man/getcap)(8), [setcap](/man/setcap)(8), [capabilities](/man/capabilities)(7)
