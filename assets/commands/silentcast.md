# TAGLINE

创建无声屏幕录像和 GIF

# TLDR

**启动** silentcast

```silentcast```

在**指定显示器**上启动

```silentcast --display=[display]```

# SYNOPSIS

**silentcast** [**--display**=_display_]

# PARAMETERS

**--display** _display_
> 指定要录制的 X 显示器

# DESCRIPTION

**silentcast** 创建 MKV 格式的无声视频屏幕录像和动画 GIF。它提供图形界面来录制不带音频的屏幕活动，非常适合制作教程、文档或演示。

工作流程是：启动应用，把绿色录制矩形框定位到目标窗口或区域上，按回车键开始录制，点击系统托盘图标停止。录制结果可处理成动画 GIF 或按需编辑。

# CAVEATS

不能同时运行多个实例。不支持录制自身界面。需要 GTK3、FFmpeg 和 ImageMagick 作为依赖。某些桌面环境（KDE Plasma 5、i3wm）可能需要特殊配置键盘快捷键才能正常工作。

# HISTORY

**silentcast** 由 **Colin Keenan** 创建，是一款开源屏幕录制工具。3.0 版本引入了完全重新设计的 GUI 界面。该项目以 GPL-3.0 许可证发布并在 GitHub 上维护。

# INSTALL

```aur: yay -S silentcast```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [byzanz-record](/man/byzanz-record)(1), [recordmydesktop](/man/recordmydesktop)(1), [peek](/man/peek)(1)
