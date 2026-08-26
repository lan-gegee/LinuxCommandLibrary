# TAGLINE

数字音频工作站

# TLDR

**启动 LMMS**

```lmms```

**打开项目**

```lmms [project.mmp]```

**渲染为音频**

```lmms -r [project.mmp] -o [output.wav]```

**渲染为 MP3**

```lmms -r [project.mmp] -o [output.mp3] -f mp3```

**导入 MIDI**

```lmms --import [file.mid]```

**无界面渲染**

```lmms -r [project.mmp] -o [output.wav] --loop```

# SYNOPSIS

**lmms** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要打开的项目文件。

**-r** _FILE_
> 将项目渲染为音频。

**-o** _FILE_
> 渲染的输出文件。

**-f** _FORMAT_
> 输出格式（wav、ogg、mp3）。

**--import** _FILE_
> 导入 MIDI 文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lmms** 是一个数字音频工作站，使用虚拟乐器、采样和效果器创作音乐。

该工具提供钢琴卷帘、步进音序器和自动化功能，支持 VST 和 LADSPA 插件。

# CAVEATS

以 GUI 为主。插件支持因平台而异。资源占用较高。

# HISTORY

LMMS（Linux MultiMedia Studio）的创建目的是提供一个免费的跨平台替代品，与 FL Studio 等商业 DAW 竞争。

# INSTALL

```apt: sudo apt install lmms```

```dnf: sudo dnf install lmms```

```pacman: sudo pacman -S lmms```

```apk: sudo apk add lmms```

```zypper: sudo zypper install lmms```

```nix: nix profile install nixpkgs#lmms```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ardour](/man/ardour)(1), [audacity](/man/audacity)(1)
