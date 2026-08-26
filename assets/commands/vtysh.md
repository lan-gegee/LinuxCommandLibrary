# TAGLINE

FRRouting 守护进程的集成 Shell

# TLDR

**启动交互式 Shell**

```sudo vtysh```

**执行单条命令**

```sudo vtysh -c "[show ip route]"```

**执行命令并将其回显**（用于脚本）

```sudo vtysh -E -c "[show ip route]"```

仅**连接到指定守护进程**

```sudo vtysh -d [bgpd]```

**执行开机启动配置**

```sudo vtysh -b```

**显示运行配置**

```sudo vtysh -c "show running-config"```

# SYNOPSIS

**vtysh** [**-b**] [**-c** _command_] [**-d** _daemon_] [**-E**] [**-h**]

# PARAMETERS

**-b**, **--boot**
> 执行集成配置文件中的开机启动配置。

**-c** _command_, **--command** _command_
> 执行指定命令后退出。可多次使用以执行多条命令。

**-d** _daemon_, **--daemon** _daemon_
> 仅连接到指定守护进程（zebra、bgpd、ospfd、ripd、isisd 等）。

**-E**, **--echo**
> 在显示结果之前先回显命令和提示符。便于脚本使用。

**-C**, **--dryrun**
> 检查配置文件的语法有效性，但不应用。

**-n**, **--noerror**
> 忽略错误对返回码的影响（在脚本中很有用）。

**-u**, **--user**
> 限制为非特权模式，不允许执行配置命令。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**vtysh** 是 FRRouting（FRR）和 Quagga 路由软件的集成命令 Shell。它提供统一的类 Cisco IOS CLI，可以从单一接口配置和监控所有路由守护进程（Zebra、BGP、OSPF、RIP、IS-IS 等）。

该 Shell 以分层模式工作：用于基本命令的用户 EXEC 模式、用于管理命令的特权 EXEC 模式（通过 **enable** 进入），以及用于修改配置的配置模式（通过 **configure terminal** 进入）。每种路由协议都有自己的配置子模式。

vtysh 通过控制套接字连接到所有正在运行的路由守护进程，呈现它们合并后的功能。诸如 **show ip route**、**show bgp summary** 和 **show running-config** 之类的命令会聚合来自所有相关守护进程的信息。

配置可以用 **write memory** 保存到集成配置文件（/etc/frr/frr.conf）或各守护进程的独立配置中。

# CAVEATS

需要 root 权限或属于 frr/quagga 组才能访问守护进程控制套接字。必须启用集成配置文件才能使用统一配置。尽管语法相似，某些命令的行为可能与 Cisco IOS 不同。交互模式下提供 Tab 补全和上下文相关帮助（?）。

# HISTORY

**vtysh** 作为 **Quagga** 路由套件的一部分开发而来，Quagga 于 **2003 年**从 GNU Zebra 分叉出来。当 Quagga 开发停滞时，**FRRouting** 项目于 **2017 年**将其分叉并继续积极开发。vtysh 至今仍是 FRR 的主要 CLI，为习惯商用路由器操作系统的网络工程师提供了熟悉的界面。

# INSTALL

```apt: sudo apt install frr```

```dnf: sudo dnf install frr```

```apk: sudo apk add quagga```

```zypper: sudo zypper install frr```

```nix: nix profile install nixpkgs#frr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zebra](/man/zebra)(8), [bgpd](/man/bgpd)(8), [ospfd](/man/ospfd)(8), [ripd](/man/ripd)(8)
