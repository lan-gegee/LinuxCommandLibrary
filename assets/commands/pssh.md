# TAGLINE

在多台主机上并行运行命令

# TLDR

**在多台主机上运行命令**

```pssh -h [hosts.txt] -i "[uptime]"```

**以内联方式指定主机**

```pssh -H "[user@host1] [user@host2]" -i "[command]"```

**限制并行数**

```pssh -h [hosts.txt] -p [10] -i "[command]"```

**设置超时**

```pssh -h [hosts.txt] -t [30] -i "[command]"```

**复制文件到主机**

```pscp -h [hosts.txt] [local_file] [/remote/path]```

**从主机复制文件**

```pslurp -h [hosts.txt] [/remote/file] [local_dir]```

**交互式运行**

```pssh -h [hosts.txt] -i -A "[sudo command]"```

# SYNOPSIS

**pssh** [_-h hostfile_] [_-H hosts_] [_-p parallel_] [_-t timeout_] [_-i_] [_options_] _command_

# PARAMETERS

**-h** _FILE_
> 主机列表文件（每行一个主机）。

**-H** _HOSTS_
> 以空格分隔的主机。

**-l** _USER_
> 默认用户名。

**-p** _NUM_
> 最大并行连接数。

**-t** _SECONDS_
> 每台主机的超时时间。

**-i**, **--inline**
> 内联显示输出。

**-o** _DIR_
> 输出目录。

**-e** _DIR_
> 错误输出目录。

**-A**
> 提示输入密码。

**-O** _OPTS_
> SSH 选项。

**-x** _ARGS_
> 额外的 SSH 参数。

**-v**
> 详细模式。

# DESCRIPTION

**pssh**（Parallel SSH）可在多台主机上同时运行命令。它将 SSH 连接并行化，在大规模服务器集群上实现更快的执行速度。

主机文件列出目标机器，每行一个。格式支持 user@host:port 语法。以 # 开头的行为注释。

并行数限制控制并发连接数量。过多的同时连接可能压垮网络或主机，建议从保守值开始。

不同输出模式的收集方式不同。内联模式（-i）随输出到达即时显示；目录模式（-o）为每台主机保存单独的输出文件。

相关工具包括：并行向主机复制文件的 pscp、并行取回文件的 pslurp，以及并行 rsync 的 prsync。

超时可避免在无响应的主机上挂起。失败的主机会与成功的主机分开报告。

# CAVEATS

非交互使用需要 SSH 密钥认证。密码提示（-A）是交互式的。过大的并行数可能引发问题。主机名必须可解析。

# HISTORY

**pssh** 由 Intel Research 的 **Brent N. Chun** 于 **2007 年**前后创建。它满足了集群和云环境中高效执行多主机命令的需求。

# INSTALL

```dnf: sudo dnf install pssh```

```apk: sudo apk add pssh```

```zypper: sudo zypper install pssh```

```brew: brew install pssh```

```nix: nix profile install nixpkgs#pssh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [pdsh](/man/pdsh)(1), [ansible](/man/ansible)(1), [clusterssh](/man/clusterssh)(1)
