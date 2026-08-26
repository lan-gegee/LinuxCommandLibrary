# TAGLINE

用于录音和混音的专业数字音频工作站

# TLDR

带图形界面**启动 Ardour**

```ardour```

**打开指定的会话**

```ardour [path/to/session]```

从命令行**创建新会话**

```ardour -N [session-name]```

使用模板**创建新会话**

```ardour -N [session-name] -T [template-name]```

禁用所有插件后以**安全模式启动**

```ardour -d [path/to/session]```

在现有会话中**旁通所有插件**

```ardour -B [path/to/session]```

**显示所有可用的按键绑定**

```ardour -b```

# SYNOPSIS

**ardour** [_OPTIONS_] [_SESSION-NAME_]

# PARAMETERS

**-a**, **--no-announcements**
> 不访问网站获取公告。

**-A**, **--actions**
> 打印所有可用的菜单动作名称。

**-b**, **--bindings**
> 显示当前所有的按键绑定。

**-B**, **--bypass-plugins**
> 旁通现有会话中的所有插件。

**-c**, **--name** _NAME_
> 使用指定的后端客户端名（默认为 ardour）。

**-d**, **--disable-plugins**
> 禁用所有插件（安全模式）。

**-D**, **--debug** _OPTIONS_
> 设置调试标志。用 -D list 查看可用选项。

**-h**, **--help**
> 显示帮助信息。

**-k**, **--keybindings** _FILE_
> 从指定文件加载按键绑定。

**-m**, **--menus** _FILE_
> 使用指定文件定义菜单。

**-n**, **--no-splash**
> 不显示启动画面。

**-N**, **--new** _SESSION-NAME_
> 通过命令行创建新会话。

**-O**, **--no-hw-optimizations**
> 禁用硬件相关的优化。

**-P**, **--no-connect-ports**
> 启动时跳过自动端口连接。

**-S**, **--sync**
> 同步绘制 GUI。

**-T**, **--template** _NAME_
> 为新会话应用模板。

**-v**, **--version**
> 显示版本信息并退出。

# DESCRIPTION

**Ardour** 是面向专业音频制作的多声道硬盘录音机（HDR）和数字音频工作站（DAW）。它提供完整的多轨录音、编辑、混音和母带处理能力，可与商业 DAW 软件媲美。

Ardour 使用 JACK（JACK Audio Connection Kit）进行所有音频 I/O，可与其他应用及硬件音频接口实现完美的采样级同步数据交换。它能够同时录制 24 路甚至更多 48kHz 的 32 位音频。该软件支持 LADSPA、LV2、VST 和 AudioUnit 插件，用于效果处理和虚拟乐器。

会话以目录形式存储，包含全部项目数据，包括音频文件、编辑记录、自动化和设置。Ardour 支持非破坏性编辑，并提供无限的撤销历史。

# CONFIGURATION

**~/.config/ardour8/**
> 用户配置目录，包含偏好设置、按键绑定、插件设置和模板。目录名包含主版本号（如 ardour7、ardour8）。

# CAVEATS

Ardour 需要 JACK 或 PipeWire 进行音频 I/O。实时音频性能取决于正确的系统配置，包括面向低延迟运行的内核设置。插件的兼容性因格式和平台而异。

# HISTORY

Ardour 由 Paul Davis 开发，他同时也是 JACK Audio Connection Kit 的负责人。开发始于 **1999** 年，首次公开发布于 **2005** 年。它已成为最强大的开源 DAW 之一，被全球的专业录音棚和音乐人使用。该项目依靠订阅和捐款资助。

# INSTALL

```apt: sudo apt install ardour```

```pacman: sudo pacman -S ardour```

```zypper: sudo zypper install ardour```

```nix: nix profile install nixpkgs#ardour```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[jackd](/man/jackd)(1), [audacity](/man/audacity)(1), [lmms](/man/lmms)(1)
