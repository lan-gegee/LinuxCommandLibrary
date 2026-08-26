# TAGLINE

FreePBX 管理的命令行界面

# TLDR

**重新加载** FreePBX 配置

```fwconsole reload```

**启动** Asterisk 及 FreePBX 所需的其他服务

```fwconsole start```

**停止** Asterisk 及 FreePBX 所需的其他服务

```fwconsole stop```

查看并**更新设置**

```fwconsole setting [keyword] [new_value]```

列出可用的**备份**

```fwconsole backup --list```

列出可用的 **FreePBX 命令**

```fwconsole list```

把所有 FreePBX 文件的**所有者**更改为 apache 用户

```fwconsole chown```

# SYNOPSIS

**fwconsole** _command_ [_options_]

# PARAMETERS

**reload**
> 应用配置更改而无需重启 Asterisk

**start** [_module_]
> 启动 FreePBX 和 Asterisk 服务（可选仅针对单个模块）

**stop** [_module_]
> 停止 FreePBX 和 Asterisk 服务

**restart**
> 重启 FreePBX 和 Asterisk 服务

**setting** _keyword_ [_value_]
> 查看或修改 FreePBX 设置

**backup** [**--list** | **--file** _file_]
> 管理或恢复 FreePBX 备份

**chown**
> 修复文件所有权以保证 Web 服务器访问

**ma**（module admin）
> 安装、启用、禁用、升级或移除 FreePBX 模块

**sysadmin**
> 系统管理任务

**list**
> 显示所有可用的 fwconsole 命令

**-h**, **--help**
> 显示指定命令的帮助

**-v**, **-vv**, **-vvv**
> 提高输出详细程度

**-q**, **--quiet**
> 抑制输出

# DESCRIPTION

**fwconsole** 是管理 FreePBX 的命令行界面。FreePBX 是一个基于 Web 的开源图形界面，用于管理 Asterisk PBX 系统。它提供对 FreePBX 配置、模块以及底层 Asterisk 服务器的管理控制。

该工具负责配置重载、服务管理、模块管理、备份和系统维护任务。它对 FreePBX 安装的自动化、脚本编写和故障排查至关重要。

通过 Web 界面做出的配置更改通常需要执行 **fwconsole reload** 才能应用到运行中的 Asterisk 实例。

# CAVEATS

大多数命令需要 root 权限或相应的 sudo 权限。在有通话进行时执行 reload 可能导致短暂的服务中断。手动修改文件后需要执行 chown 命令，以保持 Web 服务器正确的访问权限。

# HISTORY

fwconsole 属于 FreePBX，后者始于 **2004 年**，最初是 Asterisk 的一个 Web 图形界面。它原名 AMP（Asterisk Management Portal），2006 年更名为 FreePBX。fwconsole 命令行工具是 FreePBX 现代化进程的一部分。

# SEE ALSO

[asterisk](/man/asterisk)(8), [fs_cli](/man/fs_cli)(1)
