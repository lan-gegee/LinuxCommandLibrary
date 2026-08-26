# TAGLINE

为 Raspberry Pi 把操作系统镜像写入 SD 卡和 USB 驱动器

# TLDR

**启动图形界面**

```rpi-imager```

**以无头 CLI 模式写入镜像**

```rpi-imager --cli [image.img] [/dev/sdX]```

**写入并对照已知的 SHA-256 进行校验**

```rpi-imager --cli --sha256 [hash] [image.img] [/dev/sdX]```

**写入时不做校验（更快，但无完整性检查）**

```rpi-imager --cli --disable-verify [image.img] [/dev/sdX]```

**安静 CLI 模式**（适合脚本使用）

```rpi-imager --cli --quiet [image.img] [/dev/sdX]```

**使用自定义的操作系统列表源**

```rpi-imager --repo [https://your-host/os-list.json]```

**禁用遥测**

```rpi-imager --disable-telemetry```

# SYNOPSIS

**rpi-imager** [**--cli**] [_options_] [_image_] [_device_]

# PARAMETERS

**--cli**
> 命令行模式 —— 不显示 GUI。

**--debug**
> 输出详细调试信息；在 Windows 上会附带一个控制台窗口。

**--version**
> 打印应用程序版本并退出。

**--repo** _URL_
> 从自定义 URL 或本地文件路径加载操作系统列表。

**--qm** _FILE_
> 加载自定义的 Qt `.qm` 翻译文件。

**--refresh-interval** _MIN_
> 操作系统列表两次刷新之间的间隔秒数（非零时最小值为 1440 分钟）。

**--refresh-jitter** _MIN_
> 叠加到刷新间隔上的抖动量（非零时最小值为 180 分钟）。

**--disable-telemetry**, **--enable-telemetry**
> 关闭或恢复遥测。该设置会被持久保存。

**--disable-verify**
> 仅限 CLI。跳过写入后的重读校验环节。

**--sha256** _HASH_
> 仅限 CLI。校验写入的数据与给定的 SHA-256 是否一致。

**--quiet**
> 仅限 CLI。抑制进度输出。

**--help**
> 显示用法信息。

# DESCRIPTION

**rpi-imager** 是官方的 Raspberry Pi 镜像烧录工具，用于把操作系统镜像写入 SD 卡和 USB 驱动器。GUI 负责镜像发现、下载和首次启动定制（主机名、SSH、Wi-Fi、区域设置、时区、用户账户）。**--cli** 模式则是脚本化接口：它把单个镜像写入单个设备并校验结果。主机名、Wi-Fi 等定制选项只在 GUI 中提供——它们并不是 CLI 标志。

该工具从 JSON 列表下载并缓存官方及第三方镜像，通过校验和验证下载内容，并在写入后重新读取设备，以检测悄然失效的 SD 卡。

# CAVEATS

写入目标设备需要 root/管理员权限；选错设备会销毁数据——请务必反复核对路径。通过脚本预置 SSH/Wi-Fi 需要使用 GUI（它会写入 cloud-init 风格的 `firstrun` 配置负载），或改用 `systemd-firstboot` 之类的独立工具。

# HISTORY

**rpi-imager** 由 **Raspberry Pi Ltd** 于 **2020 年 3 月**发布，用于取代第三方的镜像烧录工具。**--cli** 模式、SHA-256 校验和遥测控制是在后续版本中陆续加入的。

# INSTALL

```dnf: sudo dnf install rpi-imager```

```pacman: sudo pacman -S rpi-imager```

```zypper: sudo zypper install rpi-imager```

```nix: nix profile install nixpkgs#rpi-imager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [balena-etcher](/man/balena-etcher)(1), [gnome-disks](/man/gnome-disks)(1)
