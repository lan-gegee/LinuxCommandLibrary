# TAGLINE

显示 JPEG XL 图像文件的信息

# TLDR

**显示码流头部信息**（针对 JPEG XL 文件）

```jxlinfo [path/to/image.jxl]```

**详细输出**，包含比特流的完整细节

```jxlinfo -v [path/to/image.jxl]```

单次调用**检查多个文件**

```jxlinfo [image1.jxl] [image2.jxl] [image3.jxl]```

**显示帮助**后退出

```jxlinfo -h```

# SYNOPSIS

**jxlinfo** [_-v_] [_-h_] _INPUT_

# PARAMETERS

**-v**, **--verbose**
> 输出更详细的信息，包括比特流和帧的详细内容。

**-h**, **--help**, **-?**
> 显示列出所有可用选项的帮助信息并退出。

**_INPUT_**
> 一个或多个要检查的输入 JPEG XL 图像文件名。

# DESCRIPTION

**jxlinfo** 通过解析码流头部来打印 JPEG XL（**.jxl**）图像文件的信息，无需完整解码。它会报告图像尺寸、位深、色彩编码（包括是否存在 ICC 配置文件）、动画属性以及容器 box 结构。

该工具是 **libjxl-tools** 的一部分，后者是 JPEG XL Project 维护的 JPEG XL 参考实现发行版。它常用于验证文件是否为有效的 JPEG XL 码流、在解码前检查编码参数以及调试编码器输出。

在详细模式下，**jxlinfo** 会打印帧头部、额外通道、动画时序和强度目标等附加信息。非详细模式适合脚本化场景中需要简要摘要的情况。

# CAVEATS

输出格式在不同版本的 libjxl 之间不稳定，依赖精确字段名的脚本不应解析它。该工具只检查码流头部；不会验证文件能否无错解码。如需完整解码，请使用 **djxl**(1)。

# HISTORY

**jxlinfo** 随 **libjxl** 一起发布。libjxl 是由 **JPEG XL Project** 以及来自 Google、Cloudinary 等公司的贡献者开发的 JPEG XL 图像编码系统参考实现。JPEG XL 自 **2021** 年起被标准化为 **ISO/IEC 18181**。该工具在 Debian、Ubuntu、Fedora 及其他发行版中打包为 **libjxl-tools**。

# INSTALL

```apt: sudo apt install libjxl-tools```

```apk: sudo apk add libjxl-tools```

```zypper: sudo zypper install libjxl-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[djxl](/man/djxl)(1), [cjxl](/man/cjxl)(1), [identify](/man/identify)(1), [exiftool](/man/exiftool)(1)
