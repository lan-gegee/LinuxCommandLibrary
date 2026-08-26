# TAGLINE

使用 Unicode 字符在终端中显示图片

# TLDR

**在终端中显示图片**

```catimg [image.png]```

**设置自定义宽度**

```catimg -w [80] [image.jpg]```

**双倍分辨率**

```catimg -r 2 [image.png]```

**禁用 24 位色彩**

```catimg -t [image.gif]```

# SYNOPSIS

**catimg** [_options_] _image_

# DESCRIPTION

**catimg** 使用 Unicode 方块字符和 ANSI 颜色代码直接在终端中渲染图片。它支持 JPEG、PNG 和 GIF 格式，动画 GIF 可通过可配置的循环次数播放。

该工具无需外部依赖，并且可以通过 SSH 连接工作，因此适合在远程服务器上预览图片，或在没有图形显示的最小化环境中使用。可以通过宽度、高度和分辨率倍率选项调整图像分辨率，在细节与终端尺寸之间取得平衡。

# PARAMETERS

**-w** _width_
> 显示宽度（默认：终端宽度）

**-r** _factor_
> 分辨率倍率（例如 2 表示两倍）

**-t**
> 禁用 24 位色彩（改用 256 色）

**-H** _height_
> 设置显示高度

**-l** _loops_
> GIF 动画循环次数（0 表示无限）

# INSTALLATION

```
git clone https://github.com/posva/catimg.git
cd catimg
cmake .
sudo make install
```

# SIMILAR TOOLS

**chafa**
> 高级终端图形

**timg**
> 终端图片/视频查看器

**tiv**
> 终端图片查看器

**imcat**
> 将图片输出到终端

# CAVEATS

使用 Unicode 方块字符进行渲染。画质取决于终端字体和颜色支持。在支持 24 位色彩的终端中效果最佳。

# INSTALL

```apt: sudo apt install catimg```

```dnf: sudo dnf install catimg```

```pacman: sudo pacman -S catimg```

```apk: sudo apk add catimg```

```zypper: sudo zypper install catimg```

```brew: brew install catimg```

```nix: nix profile install nixpkgs#catimg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chafa](/man/chafa)(1), [timg](/man/timg)(1), [tiv](/man/tiv)(1)

# RESOURCES

```[Source code](https://github.com/posva/catimg)```

<!-- verified: 2026-06-22 -->
