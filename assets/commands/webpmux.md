# TAGLINE

操作 WebP 元数据和动画

# TLDR

**从动画中提取帧**

```webpmux -get frame [1] [input.webp] -o [frame.webp]```

**获取 ICC 配置文件**

```webpmux -get icc [input.webp] -o [profile.icc]```

**设置 EXIF 元数据**

```webpmux -set exif [metadata.exif] [input.webp] -o [output.webp]```

**用帧创建动画**

```webpmux -frame [1.webp] +[100] -frame [2.webp] +[100] -loop [0] -o [output.webp]```

**显示文件信息**

```webpmux -info [input.webp]```

**移除 EXIF 元数据**

```webpmux -strip exif [input.webp] -o [output.webp]```

**修改动画帧的持续时间**

```webpmux -duration [200] [input.webp] -o [output.webp]```

# SYNOPSIS

**webpmux** [_-get|-set|-strip_] [_options_] _input_ [**-o** _output_]

# PARAMETERS

**-get** _TYPE_
> 提取数据：第 n 帧、icc、exif 或 xmp。

**-set** _TYPE FILE_
> 设置元数据：icc、exif 或 xmp。

**-strip** _TYPE_
> 移除元数据：icc、exif 或 xmp。

**-frame** _FILE+OPTS_
> 为动画添加帧（file +duration[+x+y[+method[blend]]]）。

**-duration** _DURATION[,START[,END]]_
> 以毫秒为单位设置帧持续时间。

**-loop** _COUNT_
> 动画循环次数（0=无限循环，范围 0-65535）。

**-bgcolor** _A,R,G,B_
> 动画画布的背景色（取值 0-255）。

**-info**
> 显示文件信息。

**-o** _FILE_
> 输出文件。

**-version**
> 显示版本号。

# DESCRIPTION

**webpmux** 是 Google libwebp 库中的一个工具，用于在容器层面操作 WebP 图像文件。它可以提取和设置元数据配置文件（ICC 色彩、XMP、EXIF），从动态 WebP 文件中提取单个帧，以及将帧合成为动画。

该工具直接操作 WebP 容器格式而不重新编码图像数据，因此操作快速且无损。可以从文件中剥离元数据以减小体积，也可以添加元数据以纳入色彩管理和描述信息。

对于动态 WebP 文件，可以将单个帧提取为独立的 WebP 图像，并可用 info 命令查看帧时序和循环参数。

# CAVEATS

仅支持 WebP 格式。属于 libwebp-tools 的一部分。每次调用只能执行一个 -strip/-get/-set 操作；要剥离多种元数据类型需要分别执行命令。

# HISTORY

**webpmux** 是 Google 的 **libwebp** 的一部分，提供操作 WebP 图像的工具。

# INSTALL

```apt: sudo apt install webp```

```dnf: sudo dnf install libwebp-tools```

```apk: sudo apk add libwebp-tools```

```zypper: sudo zypper install libwebp-tools```

```brew: brew install webp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cwebp](/man/cwebp)(1), [dwebp](/man/dwebp)(1), [img2webp](/man/img2webp)(1)
