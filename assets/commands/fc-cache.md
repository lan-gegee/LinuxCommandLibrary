# TAGLINE

构建 fontconfig 缓存文件

# TLDR

为所有目录**重建字体缓存**

```fc-cache```

**强制重建**并输出详细信息

```fc-cache -fv```

只**重建系统级缓存**（需要 root）

```sudo fc-cache -fvs```

为指定目录**重建缓存**

```fc-cache [path/to/fonts/directory]```

**清除所有缓存**并从头重建

```fc-cache -r```

检查缓存文件是否为最新（极度详细）

```fc-cache -rv```

# SYNOPSIS

**fc-cache** [**-EfrsvVh**] [**--error-on-no-fonts**] [**--force**] [**--really-force**] [**--system-only**] [**--verbose**] [**--version**] [**--help**] [_DIR_...]

# PARAMETERS

**-f**, **--force**
> 强制重新生成缓存文件，忽略时间戳检查。

**-r**, **--really-force**
> 清除所有现有缓存文件并重新扫描。

**-s**, **--system-only**
> 只扫描系统级目录，跳过用户主目录位置。

**-v**, **--verbose**
> 处理时显示状态信息。

**-E**, **--error-on-no-fonts**
> 如果指定目录中没有字体则报错。

**-V**, **--version**
> 显示 fontconfig 版本并退出。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**fc-cache** 扫描字体目录，并为使用 fontconfig 的应用程序构建字体信息缓存文件。这些缓存将字体文件名映射到字体属性，使应用启动时能快速查找字体，而无需扫描所有字体文件。

如果不给目录参数，fc-cache 会处理当前 fontconfig 配置中的所有目录。每个目录都会被扫描以查找 FreeType 可读的字体文件，并创建包含字体属性及相关文件名的缓存文件。

用户缓存放置在 **~/.cache/fontconfig/**，系统缓存放置在 **/var/cache/fontconfig/**。添加或删除字体后必须重新生成缓存。

# CONFIGURATION

**~/.cache/fontconfig/**
> 用户特定的字体缓存文件。

**/var/cache/fontconfig/**
> 系统级的字体缓存文件。

**/etc/fonts/fonts.conf**
> 主 fontconfig 配置文件，指定字体目录。

**~/.config/fontconfig/fonts.conf**
> 用户特定的 fontconfig 配置。

# CAVEATS

fc-cache 必须针对每种架构各运行一次，才能生成正确定制的字体信息。安装新字体后，运行 **fc-cache -fv** 可确保字体立即对应用可用。即使重新生成了缓存，某些应用可能仍需重启才能加载新字体。

# HISTORY

Fontconfig 由 Keith Packard 于 **2000 年**发起，旨在改进 X11 的字体处理，从早期侧重位图的 X 字体系统演进为支持可缩放字体。fc-cache 工具随着 **2002 年** Fontconfig 2.0 发布趋于稳定。Fontconfig 已成为 Linux 桌面上的标准字体配置系统。

# INSTALL

```apt: sudo apt install fontconfig```

```dnf: sudo dnf install fontconfig```

```pacman: sudo pacman -S fontconfig```

```apk: sudo apk add fontconfig```

```zypper: sudo zypper install fontconfig```

```brew: brew install fontconfig```

```nix: nix profile install nixpkgs#fontconfig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fc-list](/man/fc-list)(1), [fc-match](/man/fc-match)(1), [fc-query](/man/fc-query)(1), [fc-scan](/man/fc-scan)(1)
