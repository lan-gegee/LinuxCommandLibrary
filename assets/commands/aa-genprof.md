# TAGLINE

通过监控程序行为生成 AppArmor 配置文件

# TLDR

开始为程序生成**配置文件**

```sudo aa-genprof [/path/to/program]```

为配置文件指定**自定义目录**

```sudo aa-genprof -d [/path/to/profiles] [/path/to/program]```

为分析指定**自定义日志文件**

```sudo aa-genprof -f [/path/to/logfile] [/path/to/program]```

# SYNOPSIS

**aa-genprof** _executable_ [**-d** _/path/to/profiles_] [**-f** _/path/to/logfile_]

# DESCRIPTION

**aa-genprof** 是 AppArmor 的配置文件生成工具，它通过监控程序行为自动创建安全配置文件。如果尚无配置文件，它会先用 **aa-autodep** 创建一个。随后它将该配置文件设为投诉模式，向系统日志写入一个标记，并提示用户在另一个窗口中操作该应用程序。

当用户选择 **(S)can** 时，aa-genprof 解析投诉模式日志，并借助 **aa-logprof** 逐条处理违规记录。当用户选择 **(F)inish** 时，所有生成的配置文件都会被设为强制模式。

# PARAMETERS

**-d, --dir** _/path/to/profiles_
> 指定查找 AppArmor 安全配置文件集的位置；默认为 /etc/apparmor.d

**-f, --file** _/path/to/logfile_
> 指定日志文件位置；默认位置从 /etc/apparmor/logprof.conf 读取

**-h, --help**
> 显示帮助信息

# CONFIGURATION

**/etc/apparmor/logprof.conf**
> 控制默认日志文件位置、软件仓库设置以及配置文件生成过程中使用的其他选项。

# CAVEATS

生成配置文件需要让目标应用程序执行其所有常规操作，以捕获必要的访问模式。测试不充分可能生成阻碍正常功能的配置文件。需要 root 权限。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **apparmor-utils** 软件包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-logprof](/man/aa-logprof)(8), [aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [aa-disable](/man/aa-disable)(8), [aa-mergeprof](/man/aa-mergeprof)(8), [aa-status](/man/aa-status)(8), [aa-unconfined](/man/aa-unconfined)(8), [apparmor](/man/apparmor)(7)
