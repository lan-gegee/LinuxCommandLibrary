# TAGLINE

Slurm REST API 接口守护进程

# TLDR

在**端口**上启动 REST API

```slurmrestd [host]:port```

在 **Unix 套接字**上启动

```slurmrestd unix:/path/to/socket```

处理请求前更改**组 ID**

```slurmrestd -g [group_id] [host]:port```

指定**身份验证插件**

```slurmrestd -a [auth_plugins] [host]:port```

从**文件**读取配置

```slurmrestd -f [path/to/slurm.conf]```

处理前更改**用户 ID**

```slurmrestd -u [user_id] [host]:port```

**生成** OpenAPI 规范

```slurmrestd --generate-openapi-spec```

# SYNOPSIS

**slurmrestd** [_OPTIONS_]... <[_host_]:_port_|unix:/_path/to/socket_>...

# PARAMETERS

**-a** _plugin[,plugin]_
> 要加载的身份验证插件列表，以逗号分隔

**-d** _plugin[,plugin]_
> 用于输出格式的数据解析插件

**-s** _plugin[,plugin]_
> 决定可用端点的 OpenAPI 插件

**-f** _file_
> 从指定文件读取 Slurm 配置

**-g** _group_id_
> 更改组 ID 并放弃附加组

**-u** _user_id_
> 处理请求前更改用户 ID

**-t** _count_
> 处理线程数

**--max-connections** _count_
> 最大并发连接数（默认：124）

**--generate-openapi-spec**
> 输出 JSON 格式的 OpenAPI schema 并退出

**--yaml-compact**
> 以紧凑格式输出 YAML

**--yaml-pretty**
> 以易读的美化格式输出 YAML

**--disable-user-check**
> 禁用"slurmrestd 不得以 root 或 SlurmUser 运行"的检查

**-v**
> 详细模式（多个 v 最多可达 6 级，如 -vvvvvv）

**-V**
> 打印版本信息

**-h**
> 显示帮助

# DESCRIPTION

**slurmrestd** 为 Slurm 工作负载管理器提供 REST API 接口。它有两种运行模式：用于通过 inetd、xinetd 或 systemd socket activation 进行管道输入的 **Inetd 模式**，以及在指定地址上打开套接字的**监听模式**。

该守护进程支持通过本地 UNIX 套接字凭据或 JWT token 进行身份验证。可以指定多个监听端点，包括 TCP 端口和 Unix 套接字。在地址前加 **https://** 即可启用 TLS 加密。

# CAVEATS

需要正确的 Slurm 配置和身份验证设置。JWT 身份验证需要正确的密钥配置。建议先以提升的权限启动再降权到非特权用户。API 端点随加载的插件和 Slurm 版本而异。

# HISTORY

**slurmrestd** 于 **20.02** 版本（**2020 年**发布）加入 Slurm，旨在为程序化的集群交互提供现代 REST API 访问能力。它支持与 Web 界面、监控系统及自动化工具集成。由 **SchedMD** 维护，属于 Slurm 核心发行版的一部分。其 man 手册节号为 8（系统管理）。

# INSTALL

```apt: sudo apt install slurmrestd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[slurmctld](/man/slurmctld)(8), [sbatch](/man/sbatch)(1), [squeue](/man/squeue)(1), [sacct](/man/sacct)(1)
