# TAGLINE

带 TUI 的跨平台音频录制/播放命令行工具

# TLDR

**录制音频**到 WAV 文件

```asak rec [output]```

**播放** WAV 文件

```asak play [input.wav]```

通过从当前目录的 WAV 文件中选择，**交互式播放文件**

```asak play```

按索引**使用指定音频设备录制**

```asak rec -d [device_index] [output]```

实时**监听音频输入**并通过输出设备播放

```asak monitor```

以自定义缓冲区大小进行**监听**

```asak monitor -b [2048]```

**列出可用的音频设备**

```asak list```

# SYNOPSIS

**asak** [**-j**] _command_ [_options_]

**asak rec** [**-d** _index_] [_output_]

**asak play** [**-d** _index_] [_input_]

**asak monitor** [**-b** _size_]

**asak list**

# PARAMETERS

**-j**, **--jack**
> 使用 JACK 音频后端代替默认后端。仅在 Linux、DragonFly BSD、FreeBSD 和 NetBSD 上且以 jack 特性构建时可用。

**-d** _index_, **--device** _index_
> 用于录音或播放的音频设备索引。运行 **asak list** 可查看可用设备及其索引。

**-b** _size_, **--buffer_size** _size_
> 音频输入监听的缓冲区大小。默认 1024。数值越大延迟越高。

**-h**, **--help**
> 显示帮助信息并退出。

**-V**, **--version**
> 显示版本信息并退出。

# DESCRIPTION

**asak**（audio Swiss Army knife，音频瑞士军刀）是一个用 Rust 编写、带终端用户界面的跨平台音频录制与播放命令行工具。它旨在提供类似 SoX 的功能，同时带来交互式和可视化的体验。

该工具提供四个主要子命令。**rec** 将输入设备的音频录制成 WAV 文件；若未给出文件名，它会交互式提示并建议一个带 UTC 时间戳的默认名称。**play** 播放 WAV 文件；若未指定文件，它会在当前目录搜索 WAV 文件并提供交互式选择菜单。**monitor** 将输入设备的音频实时路由到输出设备，并带有可视化示波器显示，适合快速测试麦克风或音箱设置。**list** 显示所有可用的音频输入和输出设备及其索引。

asak 使用 **cpal** 作为音频后端，用 **ratatui** 构建终端 UI，提供电平表和播放动画等可视化反馈。当源与目标的采样率不同时，重采样由 **dasp** 库处理。

# CAVEATS

目前录制和播放仅支持 WAV 格式。**monitor** 子命令要求输出设备与系统默认设置一致。在 Linux 上，JACK 音频后端需要安装 **libjack-dev**（或等效库），并且工具需以 **jack** 特性标志构建。项目仍在积极开发中，效果处理和实时位置控制等部分功能尚未实现。

# HISTORY

**asak** 由奥斯陆大学开发者 **Qichao Lan**（chaosprint）创建，他专注于 Rust 音频编程，也是面向图的现场编程语言 **Glicol** 的作者。最早的提交出现在 **2024 年初**，项目于 **2024 年 12 月**在 Hacker News 上公开发布。到 2025 年年中，该工具已达到 0.3.6 版本。它采用 MIT 许可证授权。

# INSTALL

```aur: yay -S asak```

```brew: brew install asak```

```nix: nix profile install nixpkgs#asak```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[sox](/man/sox)(1), [arecord](/man/arecord)(1), [aplay](/man/aplay)(1), [play](/man/play)(1), [rec](/man/rec)(1), [ffmpeg](/man/ffmpeg)(1)
