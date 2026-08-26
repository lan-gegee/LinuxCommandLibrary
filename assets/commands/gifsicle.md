# TAGLINE

创建、编辑和优化 GIF 图片与动画

# TLDR

**优化** GIF 以获得更小的文件体积

```gifsicle -O3 [input.gif] -o [output.gif]```

**配合有损压缩进一步缩小**体积

```gifsicle -O3 --lossy=[80] [input.gif] -o [output.gif]```

**调整** GIF 尺寸

```gifsicle --resize [320x240] [input.gif] -o [output.gif]```

**按指定宽度缩放**并保持宽高比

```gifsicle --resize-width [320] [input.gif] -o [output.gif]```

**选取**一段帧范围

```gifsicle [input.gif] '#0-9' -o [frames.gif]```

**将多张图片合并**为无限循环的动画

```gifsicle --delay=[10] --loopcount=forever [frame*.gif] -o [output.gif]```

**更改**动画速度

```gifsicle --delay=[5] [input.gif] -o [faster.gif]```

**减少**颜色数量

```gifsicle --colors [64] [input.gif] -o [output.gif]```

**显示** GIF 的相关信息

```gifsicle --info [input.gif]```

**原地优化**文件

```gifsicle -bO3 [*.gif]```

# SYNOPSIS

**gifsicle** [_options_, _frames_, and _filenames_] ...

# PARAMETERS

**-o**, **--output** _file_
> 将输出写入 _file_。使用 **-** 表示标准输出。

**-O**, **--optimize**[=_level_]
> 优化输出。**1** 只存储每帧发生变化的部分（**-O** 不带级别时的默认值），**2** 额外利用透明度，**3** 会尝试多种方法并选择最优结果，速度较慢。

**--lossy**[=_lossiness_]
> 通过改变颜色来缩小文件，代价是产生伪影。数值越高文件越小、噪点越多。默认 **20**。

**-U**, **--unoptimize**
> 将每一帧展开为完整尺寸的图像。在编辑单个帧之前很有用。

**--resize** _WxH_
> 缩放到精确尺寸。某个维度使用 **_** 可保持宽高比。

**--resize-width** _W_, **--resize-height** _H_
> 按宽度或高度缩放，保持宽高比。

**--resize-fit** _WxH_
> 缩小以适配矩形区域，保持宽高比。若 GIF 已经适配则不做任何操作。

**--resize-fit-width** _W_, **--resize-fit-height** _H_
> 按宽度或高度缩小以适配，保持宽高比。

**--resize-method** _method_
> 重采样方法：**sample**（快速，缩小时有噪点）、**mix**（默认，质量更好）、**box**、**catrom**、**mitchell**、**lanczos2**、**lanczos3**。

**--scale** _Xfactor_[x_Yfactor_]
> 按因子缩放，例如 **0.5** 表示一半大小。_Yfactor_ 默认等于 _Xfactor_。

**--crop** _x1,y1+WxH_, **--crop** _x1,y1-x2,y2_
> 裁剪到指定区域。尺寸为零时延伸到图像边缘；负值则从边缘回退。

**--crop-transparency**
> 裁掉透明边框。

**-d**, **--delay** _time_
> 帧延迟，单位为百分之一秒。

**-l**, **--loopcount**[=_count_]
> 将 Netscape 循环扩展设置为 _count_ 或 **forever**。单独的 **--loopcount** 意味着永远循环。默认是 **--no-loopcount**，即不添加循环扩展。

**-k**, **--colors** _num_
> 将颜色减少到 _num_ 种，取值介于 **2** 和 **256** 之间。

**--color-method** _method_
> 颜色缩减方法：**diversity**（默认，xv 的算法）、**blend-diversity**、**median-cut**（Heckbert 算法）。

**-f**, **--dither**[=_method_]
> 在调色板变化时进行抖动处理。方法包括 **floyd-steinberg**（默认）、**atkinson**、**ordered**、**halftone**、**ro64**、**o3**、**o4**、**o8**。

**--rotate-90**, **--rotate-180**, **--rotate-270**
> 旋转图像。

**--flip-horizontal**, **--flip-vertical**
> 翻转图像。

**-e**, **--explode**
> 将每一帧分别写入名为 _file_**.**_number_ 的文件。

**-m**, **--merge**
> 合并模式：将所有输入合并为一个输出。这是默认模式。

**-b**, **--batch**
> 批量模式：就地修改每个输入文件。

**-I**, **--info**
> 打印输入 GIF 的信息，而不写出输出文件。

**--careful**
> 写出略大一些的 GIF，以规避某些其他 GIF 阅读器的缺陷，尤其是旧版 Java 和 Internet Explorer。

**--conserve-memory**
> 以速度换取更低的内存占用，适用于非常大的 GIF。

**-w**, **--no-warnings**
> 抑制警告消息。

# DESCRIPTION

**gifsicle** 从命令行操作 GIF 图片和动画：它可以将文件合并成动画、把动画拆分为帧、就地编辑单个帧以及减小文件体积，全程无需图形界面。

它的参数是有顺序依赖性的，这是它区别于大多数工具的地方。选项、帧选择和文件名按从左到右的顺序读取，一个选项作用于其后出现的输入文件。帧选择使用附着于文件的 **#** 记法：**'#0'** 是第一帧，**'#0-5'** 是一段范围，**'#-1'** 是最后一帧。记得加引号，因为 **#** 在大多数 Shell 中表示注释的开始。

优化是最受人们青睐的功能。**-O3** 会对每帧尝试多种编码方式并保留最小的一种，由于只存储帧间差异且完全无损，通常能显著压缩未优化的动画。当这还不够时，**--lossy** 允许合并相近颜色以体积换取精确度，而 **--colors** 则直接缩减调色板。

默认情况下 **gifsicle** 以合并模式运行，将所有输入合并为一个用 **-o** 写出的输出。**--batch** 切换为就地编辑每个输入文件，**--explode** 则为每帧写出一个文件。

# CAVEATS

输入必须已经是 GIF。**gifsicle** 不能读取 PNG、JPEG 或视频，因此请先用 **ffmpeg** 或 ImageMagick 的 **convert** 生成 GIF，再在这里进行优化。

由于参数与位置相关，**gifsicle --colors 64 a.gif b.gif** 和 **gifsicle a.gif --colors 64 b.gif** 并不是同一条命令。放在某个文件之后的选项不会追溯作用于该文件。

默认值为 **--no-loopcount**，因此你组装的动画只会播放一次，除非传入 **--loopcount=forever**。另请注意，_count_ 是首次完整播放*之后*的重复次数，所以 **--loopcount=3** 会把动画播放四次。

**-b** 会不加备份地重写原始文件。在对整个目录运行之前，请先在副本上确认结果。

**--lossy** 和 **--colors** 不可逆，反复重新优化已有损的 GIF 会累积伪影。

大型动画可能占用大量内存，尤其是会展开所有帧到全尺寸的 **-U**；**--conserve-memory** 用速度换取内存占用。

# HISTORY

**gifsicle** 由 **Eddie Kohler** 编写，首次发布于 **1997 年**，源自他读研究生期间对 GIF 工具的研究。它成为 GIF 处理和网页优化的标准工具，也是许多"压缩这个 GIF"服务背后的引擎。开发仍在 GitHub 上继续，基于 **giflossy** 分支的工作，**--lossy** 于 **2015 年**加入。

# INSTALL

```apt: sudo apt install gifsicle```

```dnf: sudo dnf install gifsicle```

```pacman: sudo pacman -S gifsicle```

```apk: sudo apk add gifsicle```

```zypper: sudo zypper install gifsicle```

```brew: brew install gifsicle```

```nix: nix profile install nixpkgs#gifsicle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [ffmpeg](/man/ffmpeg)(1), [optipng](/man/optipng)(1), [pngquant](/man/pngquant)(1), [imagemagick](/man/imagemagick)(1)

# RESOURCES

```[Source code](https://github.com/kohler/gifsicle)```

```[Homepage](https://www.lcdf.org/gifsicle/)```

```[Documentation](https://www.lcdf.org/gifsicle/man.html)```

<!-- verified: 2026-07-16 -->
