# TAGLINE

文件完整性检查与主机入侵检测

# TLDR

**初始化文件完整性数据库**

```samhain -t init```

**对照基线数据库检查文件**

```samhain -t check```

**以守护进程方式运行**，进行持续监控

```samhain -D```

**检查配置文件语法**

```samhain -t check --verify-config```

**用当前文件状态更新数据库**

```samhain -t update```

在前台运行并输出**详细信息**

```samhain -t check --foreground -p info```

# SYNOPSIS

**samhain** [_-t init|check|update_] [_-D_] [_-p priority_] [_--foreground_] [_-c configfile_]

# PARAMETERS

**-t** _action_
> 指定操作：init（创建基线）、check（对照基线校验）、update（刷新数据库）

**-D**
> 以守护进程方式运行

**--foreground**
> 在前台运行，不 fork

**-c** _file_
> 使用替代的配置文件（默认：/etc/samhainrc）

**-p** _priority_
> 设置日志优先级：debug、info、notice、warn、err、crit

**--verify-config**
> 检查配置文件语法后退出

**-l** _file_
> 指定日志文件路径

**-e** _file_
> 指定数据库文件路径

# DESCRIPTION

**Samhain** 是一款基于主机的入侵检测系统（HIDS），提供文件完整性监控、日志文件分析和 rootkit 检测。它跟踪关键系统文件的校验和、权限、时间戳和属性，以检测未授权的修改。

该系统有三种运行模式：**init** 创建基线数据库，**check** 将当前文件状态与基线比较，**update** 刷新数据库。Samhain 能够发现隐藏进程、可疑的 SUID 可执行文件以及内核级的入侵。

对于多主机环境，Samhain 采用客户端-服务器架构，由 **yule** 充当中央日志服务器和配置主机。配置存储在 **/etc/samhainrc**。

# CONFIGURATION

**/etc/samhainrc**
> 主配置文件，定义受监控的目录、要检查的文件属性、日志目标和严重级别。

**/var/lib/samhain/samhain_file**
> 文件完整性基线数据库的默认位置。

# CAVEATS

基线数据库应基于已知干净的系统状态创建并妥善保存（最好存放在只读介质上）。使用隐身选项编译时，帮助文件和 man page 可能不可用，以向攻击者隐藏 HIDS 的存在。

# HISTORY

Samhain 由 **Rainer Wichmann** 开发，首次发布于 **1999 年**。其名称源自标志着收获季结束的凯尔特节日。它从一个简单的文件完整性检查器发展为功能全面的 HIDS，支持跨异构环境的集中监控。

# INSTALL

```apt: sudo apt install samhain```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aide](/man/aide)(1), [tripwire](/man/tripwire)(8), [rkhunter](/man/rkhunter)(1), [chkrootkit](/man/chkrootkit)(1)
