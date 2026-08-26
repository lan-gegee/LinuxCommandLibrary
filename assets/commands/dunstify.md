# TAGLINE

面向 dunst 的桌面通知发送工具

# TLDR

**发送通知**

```dunstify "[message]"```

**带标题的通知**

```dunstify "[title]" "[body]"```

**设置紧急级别**

```dunstify -u [critical] "[message]"```

**设置超时**

```dunstify -t [5000] "[message]"```

**添加动作按钮**

```dunstify -A "[action,label]" "[message]"```

**替换通知**

```dunstify -r [id] "[updated message]"```

**设置图标**

```dunstify -i [icon_name] "[message]"```

**打印通知 ID**，以便日后替换

```dunstify -p "[message]"```

**按 ID 关闭通知**

```dunstify -C [id]```

# SYNOPSIS

**dunstify** [_options_] _summary_ [_body_]

# PARAMETERS

**-u**, **--urgency** _level_
> 紧急级别（low、normal、critical）。

**-t**, **--timeout** _ms_
> 超时时间，单位毫秒。

**-i**, **--icon** _icon_
> 图标名称或路径。

**-r**, **--replace** _id_
> 替换具有该 ID 的通知。

**-A**, **--action** _action,label_
> 添加动作按钮。

**-C**, **--close** _id_
> 按 ID 关闭通知。

**-h**, **--hints** _TYPE:NAME:VALUE_
> 设置一个提示，例如 `int:value:50` 表示进度条。

**-p**, **--printid**
> 打印通知 ID（之后可配合 **-r** 或 **-C** 使用）。

**-a**, **--appname** _name_
> 发送应用的名字。

**-I**, **--raw_icon** _path_
> 以原始图像数据而非名称或路径发送图标。

**-b**, **--block**
> 阻塞直到通知被关闭；退出码反映其关闭方式。

**-c**, **--capabilities**
> 打印通知服务器的能力并退出。

**-s**, **--serverinfo**
> 打印通知服务器信息并退出。

**-v**, **--version**
> 打印版本并退出。

# DESCRIPTION

**dunstify** 是专为 dunst 设计的通知客户端，提供超出标准 notify-send 工具的扩展功能。它实现了 freedesktop.org 通知规范，并带有 dunst 特有的增强。

该工具的关键优势是通知替换：通过保存上一次调用返回的通知 ID（借助 --printid），后续通知可以更新已有通知而不是产生重复项。这对进度指示器、状态更新以及音量/亮度通知至关重要。

其他特性包括点击时可触发命令的动作按钮、用于高级样式定制的自定义提示，以及以编程方式关闭通知的能力。该工具与 dunst 的配置无缝集成，保证外观和行为一致。

# INSTALL

```apt: sudo apt install dunst```

```dnf: sudo dnf install dunst```

```pacman: sudo pacman -S dunst```

```apk: sudo apk add dunstify```

```zypper: sudo zypper install dunst```

```nix: nix profile install nixpkgs#dunst```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dunst](/man/dunst)(1), [dunstctl](/man/dunstctl)(1), [notify-send](/man/notify-send)(1)

# RESOURCES

```[Source code](https://github.com/dunst-project/dunst)```

```[Homepage](https://dunst-project.org/)```

```[Documentation](https://dunst-project.org/documentation/)```

<!-- verified: 2026-07-14 -->
