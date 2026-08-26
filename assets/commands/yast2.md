# TAGLINE

SUSE 系统配置工具

# TLDR

**启动 YaST 图形界面**

```sudo yast2```

**启动 YaST 文本界面**

```sudo yast2 --ncurses```

**打开特定模块**

```sudo yast2 [sw_single]```

**列出可用模块**

```yast2 --list```

**安装软件包**

```sudo yast2 --install [package_name]```

**移除软件包**

```sudo yast2 --remove [package_name]```

**配置网络**

```sudo yast2 lan```

# SYNOPSIS

**yast2** [_options_] [_module_] [_module-options_]

# PARAMETERS

**--ncurses**
> 强制使用文本界面。

**--qt**
> 强制使用 Qt 图形界面。

**--gtk**
> 强制使用 GTK 图形界面。

**--list**
> 列出可用模块。

**--install** _pkg_
> 安装软件包。

**--remove** _pkg_
> 移除软件包。

**--update** _pkg_
> 更新软件包。

**--help**
> 显示帮助。

# COMMON MODULES

**sw_single**：软件管理。

**lan**：网络配置。

**users**：用户管理。

**firewall**：防火墙配置。

**disk**：磁盘分区工具。

**bootloader**：引导加载程序配置。

**printer**：打印机设置。

**sound**：声卡配置。

# DESCRIPTION

**yast2**（Yet another Setup Tool 2）是 openSUSE 和 SUSE Linux Enterprise 的综合系统配置工具。它提供图形和文本两种管理界面。

YaST 可以配置硬件、网络、安全、软件包、系统服务和用户。各个模块负责特定任务，可以从控制中心访问，也可以直接通过命令行调用。

该工具支持 AutoYaST，可通过 XML 控制文件进行自动化安装，从而实现多系统的无人值守部署。

# CAVEATS

仅适用于 SUSE；其他发行版不可用。部分模块需要 root 权限。在较新的 SUSE 版本中正被 Cockpit 和 Agama 取代。

# HISTORY

**YaST** 于 1995 年 4 月随 SuSE Linux 首次发布。YaST2 出现在 SuSE 6.3（1999 年）中作为安装器，并在 6.4 中成为完整的系统工具。它于 2004 年以 GPL 许可证开源。在 openSUSE Leap 16 和 SLES 16 上，YaST 正被基于 Web 的工具取代。

# INSTALL

```zypper: sudo zypper install yast2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zypper](/man/zypper)(8), [systemctl](/man/systemctl)(1)
