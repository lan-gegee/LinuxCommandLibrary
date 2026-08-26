# TAGLINE

终端图像拼贴 / 图片目录浏览器

# TLDR

**浏览**目录中的图片

```ucollage [directory]```

**打开**当前目录

```ucollage```

# SYNOPSIS

**ucollage** [*options*] [*path*]

# DESCRIPTION

**ucollage** 在终端内以可导航的拼贴形式展示图片集合（在支持的地方利用终端图形能力）。适合在不离开 Shell 的情况下快速浏览照片目录。

# PARAMETERS

*path*

> 图片所在目录（默认：**.**）。

导航/打开/删除的按键绑定因版本而异——参见 **ucollage --help** 和上游 README。

# CAVEATS

要获得最佳效果，需要支持图像协议的终端（Kitty/iTerm/Sixel 等）。在纯 VT100 终端上体验会打折扣。

# INSTALL

```aur: yay -S ucollage```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[viu](/man/viu)(1), [timg](/man/timg)(1), [ranger](/man/ranger)(1)

# RESOURCES

```[Source code](https://github.com/ckardaris/ucollage)```

<!-- verified: 2026-07-19 -->
