# TAGLINE

为 CUPS 调度器配置 cupsd.conf 选项

# TLDR

**显示当前 CUPS** 服务器设置

```cupsctl```

**启用远程管理**

```cupsctl --remote-admin```

**启用打印机共享并**允许从任意地址访问

```cupsctl --share-printers --remote-any```

开启向 error_log 的**调试日志**

```cupsctl --debug-logging```

**禁用打印机共享**

```cupsctl --no-share-printers```

以加密方式与**远程调度器通信**

```cupsctl -E -h [server:631] --no-remote-admin```

**设置任意** cupsd.conf 指令

```cupsctl [MaxJobs=500]```

# SYNOPSIS

**cupsctl** [**-E**] [**-U** _username_] [**-h** _server_[:_port_]] [**--**[**no-**]**debug-logging**] [**--**[**no-**]**remote-admin**] [**--**[**no-**]**remote-any**] [**--**[**no-**]**share-printers**] [**--**[**no-**]**user-cancel-any**] [_name_=_value_ ...]

# PARAMETERS

**-E**
> 启用与调度器之间连接的加密。

**-U** _username_
> 以 _username_ 而非当前用户进行身份验证。

**-h** _server_[:_port_]
> 连接给定主机（及可选端口）上的调度器。

**--debug-logging** / **--no-debug-logging**
> 启用或禁用向 error_log 文件的调试日志。

**--remote-admin** / **--no-remote-admin**
> 启用或禁用远程管理。

**--remote-any** / **--no-remote-any**
> 启用或禁用来自任意地址（包括互联网）的打印。

**--share-printers** / **--no-share-printers**
> 启用或禁用与其他计算机共享本地打印机。

**--user-cancel-any** / **--no-user-cancel-any**
> 允许或禁止用户取消其他用户的任务。

_name_=_value_
> 直接设置任意的 **cupsd.conf** 指令。

# DESCRIPTION

**cupsctl** 更新 CUPS 调度器使用的 **cupsd.conf** 文件。不带参数运行时会以 _name_=_value_ 对的形式打印当前设置；传入选项或 _name_=_value_ 参数则会修改配置，并让 **cupsd** 重新加载。

由于 **cupsctl** 通过 IPP 与 **cupsd** 通信而不是直接编辑文件，因此无需 Shell 访问服务器即可管理本地或远程的调度器。

# CAVEATS

修改服务器设置通常需要管理员（root）权限或属于 **lpadmin** 组。未知或拼写错误的 _name_=_value_ 指令会被静默接受；请再执行一次不带参数的 **cupsctl** 来核对结果。某些设置需要完全重启 **cupsd** 才能彻底生效。

# HISTORY

**cupsctl** 由 Apple 在 **CUPS 1.3** 发布前后（2007 年）加入 **CUPS**，作为直接编辑 **cupsd.conf** 的便捷封装。CUPS 本身由 Michael Sweet 于 1999 年创建，现由 OpenPrinting 项目开发。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cupsd](/man/cupsd)(8), [cups-config](/man/cups-config)(1), [lpadmin](/man/lpadmin)(8), [lpinfo](/man/lpinfo)(8), [lpstat](/man/lpstat)(1), [lp](/man/lp)(1)
