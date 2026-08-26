# TAGLINE

Cockpit Web 服务消息中继

# TLDR

显示 bridge 已知的**已安装 Cockpit 软件包**

```cockpit-bridge --packages```

打印 bridge 的**用法与选项**

```cockpit-bridge --help```

# SYNOPSIS

**cockpit-bridge** [_options_]

# DESCRIPTION

**cockpit-bridge** 在 Cockpit Web 前端与服务器端系统配置工具之间转发消息和命令。它作为通信层，让基于浏览器的界面能够与 systemd、NetworkManager 和存储管理等系统服务交互。

bridge 运行在用户的会话中，将基于 JSON 的 Cockpit 协议消息转换为 D-Bus 调用、文件操作和进程管理动作。它强制执行登录用户的权限，确保 Web 界面无法执行超出用户授权范围的操作。

此进程通常由 cockpit-ws 自动启动，不打算由用户直接运行。**--packages** 选项在调试时很有用，可列出所有已安装的 Cockpit UI 软件包。

# PARAMETERS

**--packages**
> 列出所有可用的 Cockpit 软件包

**--help**
> 显示帮助信息

# CONFIGURATION

**/etc/cockpit/cockpit.conf**
> Cockpit 主配置文件，控制 bridge 行为、允许的来源以及认证设置。

# CAVEATS

Cockpit 套件的组成部分。通常由 cockpit-ws 自动调用，而非用户直接调用。需要正确安装 Cockpit。

# INSTALL

```dnf: sudo dnf install cockpit-bridge```

```zypper: sudo zypper install cockpit-bridge```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cockpit-ws](/man/cockpit-ws)(8), [cockpit-tls](/man/cockpit-tls)(8)

# RESOURCES

```[Source code](https://github.com/cockpit-project/cockpit)```

```[Documentation](https://cockpit-project.org/guide/latest/)```

<!-- verified: 2026-06-22 -->
