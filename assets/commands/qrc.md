# TAGLINE

面向文本终端的二维码生成器

# TLDR

**从文本生成二维码**

```qrc "[text]"```

**从标准输入生成二维码**

```echo "[text]" | qrc```

# SYNOPSIS

**qrc** [_options_] [_text_]

# DESCRIPTION

**qrc** 是一款二维码生成器，可使用 ASCII 字符画或 Sixel 图形直接在终端输出可扫描的二维码。它接受来自命令行参数或标准输入的文本，并支持二维码反色、边距调整以及前景色/背景色自定义等选项。

# HISTORY

**qrc** 由 **SATOH Fumiyasu**（fumiyas）创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S qrc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qrtool](/man/qrtool)(1), [qrencode](/man/qrencode)(1)
