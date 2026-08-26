# TAGLINE

面向网络服务的快速并行模块化登录爆破工具

# TLDR

使用密码列表**暴力破解 SSH 登录**

```medusa -h [192.168.1.1] -u [admin] -P [passwords.txt] -M ssh```

从文件中**测试多个主机**

```medusa -H [hosts.txt] -u [admin] -P [passwords.txt] -M ssh```

使用用户名和密码列表进行**暴力破解**

```medusa -h [target] -U [users.txt] -P [passwords.txt] -M ftp```

**使用组合文件**（host:user:password 格式）

```medusa -C [combos.txt] -M ssh```

找到第一个有效凭据后即**停止**

```medusa -h [target] -u [admin] -P [passwords.txt] -M ssh -f```

**指定非默认端口**并增加线程数

```medusa -h [target] -n [2222] -u [root] -P [passwords.txt] -M ssh -t [20]```

**列出可用模块**

```medusa -d```

**测试空密码及用户名作为密码的情况**

```medusa -h [target] -u [admin] -P [passwords.txt] -M ssh -e ns```

# SYNOPSIS

**medusa** [-h _host_|-H _file_] [-u _user_|-U _file_] [-p _pass_|-P _file_] -M _module_ [_options_]

# PARAMETERS

**-h** _HOST_
> 目标主机名或 IP 地址

**-H** _FILE_
> 包含目标主机的文件

**-u** _USER_
> 要测试的用户名

**-U** _FILE_
> 包含用户名的文件

**-p** _PASS_
> 要测试的密码

**-P** _FILE_
> 包含密码的文件

**-C** _FILE_
> 组合文件（host:user:password 格式）

**-M** _MODULE_
> 认证模块（ssh、ftp、http、smb、telnet 等）

**-m** _PARAM_
> 模块特定的参数

**-n** _PORT_
> 非默认端口号

**-s**
> 启用 SSL

**-t** _NUM_
> 同时测试的登录总数。

**-T** _NUM_
> 同时测试的主机数

**-L**
> 对每个用户名并行执行登录尝试

**-f**
> 每台主机找到第一个有效凭据后停止

**-F**
> 整体找到第一个有效凭据后停止

**-e** _[n/s/ns]_
> 附加检查：n=空密码，s=密码等于用户名

**-g** _SECS_
> 尝试连接 NUM 秒后放弃（默认：3）。

**-r** _SECS_
> 重试之间休眠 NUM 秒（默认：3）。

**-R** _NUM_
> 放弃前尝试重试 NUM 次。

**-c** _USEC_
> 套接字测试期间等待的时间（微秒）。

**-O** _FILE_
> 将有效凭据日志追加到文件。

**-v** _NUM_
> 详细级别（0-6，默认：5）。

**-w** _NUM_
> 错误调试级别（0-10，默认：5）。

**-d**
> 列出所有可用模块。

**-q**
> 显示模块用法信息（与 -M 配合使用）。

**-b**
> 不显示启动横幅。

**-V**
> 显示版本。

**-Z** _MAP_
> 使用提供的映射恢复上次的扫描。

# DESCRIPTION

**medusa** 是一个面向网络服务的快速、并行、模块化登录爆破工具。它基于线程架构设计，可以对多个主机、用户或密码并发执行快速凭据测试。

每种服务都通过独立的模块（.mod 文件）支持，因此无需修改核心程序即可扩展工具。支持的协议包括 SSH、FTP、HTTP、IMAP、SMB、MySQL、PostgreSQL、Telnet、VNC 等众多协议。

Medusa 可以从文件、组合列表或命令行参数读取待测凭据。它支持 SSL 连接和自定义端口，并能将有效凭据保存到日志文件。其恢复功能允许中断的扫描从停止处继续。

# CAVEATS

暴力破解攻击会在目标系统上产生大量网络流量和日志记录。许多服务在多次失败尝试后会锁定账户。只能在你拥有所有权或已获得明确授权测试的系统上使用。某些模块可能需要特定参数才能正常运行。SSL 支持取决于具体模块。

# HISTORY

Medusa 由 **Joe Mondloch**（JoMo-Kun）开发，最初于 **2005 年**前后发布。其名称源自拥有多条蛇首的神话生物，象征该工具同时攻击多个目标的能力。它被设计为 Hydra 的替代品，专注于模块化和并行测试能力。该项目至今仍是网络安全评估和渗透测试中的常用工具。

# INSTALL

```apt: sudo apt install medusa```

```dnf: sudo dnf install medusa```

```pacman: sudo pacman -S medusa```

```brew: brew install medusa```

```nix: nix profile install nixpkgs#medusa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hydra](/man/hydra)(1), [ncrack](/man/ncrack)(1), [john](/man/john)(1), [hashcat](/man/hashcat)(1)
