# TAGLINE

用于按半字节编辑字节的终端十六进制编辑器

# TLDR

**打开文件**

```heh [path/to/file]```

# SYNOPSIS

**heh** [_options_] _file_

# DESCRIPTION

**heh** 是一个跨平台的终端十六进制编辑器，用于在字节级别修改文件数据。它旨在复刻 **hexyl** 的视觉风格，同时在功能上充当 **GHex** 的终端 UI 版本。该编辑器支持在十六进制和 ASCII 两种模式下查看和编辑，编辑粒度可精确到半字节（nibble，即半个字节）。

界面并排显示偏移地址、十六进制值和 ASCII 表示，并按类别对字节进行着色，便于识别不同的数据类型。

# KEY BINDINGS

**h/j/k/l** — 向左/下/上/右移动光标
**i** — 进入插入模式
**Esc** — 返回普通模式
**/** — 搜索
**:w** — 保存
**:q** — 退出
**:wq** — 保存并退出

# CAVEATS

大文件可能会消耗大量内存，因为整个文件都会被加载。编辑器采用类 vim 的按键绑定，可能需要熟悉模态编辑。

# HISTORY

**heh** 由 **ndd7xv** 创建，使用 **Rust** 编写。其设计目标是提供轻量、原生于终端的十六进制编辑体验，同时保持熟悉的视觉布局。

# INSTALL

```pacman: sudo pacman -S heh```

```nix: nix profile install nixpkgs#heh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hexyl](/man/hexyl)(1), [xxd](/man/xxd)(1), [hexdump](/man/hexdump)(1)
