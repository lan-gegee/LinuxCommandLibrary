# TAGLINE

带交互式 CLI 的并行 SSH 作业管理器

# TLDR

**在多台主机上运行命令**

```ssh-para -H [host1] [host2] [host3] -- echo connection ok```

**以 20 个并行作业进行大规模修补**

```ssh-para -p 20 -f [hostlist.txt] -- 'sudo yum update -y'```

**在远程主机上执行本地脚本**

```ssh-para -p 20 -f [hosts.txt] -s [./myscript] -a status```

# SYNOPSIS

**ssh-para** [**-p** _parallelism_] [**-H** _hosts_... | **-f** _hostfile_] **--** _command_

# PARAMETERS

**-p** _N_
> 并行 SSH 连接数量。

**-H** _HOSTS_
> 以空格分隔的目标主机列表。

**-f** _FILE_
> 包含目标主机名的文件，每行一个。

**-s** _SCRIPT_
> 要在远程主机上执行的本地脚本。

**-a** _ARGS_
> 传递给脚本的参数。

# DESCRIPTION

**ssh-para** 可以同时在多台远程服务器上执行命令和脚本，并提供交互式的实时输出监控。它支持暂停、恢复和中止作业、终止卡住的连接、可配置的并行度以及日志生成。需要基于 SSH 密钥的认证。

# HISTORY

**ssh-para** 由 **joknarf** 创建，使用 **Python** 编写。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add dropbear-ssh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pssh](/man/pssh)(1), [pdsh](/man/pdsh)(1), [sake](/man/sake)(1)
