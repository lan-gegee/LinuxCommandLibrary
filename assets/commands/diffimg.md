# TAGLINE

计算两张输入图像之间逐像素的差异图像

# TLDR

**计算**两幅图像的差异并保存

```diffimg [image1.png] [image2.png] [diff.png]```

**将其用于视觉回归测试**

```diffimg [expected.png] [actual.png] [report/diff.png]```

# SYNOPSIS

**diffimg** _image1_ _image2_ _output_

# DESCRIPTION

**diffimg** 计算两张尺寸相同的图像之间的逐像素差异，并将结果写入第三个文件。每个输出像素编码两个输入对应像素之间的差值——相同区域显示为黑色，变化区域则会亮起。这使它成为视觉回归检查、前后对比和 QA 流程中的便捷工具。

具体实现各不相同——有的是 Python/PIL 封装，有的是带 CLI 前端的基于 Qt 的 GUI，还有的是 Go/Rust 重写版本。但它们都遵循相同的基本三参数签名，并且都支持 PNG、JPEG 和 GIF 输入。

# PARAMETERS

_image1_
> 第一张输入图像。

_image2_
> 第二张输入图像。必须与 _image1_ 尺寸相同。

_output_
> 差异图像的写入路径。扩展名决定输出格式。

# SUPPORTED FORMATS

PNG、JPEG、GIF，以及（在底层可用 ImageMagick 时）PostScript 和 TIFF。

# CAVEATS

两张图像必须尺寸相同；如果不同，请先调整大小或裁剪。输出反映的是原始像素差值，而非感知差异——1 像素的位移会让每条边缘都亮起。若要进行感知或结构性比较，请使用 **compare**（ImageMagick）配合 `-metric SSIM`，或使用 `pixelmatch`、`odiff`、`perceptualdiff` 等专用工具。

还存在其他同样名为 `diffimg` 的工具——可通过 `diffimg --version` 或软件包描述确认你使用的是哪一个。

# HISTORY

自 21 世纪初以来，出现过多个名为 **diffimg** 的工具。打包最广泛的是 **Jonathan Zurflueh (thebulb)** 编写的 Python CLI/GUI 版本。其他实现包括基于 Qt 的桌面 GUI 以及 Go/Rust 重写版本。

# INSTALL

```apt: sudo apt install graphviz```

```dnf: sudo dnf install graphviz```

```pacman: sudo pacman -S graphviz```

```apk: sudo apk add graphviz```

```zypper: sudo zypper install graphviz```

```brew: brew install graphviz```

```nix: nix profile install nixpkgs#graphviz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[compare](/man/compare)(1), [diff](/man/diff)(1), [convert](/man/convert)(1)
