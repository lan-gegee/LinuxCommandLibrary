# TAGLINE

支持插件的轻量级音频播放器

# TLDR

**启动** Audacious

```audacious```

播放**指定文件**

```audacious [file1.mp3] [file2.mp3]```

将文件加入**播放队列**

```audacious -e [file.mp3]```

**无界面**启动（不显示 GUI）

```audacious -H```

**显示**当前曲目

```audacious -t```

# SYNOPSIS

**audacious** [_-e_] [_-H_] [_options_] [_files_]

# DESCRIPTION

**audacious** 是一款轻量级的基于 GTK 的音频播放器，注重低资源占用和高音质。它通过插件支持众多格式，并提供 Winamp 经典界面模式。

该播放器在保持简洁的同时，强调通过皮肤和插件进行自定义。

# PARAMETERS

**-e**, **--enqueue**
> 将文件加入播放列表而不立即播放

**-H**, **--headless**
> 不带 GUI 运行

**-t**, **--show-main-window**
> 显示主窗口

**-p**, **--play**
> 开始播放

**-u**, **--pause**
> 暂停播放

**-s**, **--stop**
> 停止播放

**-f**, **--fwd**
> 向后跳转

**-r**, **--rew**
> 向前跳转

**--shuffle**
> 切换随机播放

**--repeat**
> 切换循环播放

**-m**, **--show-jump-box**
> 显示跳转到文件对话框

# CONFIGURATION

**~/.config/audacious/config**
> 主配置文件，包含播放器设置和偏好。

**~/.config/audacious/plugin-registry**
> 已安装插件及其启用状态的注册表。

# CAVEATS

插件可用性因发行版而异。某些格式需要额外的编解码器。GTK2 版本（旧版）与 GTK3/Qt 版本存在差异。

# HISTORY

**Audacious** 于 **2005** 年从 Beep Media Player（本身是 XMMS 的分支）分叉而来。它在 Linux 上延续了类 Winamp 界面的传统。

# INSTALL

```apt: sudo apt install audacious```

```dnf: sudo dnf install audacious```

```pacman: sudo pacman -S audacious```

```apk: sudo apk add audacious```

```zypper: sudo zypper install audacious```

```brew: brew install audacious```

```nix: nix profile install nixpkgs#audacious```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[mpv](/man/mpv)(1), [vlc](/man/vlc)(1)
