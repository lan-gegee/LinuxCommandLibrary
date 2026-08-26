# TAGLINE

安装和管理 Android SDK 软件包

# TLDR

**列出**可用和已安装的软件包

```sdkmanager --list```

仅**列出**已安装的软件包

```sdkmanager --list_installed```

**安装**平台软件包

```sdkmanager "platforms;android-35"```

一次**安装**多个软件包

```sdkmanager "platforms;android-35" "build-tools;35.0.0"```

**更新**所有已安装的软件包

```sdkmanager --update```

**卸载**软件包

```sdkmanager --uninstall "build-tools;34.0.0"```

非交互式**接受**所有待处理的许可协议

```yes | sdkmanager --licenses```

使用指定的 SDK 根目录和渠道**安装**软件包

```sdkmanager --sdk_root=[path] --channel=1 "platform-tools"```

# SYNOPSIS

**sdkmanager** [_--list_|_--list_installed_|_--update_|_--licenses_|_--uninstall_] [_options_] [_packages..._]

# PARAMETERS

**--list**
> 列出所有可用和已安装的软件包。

**--list_installed**
> 仅列出已安装的软件包。

**--update**
> 将所有已安装的软件包更新到最新版本。

**--uninstall** _PACKAGES_
> 移除指定的软件包。

**--licenses**
> 查看并接受 SDK 许可协议。安装软件包前必须完成。

**--sdk_root** _PATH_
> 指定 SDK 安装目录（覆盖 ANDROID_HOME）。

**--channel** _N_
> 包含指定渠道的软件包：0（stable，默认）、1（beta）、2（dev）、3（canary）。

**--no_https**
> 使用 HTTP 而非 HTTPS 下载。

**--verbose**
> 启用详细输出，显示错误、警告和所有消息。

**--proxy** _TYPE_
> 通过指定类型的代理连接（http 或 socks）。

**--proxy_host** _HOST_
> 代理的 IP 或 DNS 地址。

**--proxy_port** _PORT_
> 代理端口号。

# DESCRIPTION

**sdkmanager** 从命令行管理 Android SDK 组件，用于安装、更新和移除平台软件包、构建工具、系统镜像及其他 SDK 组件。它是 Android Studio 的 SDK Manager 的无界面版本，随 Android SDK Command-Line Tools 软件包提供。

软件包通过字符串路径标识，例如 **platforms;android-35** 表示平台 API、**build-tools;35.0.0** 表示编译工具、**system-images;android-35;google_apis;x86_64** 表示模拟器镜像。多个软件包可以在一条命令中安装，以空格分隔并各自加引号。

安装软件包前必须接受许可协议。交互式运行 **--licenses** 可接受所有待处理的许可，这对需要以非交互方式配置 SDK 的自动化 CI/CD 环境至关重要。

# CONFIGURATION

**ANDROID_HOME**
> 指定 Android SDK 安装根目录的环境变量。

**ANDROID_SDK_ROOT**
> ANDROID_HOME 的替代方案，用于指定 SDK 位置（已弃用，推荐使用 ANDROID_HOME）。

# CAVEATS

属于 Android SDK Command-Line Tools，需单独下载。需要设置 ANDROID_HOME 或 --sdk_root。软件包下载体积可能较大。如果已安装 Android Studio，也可以改用 IDE 内置的 SDK Manager。

# INSTALL

```nix: nix profile install nixpkgs#sdkmanager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[adb](/man/adb)(1), [avdmanager](/man/avdmanager)(1), [emulator](/man/emulator)(1), [gradle](/man/gradle)(1)
