# TAGLINE

跨平台终端音频频谱可视化器

# TLDR

**启动音频可视化器**

```cava```

**使用自定义配置文件**

```cava -p [/path/to/config]```

**显示版本**

```cava -v```

# SYNOPSIS

**cava** [_options_]

# DESCRIPTION

**cava**（Console Audio Visualizer for ALSA）是一个条形频谱音频可视化器，在终端或桌面上以动画条形显示实时频率分析。它从系统捕获音频，并将其渲染成彩色的均衡器风格画面。

该可视化器支持多种音频后端，包括 ALSA、PulseAudio、PipeWire、JACK、sndio 和 PortAudio。输出可以通过 ncurses 渲染到终端，通过 SDL 渲染为桌面窗口，或者输出原始数据供管道传给其他程序。所有视觉和音频设置均通过配置文件控制。

# PARAMETERS

**-p** _path_
> 配置文件路径

**-v**
> 打印版本

# CONTROLS

**q** / **Ctrl+C**
> 退出

**r**
> 重新加载配置

# CONFIGURATION

**~/.config/cava/config**
> 控制条形宽度、间距、颜色、渐变、音频源、灵敏度、平滑度以及输出模式。

# AUDIO SOURCES

- PulseAudio
- PipeWire
- ALSA
- JACK
- sndio
- PortAudio
- FIFO 缓冲区

# SIGNALS

**SIGUSR1**
> 强制重新加载配置

# CAVEATS

需要音频捕获权限。不同的音频后端需要相应的开发库。播放音乐时效果最佳。

# INSTALL

```apt: sudo apt install cava```

```dnf: sudo dnf install cava```

```pacman: sudo pacman -S cava```

```zypper: sudo zypper install cava```

```brew: brew install cava```

```nix: nix profile install nixpkgs#cava```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[alsamixer](/man/alsamixer)(1), [pavucontrol](/man/pavucontrol)(1)

# RESOURCES

```[Source code](https://github.com/karlstav/cava)```

<!-- verified: 2026-06-22 -->
