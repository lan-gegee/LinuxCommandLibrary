# TAGLINE

将动画 GIF 显示为彩色终端艺术

# TLDR

**在终端中播放** GIF

```gif-for-cli [file.gif]```

**从 URL 播放**（如果支持）

```gif-for-cli "[https://example.com/a.gif]"```

# SYNOPSIS

**gif-for-cli** [*options*] *gif*

# DESCRIPTION

**gif-for-cli**（Google）使用 ANSI/Unicode 块字符渲染 GIF 动画，使短片可以在终端内播放。适用于演示和彩蛋。需要支持颜色的终端；处理管线中使用 **ffmpeg**。

# PARAMETERS

*gif*

> 动画的路径或来源。

显示尺寸和颜色模式相关选项取决于版本——见 **gif-for-cli --help**。

# CAVEATS

性能取决于终端模拟器和 GIF 分辨率。不适合对无障碍性要求高的输出。软件包安装方式各异（pip/源码）。

# INSTALL

```nix: nix profile install nixpkgs#gif-for-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timg](/man/timg)(1), [chafa](/man/chafa)(1), [viu](/man/viu)(1)

# RESOURCES

```[Source code](https://github.com/google/gif-for-cli)```

<!-- verified: 2026-07-19 -->
