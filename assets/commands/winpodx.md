# TAGLINE

在 Linux 上以原生窗口运行 Windows 应用

# TLDR

**启动 Windows pod** 并等待 RDP 就绪

```winpodx pod start --wait```

**列出 pod 内检测到的可用 Windows 应用**

```winpodx app list```

**启动已注册的应用**（如 Microsoft Word）

```winpodx app run [app_name]```

用 Windows 应用程序**打开本地文件**

```winpodx app run [app_name] [path/to/file]```

以单个 RDP 窗口的形式**启动完整的 Windows 桌面**

```winpodx app run desktop```

**打开 Qt6 图形界面**

```winpodx gui```

完成后**停止 pod**

```winpodx pod stop```

**运行交互式设置向导**

```winpodx setup```

# SYNOPSIS

**winpodx** _domain_ _command_ [_arguments_] [**--flags**]

# PARAMETERS

**app list**
> 显示 pod 内检测到的所有 Windows 应用。

**app run** _name_ [_file_]
> 以 RemoteApp 窗口的方式启动指定应用。可选的文件将用该应用打开。

**app install** _name_
> 将自定义应用注册到桌面启动器菜单。

**app install-all**
> 将检测到的每个应用都注册为桌面启动器条目。

**app sessions**
> 列出活动的 RemoteApp 会话。

**app kill** _name_
> 终止正在运行的 RemoteApp 会话。

**app refresh**
> 重新扫描 Windows 客户机以发现新安装的应用。

**pod start** [**--wait**]
> 启动 Windows 容器。**--wait** 会阻塞直到 RDP 可连接。

**pod stop**
> 停止 Windows 容器。

**pod restart**
> 重启 Windows 容器。

**pod status**
> 打印容器、RDP 和代理的状态。

**pod wait-ready** [**--logs**]
> 阻塞直到首次启动的 Sysprep / OEM 阶段结束。**--logs** 会流式输出进度。

**pod apply-fixes**
> 重新应用 Windows 侧的配置调整（注册表、服务、默认值）。

**pod sync-password**
> 在 **winpodx.toml** 与 Windows 客户机之间同步 RDP 密码。

**pod multi-session** {_on_|_off_|_status_}
> 切换内置的 rdprrap 多会话支持。

**power --suspend**
> 暂停正在运行的容器。

**power --resume**
> 恢复已暂停的容器。

**rotate-password**
> 生成并应用新的 RDP 密码。

**setup**
> 运行交互式首次配置向导。

**check** [**--json**]
> 运行健康探测（pod、RDP、代理、往返延迟、磁盘）并打印结果。

**info**
> 打印系统诊断信息（版本、路径、依赖）。

**cleanup**
> 清除客户机中过期的 Office 锁定文件。

**timesync**
> 强制 Windows 客户机进行一次时间同步。

**debloat**
> 禁用客户机中的遥测和不需要的服务。

**config show**
> 打印当前配置。

**config set** _key_ _value_
> 更新配置键（如 **rdp.scale 140**）。

**config import**
> 从现有的 **winapps.conf** 导入设置。

**gui**
> 启动 Qt6 主窗口。

**tray**
> 启动系统托盘图标。

# DESCRIPTION

**winpodx** 在 Podman 或 Docker 容器内运行一个 Windows 客户机，并通过 **FreeRDP** RemoteApp 把各个 Windows 应用呈现为原生的 Linux 窗口。每个应用都有自己可固定、可 Alt-Tab 切换的窗口，带有原始图标和文件关联，而不会暴露底层的 Windows 桌面。

客户机内的一个小型 HTTP 代理接收来自宿主机的 bearer 认证命令，因此启动应用时不会闪现 PowerShell 窗口。应用发现、密码轮换、多会话和健康检查都由 **winpodx** CLI 驱动；Qt6 GUI 提供相同的操作，外加一个带白名单的应用内终端。

**winpodx** 仅面向 Linux。首次运行会下载 Windows ISO、执行 Sysprep 并应用 OEM 定制步骤；在 pod 可用之前预计需要五到十分钟。

# CONFIGURATION

配置文件位于 _~/.config/winpodx/winpodx.toml_，可通过 **winpodx config set** 编辑：

```
[pod]
backend = "podman"        # or "docker"
cpus = 4
ram = "8G"
auto_start = true
idle_timeout = "30m"

[rdp]
host = "127.0.0.1"
port = 3389
scale = 100
dpi = 96
user = "winpodx"
password_rotation_days = 7

[agent]
port = 8765
token = "<generated>"
```

启动时读取的环境变量：

```
WINPODX_CONFIG       Override config file path
WINPODX_LOG_LEVEL    debug | info | warn | error
```

# CAVEATS

需要可正常工作的 Podman 或 Docker 安装、可用的 KVM 加速器，以及带有 RemoteApp 支持的较新 **FreeRDP 3** 版本。首次启动会执行完整的 Windows 安装加 Sysprep；不要中断 **winpodx pod wait-ready**。Microsoft Windows 本身仍受其自身许可条款约束，winpodx **不会再分发**它；用户需自行提供有效的 Windows 安装介质。客户机代理使用 bearer 令牌监听 **localhost:8765**；不要将该端口暴露给其他主机。

# HISTORY

**winpodx** 是一个 Python 3.9+ 项目，它把 **dockur/windows** 容器镜像与 **FreeRDP** RemoteApp 以及自定义的 PowerShell HTTP 客户机代理结合在一起。它面向与 **WinApps** 相同的使用场景，但将容器、代理和 GUI 作为单一工具交付，而不是依赖手动配置的虚拟机。开发仍在 **kernalix7/winpodx** 仓库持续进行。

# INSTALL

```aur: yay -S winpodx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [docker](/man/docker)(1), [xfreerdp](/man/xfreerdp)(1), [virsh](/man/virsh)(1), [wine](/man/wine)(1)
