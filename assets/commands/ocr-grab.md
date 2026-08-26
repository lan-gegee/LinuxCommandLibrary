# TAGLINE

X11 区域截图工具，即时调用 Tesseract OCR 并复制到剪贴板（类似 Flameshot）

# TLDR

**启动**选择器并将所选区域 OCR 到剪贴板

```ocr-grab```

从源码**构建**

```make```

# SYNOPSIS

**ocr-grab**

# DESCRIPTION

OCR Grab 是一款轻量级的 C/GTK3 + Tesseract 工具，适用于 X11。它可以交互式地选择屏幕区域（带调整模式），并立即对选区运行 OCR，将提取出的文本复制到剪贴板（在精简窗口管理器上可通过 xclip 兜底）。

它的定位是在目标是捕获文本而非图像时，作为 Flameshot 式工作流的快速、键盘驱动的补充或替代方案。除了启动交互式选择器外没有任何 CLI 标志。

# USAGE

1. 将 `ocr-grab` 绑定到快捷键（例如 i3 中 Mod+Print）。
2. 拖拽选择区域。
3. 如有需要可用鼠标调整（边缘、角点或整体移动）。
4. 按 Enter 进行 OCR 并复制，或按 Escape 取消。

弹窗会显示结果；"Copy & Close" 会将其同时放入主剪贴板和选择剪贴板。

# DEPENDENCIES

构建需要 gtk+-3.0、tesseract、leptonica、zbar 和 x11 的开发头文件，还需要 C 编译器和 make。运行时需要语言数据（如 `tesseract-ocr-eng`）；在精简窗口管理器上可选安装 `xclip`。

# CAVEATS

- 仅限 X11（未提及原生 Wayland 支持）。
- 需要 tesseract 语言数据（例如 tesseract-ocr-eng）。
- 采用 GPL-3.0 许可证。

# SEE ALSO

[flameshot](/man/flameshot)(1), [tesseract](/man/tesseract)(1), [xclip](/man/xclip)(1)

# RESOURCES

```[Source code](https://github.com/talalalrwas/ocr-grab)```

```[Documentation](https://github.com/talalalrwas/ocr-grab#readme)```

<!-- verified: 2026-07-11 -->
