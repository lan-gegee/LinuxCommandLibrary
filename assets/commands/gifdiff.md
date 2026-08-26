# TAGLINE

检查两张 GIF 图片的显示效果是否相同

# TLDR

**比较两个 GIF 文件**（退出状态 0 = 相同，1 = 不同）

```gifdiff [file1.gif] [file2.gif]```

**简洁模式** —— 仅返回退出状态，无输出

```gifdiff -q [file1.gif] [file2.gif]```

**忽略帧重绘差异**（渲染结果相同但重绘信息不同的帧）

```gifdiff -w [file1.gif] [file2.gif]```

**在 Shell 脚本中使用**

```gifdiff -q [file1.gif] [file2.gif] && echo "identical"```

# SYNOPSIS

**gifdiff** [**-q** | **--brief**] [**-w** | **--ignore-redraw**] _gif1_ _gif2_

# PARAMETERS

**-q**, **--brief**
> 不产生输出；只返回退出状态（图像显示效果相同时为 0，否则为 1）。

**-w**, **--ignore-redraw**
> 忽略仅影响帧重绘方式的差异。两个渲染结果相同但重绘编码方式不同的动画仍被视为相等。

**-h**, **--help**
> 打印用法信息并退出。

**-v**, **--version**
> 打印 gifdiff 版本并退出。

# DESCRIPTION

**gifdiff** 比较两个 GIF 图像文件，判断它们在渲染时的显示效果是否相同。与逐字节比较不同，它会考虑语义上无关紧要的编码差异（例如产生相同可见输出的不同帧处置方法）。

gifdiff 是 **gifsicle** 工具集的一部分，主要用于对 GIF 生成器进行回归测试，以及确认两个不同编码的文件产生相同的动画。

# CAVEATS

gifdiff **不会**生成可视化的差异图像。如需像素级的差异可视化，请使用 ImageMagick 的 **compare(1)** 等工具。

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

[gifsicle](/man/gifsicle)(1), [gifview](/man/gifview)(1), [compare](/man/compare)(1)
