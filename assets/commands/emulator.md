# TAGLINE

用于测试应用的 Android SDK 模拟器

# TLDR

**启动 Android 模拟器**

```emulator -avd [avd_name]```

**列出可用的 AVD**

```emulator -list-avds```

**清除用户数据后启动**

```emulator -avd [avd_name] -wipe-data```

**不加载快照启动**

```emulator -avd [avd_name] -no-snapshot-load```

**启用 GPU 加速启动**

```emulator -avd [avd_name] -gpu host```

**以无界面模式启动**

```emulator -avd [avd_name] -no-window```

# SYNOPSIS

**emulator** [_options_] **-avd** _name_

# PARAMETERS

**-avd** _name_
> Android Virtual Device 名称。

**-list-avds**
> 列出可用的 AVD。

**-wipe-data**
> 重置用户数据。

**-no-snapshot-load**
> 不加载快照。

**-no-snapshot-save**
> 退出时不保存快照。

**-gpu** _mode_
> GPU 模式：auto、host、swiftshader、off。

**-no-window**
> 无界面模式。

**-no-audio**
> 禁用音频。

**-memory** _size_
> 内存大小（MB）。

**-port** _port_
> 控制台端口号。

**-dns-server** _servers_
> DNS 服务器地址。

**-http-proxy** _proxy_
> HTTP 代理地址。

**-writable-system**
> 使系统镜像在本会话中可写（`adb remount` 需要）。

**-snapshot** _name_
> 从指定名称的快照启动。

**-netdelay** _delay_
> 模拟网络延迟（gsm、edge、umts、none）。

**-netspeed** _speed_
> 模拟网络吞吐量（gsm、edge、umts、full）。

**-camera-back** _mode_
> 后置摄像头来源：emulated、webcam0、none。

**-verbose**
> 打印详细的启动与初始化消息。

# CONFIGURATION

**~/.android/avd/**
> 存放 Android Virtual Device 配置与数据的目录。

**config.ini**
> 每个 AVD 目录内的 AVD 专属配置文件。

# DESCRIPTION

**emulator** 是 Android 模拟器，属于 Android SDK 的一部分。它运行 Android Virtual Device（AVD）用于应用测试和开发，可模拟具有不同 API 级别和配置的各种 Android 设备。

模拟器提供 GPS 模拟、网络状况、来电/短信、摄像头以及加速度计输入等功能。它与 Android Studio 集成，便于调试和测试。

# CAVEATS

需要硬件虚拟化（Linux 上为 KVM，其他平台为 HAXM/Hypervisor）。首次启动较慢。x86 镜像的运行速度快于 ARM 模拟。需要较大的内存和 CPU 资源。部分硬件特性无法被完全模拟。

# HISTORY

Android 模拟器由 **Google** 随第一个 Android SDK 于 **2008 年**推出。此后它经历了长足演进，基于 QEMU 的架构不断提升性能与保真度。现代版本采用硬件加速和快速启动（quick boot）来缩短启动时间。

# SEE ALSO

[adb](/man/adb)(1), [avdmanager](/man/avdmanager)(1), [sdkmanager](/man/sdkmanager)(1)

# RESOURCES

```[Homepage](https://developer.android.com/studio/run/emulator)```

```[Documentation](https://developer.android.com/studio/run/emulator-commandline)```

<!-- verified: 2026-07-14 -->
