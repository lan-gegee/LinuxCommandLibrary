# TAGLINE

管理 Apple iOS 模拟器

# TLDR

**列出所有模拟器**和运行时

```xcrun simctl list```

按名称或 UUID **启动模拟器**

```xcrun simctl boot "[iPhone 15 Pro]"```

关闭模拟器

```xcrun simctl shutdown [device_uuid|booted]```

在已启动的模拟器上**安装应用**

```xcrun simctl install booted [path/to/app.app]```

在模拟器上**启动应用**

```xcrun simctl launch booted [com.example.bundleid]```

对模拟器**截图**

```xcrun simctl io booted screenshot [output.png]```

发送推送通知

```xcrun simctl push booted [com.example.bundleid] [notification.apns]```

向应用授予隐私权限

```xcrun simctl privacy booted grant [location] [com.example.bundleid]```

# SYNOPSIS

**xcrun simctl** _subcommand_ [_arguments_]

# SUBCOMMANDS

**list** [_devices_|_devicetypes_|_runtimes_|_pairs_]
> 列出可用设备、设备类型、运行时或设备配对。

**create** _name_ _devicetype_ _runtime_
> 以指定的名称、设备类型和运行时创建新模拟器。

**delete** _device_
> 删除模拟器设备。

**boot** _device_
> 启动模拟器设备。

**shutdown** _device_|**all**
> 关闭某个模拟器或全部模拟器。

**erase** _device_|**all**
> 清空模拟器的内容与设置。

**install** _device_ _app_path_
> 在模拟器上安装应用 bundle。

**uninstall** _device_ _bundle_id_
> 按 bundle 标识符卸载应用。

**launch** _device_ _bundle_id_ [_args_]
> 在模拟器上启动应用。

**terminate** _device_ _bundle_id_
> 终止正在运行的应用。

**io** _device_ _operation_
> 执行 I/O 操作：screenshot、recordVideo。

**push** _device_ _bundle_id_ _json_file_
> 向正在运行的应用发送推送通知。

**privacy** _device_ _action_ _service_ _bundle_id_
> 管理隐私权限（grant、revoke、reset）。

**addmedia** _device_ _paths_
> 向模拟器的照片库添加照片或视频。

**openurl** _device_ _url_
> 在模拟器中打开 URL。

**runtime** **add**|**delete** _path_
> 管理模拟器运行时磁盘映像。

**help** [_subcommand_]
> 显示 simctl 或特定子命令的帮助。

# DESCRIPTION

**simctl** 是 Apple 提供的命令行工具，用于管理和操作 macOS 上的 iOS、watchOS 和 tvOS 模拟器。它通过 **xcrun simctl** 调用，以确保使用与你当前 Xcode 安装匹配的正确版本。

该工具全面控制模拟器的生命周期（创建、启动、关闭、删除）、应用管理（安装、启动、卸载）以及测试功能（推送通知、隐私权限、截图、视频录制）。它对自动化测试、CI/CD 流水线和开发工作流尤其有用。

特殊标识符 **booted** 可用于定位当前正在运行的模拟器，而无需指定 UUID。

# CAVEATS

仅在安装了 Xcode 的 macOS 上可用。需要 Xcode 命令行工具。隐私管理等部分功能需要 Xcode 11.4 或更高版本。模拟器运行时会占用大量磁盘空间。工具路径为 **/Applications/Xcode.app/Contents/Developer/usr/bin/simctl**，但应通过 **xcrun** 调用以确保版本兼容。

# HISTORY

**simctl** 由 Apple 作为 Xcode 的一部分推出，用于取代较旧的模拟器管理工具。它随 iOS 开发不断演进，增加了推送通知测试、隐私权限管理和改进的运行时处理等功能。该工具已成为 iOS CI/CD 工作流和自动化测试的必备工具，地位相当于 Android 的 **adb** 命令。

# SEE ALSO

[xcrun](/man/xcrun)(1), [xcodebuild](/man/xcodebuild)(1)
