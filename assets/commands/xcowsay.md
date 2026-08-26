# TAGLINE

在桌面上以图形方式显示奶牛消息

# TLDR

显示带**消息**的奶牛

```xcowsay "[hello, world]"```

通过**管道**输入显示

```ls | xcowsay```

在指定**位置**显示

```xcowsay --at [X],[Y]```

改变奶牛**大小**

```xcowsay --cow-size [small|med|large]```

显示**思想**气泡

```xcowsay --think```

使用自定义**图片**

```xcowsay --image [path/to/file]```

# SYNOPSIS

**xcowsay** [_OPTIONS_] [_MESSAGE_]

# PARAMETERS

**--at** _X,Y_
> 在指定的坐标处显示

**--cow-size** _SIZE_
> 奶牛大小：small、med 或 large

**--think**
> 使用思想气泡而不是对话气泡

**--image** _FILE_
> 使用自定义图片代替奶牛

**--time** _SECONDS_
> 显示时长

# DESCRIPTION

**xcowsay** 在 Linux 桌面上显示一只带有消息的可爱奶牛。与 cowsay 类似，但采用图形化显示。奶牛会在超时后或被点击时消失。

消息可以作为参数提供，也可以从其他命令管道传入。

# CAVEATS

仅支持 X11。除非另行指定，显示时长取决于消息长度。自定义图片必须为 PNG 格式。

# INSTALL

```dnf: sudo dnf install xcowsay```

```zypper: sudo zypper install xcowsay```

```nix: nix profile install nixpkgs#xcowsay```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cowsay](/man/cowsay)(1), [notify-send](/man/notify-send)(1)
