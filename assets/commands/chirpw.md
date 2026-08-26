# TAGLINE

业余无线电编程工具

# TLDR

**启动 CHIRP 无线电编程软件**

```chirpw```

**使用指定的电台驱动启动**

```chirpw --onlydriver [driver_name]```

**以下载动作启动**

```chirpw --action download```

**恢复上次会话的标签页**

```chirpw --restore```

**以详细输出运行**

```chirpw -v```

**显示版本信息**

```chirpw --version```

# SYNOPSIS

**chirpw** [**--module** _module_] [**--onlydriver** _driver_] [**--action** _action_] [**--restore**] [**--page** _page_] [**--force-language** _code_] [**-q**|**-v**] [**--log** _file_] [**--log-level** _level_]

# DESCRIPTION

**chirpw** 是 CHIRP 的图形界面。CHIRP 是一款免费开源的工具，用于对业余（ham）无线电台收发信机进行编程。它允许用户管理电台的存储信道、配置设置，并通过串口或 USB 连接在计算机与电台之间传输数据。

CHIRP 支持来自 Baofeng、Yaesu、Kenwood、Icom 等厂商的数百种电台型号。该软件可以导入/导出多种文件格式，并可查询在线中继台数据库。

# PARAMETERS

**--module** _module_
> 启动时加载指定模块。

**--onlydriver** _driver_
> 仅加载指定的电台驱动。

**--action** _action_
> 立即启动 UI 动作：upload、download、query_rr、query_mg、query_rb、query_dm、new。

**--restore**
> 恢复上次会话的标签页。

**--profile**
> 启用性能分析。

**--inspect**
> 显示 wxPython 检查器。

**--page** _PAGE_
> 启动时选中默认编辑器的此页面。

**--force-language** _CODE_
> 强制使用指定的 ISO 语言代码作为 locale。

**-q**
> 安静模式（较少输出）。

**-v**
> 详细模式（较多输出）。

**--log** _file_
> 将日志写入指定文件。

**--log-level** _level_
> 设置日志详细级别（critical、error、warn、info、debug）。默认：debug。

**--version**
> 输出版本并退出。

# CAVEATS

访问串口需要相应权限。将你的用户加入串口组：
```
sudo usermod -a -G $(stat -c %G /dev/ttyUSB0) $USER
```
更改组后需注销并重新登录。

在 Linux 系统上，电台端口通常为 **/dev/ttyUSB0**。

# HISTORY

**CHIRP** 由 Dan Smith（KK7DS）创建，自 2008 年以来一直积极开发。它最初是针对 Icom IC-91/92 电台的工具，后来扩展为支持多家厂商的数百种电台型号。
