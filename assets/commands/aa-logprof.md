# TAGLINE

基于日志事件交互式更新 AppArmor 配置文件

# TLDR

基于系统日志交互式**审查并更新**配置文件

```sudo aa-logprof```

为 AppArmor 配置文件指定一个**特定目录**

```sudo aa-logprof -d /path/to/profiles```

使用**特定日志文件**代替默认值

```sudo aa-logprof -f /path/to/logfile```

忽略某个标记**之前的所有日志条目**

```sudo aa-logprof -m "log_marker_text"```

# SYNOPSIS

**aa-logprof** [_-d /path/to/profiles_] [_-f /path/to/logfile_] [_-m mark_]

# DESCRIPTION

**aa-logprof** 是一个交互式工具，它扫描 AppArmor 安全日志，并提示用户审查和更新现有的安全配置文件。启动后，它会识别当前配置文件未覆盖的新 AppArmor 事件，并提出修改建议。

退出时，更新后的配置文件会被保存；如果 AppArmor 处于活动状态，还会重新加载。交互选项包括：**(A)llow**、**(D)eny**、**(I)gnore**、**(N)ew**、**(G)lob last piece**、**(Q)uit**。

# PARAMETERS

**-d, --dir /path/to/profiles**
> 指定查找 AppArmor 安全配置文件集的位置；默认为 /etc/apparmor.d

**-f, --file /path/to/logfile**
> 指定日志文件位置；默认值从 /etc/apparmor/logprof.conf 读取

**-m, --logmark "mark"**
> 过滤掉指定标记之前的日志条目；标记含空格时请使用引号

**-h, --help**
> 显示帮助信息

# CONFIGURATION

**/etc/apparmor/logprof.conf**
> 控制默认日志文件位置、软件仓库设置以及基于日志更新配置文件时的行为选项。

# CAVEATS

日志分析依赖审计守护进程的配置。请确保 **auditd** 或 **klogd** 已正确配置以捕获 AppArmor 事件。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-genprof](/man/aa-genprof)(8), [aa-cleanprof](/man/aa-cleanprof)(8), [aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [auditd](/man/auditd)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
