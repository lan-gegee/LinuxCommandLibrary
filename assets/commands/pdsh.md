# TAGLINE

并行分布式 Shell——一次在多台主机上运行命令

# TLDR

**在一列主机上运行命令**

```pdsh -w [host1,host2,host3] [command]```

**使用主机范围**（压缩的数字区间）

```pdsh -w [host[1-10]] [command]```

**强制使用 SSH** 远程命令模块

```pdsh -R ssh -w [hosts] [command]```

**从文件读取目标主机**

```pdsh -w ^[hosts.txt] [command]```

**限制扇出数**（并发连接）

```pdsh -f [16] -w [hosts] [command]```

**将输出通过 dshbak 管道处理**，按主机分组结果

```pdsh -w [hosts] [command] | dshbak -c```

# SYNOPSIS

**pdsh** [_options_] [_command_]

# PARAMETERS

**-w** _HOSTS_
> 目标主机列表。接受逗号分隔的主机名、压缩范围（host[1-10]），或用 `^file` 从文件读取。

**-x** _HOSTS_
> 从目标列表中排除这些主机。

**-R** _MODULE_
> 远程命令模块：`ssh`、`rsh`、`mrsh`、`exec`、`krb4` 等。默认值取决于编译配置。

**-l** _USER_
> 登录远程主机所用的用户名。

**-t** _SECONDS_
> 每台主机的连接超时时间。默认：10。

**-u** _SECONDS_
> 每台主机的命令超时时间（会终止过慢的命令）。

**-f** _NUMBER_
> 并发（扇出）连接的最大数量。默认：32。

**-N**
> 不显示输出中每一行的 "hostname:" 前缀。

**-S**
> 以最大的远程退出状态作为 pdsh 的退出码返回。

**-g** _GROUP_
> 在 dshgroup 或 genders 中定义的主机组上运行。

**-a**
> 面向所有主机（需要可用的主机模块，如 genders 或 machines）。

**-q**
> 显示目标主机列表后退出，不执行命令。

# DESCRIPTION

**pdsh** 是一个高性能的并行远程 Shell 工具。它在多台主机上并行启动指定的命令，并把各主机的 stdout/stderr 合并回传给用户，每行前面带有对应主机的名称。

它由 LLNL 为集群管理而开发，支持多种"远程命令模块"（ssh、rsh、mrsh 等），可在编译时选定或通过 **-R** 指定。目标主机可以显式列表、压缩数字区间、文件、dshgroup 或 genders/SLURM 模块的形式给出。

配套工具 **pdcp**（并行复制）、**rpdcp**（反向并行复制）和 **dshbak**（把各主机的相同输出归组）共同组成一套面向脚本化集群操作的小型工具集。

# CAVEATS

要求所选的远程 Shell（通常是基于密钥认证的 SSH）能在每台目标主机上非交互地工作。来自多台主机的输出会交错在一起——可用管道交给 **dshbak** 归组。由于两端的 Shell 都会解释命令字符串，引号处理可能比较棘手。

# HISTORY

**pdsh** 起源于 **劳伦斯利弗莫尔国家实验室**，诞生于 20 世纪 90 年代末，作为 IBM DSH 的后继者用于管理大型 Linux 集群。它目前托管在 GitHub 上，仍在 HPC 管理领域广泛使用。

# INSTALL

```apt: sudo apt install pdsh```

```dnf: sudo dnf install pdsh```

```apk: sudo apk add pdsh```

```zypper: sudo zypper install pdsh```

```brew: brew install pdsh```

```nix: nix profile install nixpkgs#pdsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [pssh](/man/pssh)(1), [ansible](/man/ansible)(1), [rsync](/man/rsync)(1)
