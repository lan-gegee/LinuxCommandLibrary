# TAGLINE

在 Sway 上显示带按钮的警告或错误消息

# TLDR

**显示一条简单的警告**消息

```swaynag -m "[Low battery]"```

**显示一条错误**（使用红色错误样式）

```swaynag -t error -m "[Disk full]"```

**添加一个**可运行命令的**按钮**

```swaynag -m "[Reboot required]" -b "[Reboot]" "[systemctl reboot]"```

**从标准输入读取详细消息**并显示切换按钮

```dmesg | swaynag -m "[Kernel messages]" -l```

将栏**锚定在屏幕底部**

```swaynag -m "[Bottom notice]" -e bottom```

**指定特定输出**

```swaynag -m "[Hello]" -o [HDMI-A-1]```

**使用自定义配置**文件

```swaynag -c [path/to/config] -m "[Hi]"```

# SYNOPSIS

**swaynag** [_options..._]

# PARAMETERS

**-m**, **--message** _text_
> 要显示的消息。

**-l**, **--detailed-message**
> 从标准输入读取详细消息；会添加一个用于切换详细文本的按钮。

**-L**, **--detailed-button** _text_
> 详细消息切换按钮的文字（默认：_Toggle details_）。

**-t**, **--type** _name_
> 消息类型（_error_、_warning_，或配置文件中定义的自定义类型）。每种类型有自己的配色。

**-e**, **--edge** _top|bottom_
> 锚定的屏幕边缘（默认：_top_）。

**-y**, **--layer** _overlay|top|bottom|background_
> 使用的 wlr-layer-shell 层（默认：_overlay_）。

**-o**, **--output** _name_
> 显示该栏的 xdg_output 名称。

**-b**, **--button** _text_ _command_
> 添加一个按钮，按下后在终端中运行 _command_。可重复使用。

**-B**, **--button-no-terminal** _text_ _command_
> 与 **-b** 相同，但不通过终端运行 _command_。

**-z**, **--button-dismiss** _text_ _command_
> 添加一个按钮，运行 _command_ 后关闭 swaynag。

**-Z**, **--button-dismiss-no-terminal** _text_ _command_
> 与 **-z** 相同，但不通过终端运行。

**-s**, **--dismiss-button** _text_
> 关闭按钮的文字（默认：_X_）。

**-f**, **--font** _font_
> Pango 字体描述。

**-c**, **--config** _file_
> 从 _file_ 加载配置。

**-v**, **--version**
> 打印版本并退出。

**-h**, **--help**
> 显示帮助并退出。

# CONFIGURATION

**swaynag** 会加载以下位置中第一个可读的文件：

```
$HOME/.swaynag/config
$XDG_CONFIG_HOME/swaynag/config
SYSCONFDIR/swaynag/config
```

配置文件采用 INI 风格的分节结构。节名对应 **-t**/**--type** 的取值；**[<default>]** 适用于所有类型。常见的键控制颜色、边框、内边距、字体、层和默认按钮。完整配置项请参阅 **swaynag**(5)。

# DESCRIPTION

**swaynag** 是 **Sway** 合成器的屏幕消息对话框。它在屏幕顶部或底部绘制一条栏，包含一条消息、可选的详细正文以及可选的按钮。Sway 本身会调用 **swaynag** 来提示配置错误或重要警告，但用户和脚本也可以直接调用它来显示确认信息、重启提示或自定义警告。

该工具使用 **wlr-layer-shell** 协议，因此仅适用于实现该协议的 Wayland 合成器（Sway 及其他基于 wlroots 的合成器）。

# HISTORY

**swaynag** 是 **Sway** 合成器的一部分。Sway 是一个与 i3 兼容的平铺式 Wayland 合成器，由 **Drew DeVault** 于 **2015 年**发起；**swaynag** 作为 Sway 过去针对配置错误所启动的 i3 nagbar 的替代品而加入。

# INSTALL

```apt: sudo apt install sway```

```dnf: sudo dnf install sway```

```pacman: sudo pacman -S sway```

```apk: sudo apk add swaynag```

```zypper: sudo zypper install sway```

```nix: nix profile install nixpkgs#sway```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [swaymsg](/man/swaymsg)(1), [swaybar](/man/swaybar)(5), [swaynag](/man/swaynag)(5)
