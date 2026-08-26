# TAGLINE

可配置的终端十六进制查看与编辑工具

# TLDR

**在十六进制编辑器中打开文件**

```hexhog [path/to/file]```

**通过 cargo 安装 hexhog**

```cargo install hexhog```

# SYNOPSIS

**hexhog** [_file_]

# DESCRIPTION

**hexhog** 是一个用 Rust 编写、面向终端的可配置十六进制查看与编辑工具。它提供十六进制编辑功能，包括编辑、删除和插入字节，以及选择和复制/粘贴字节区间。界面以可自定义的布局显示偏移地址、十六进制值和 ASCII 表示。

与模态编辑器不同，hexhog 力求尽可能直观。颜色主题和按键绑定均可配置。空字节、可打印 ASCII、空白字符和扩展字符等字节类型会以不同颜色显示。它适合处理二进制数据的程序员、逆向工程师或取证分析人员使用。

# CAVEATS

主要针对较小的二进制文件设计。非常大的文件可能影响性能和内存占用。

# HISTORY

**hexhog** 由 **DVDTSB** 创建，为终端中的十六进制编辑提供了一种简单、可配置的方式。源代码托管在 GitHub 的 **github.com/DVDTSB/hexhog**。

# INSTALL

```brew: brew install hexhog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hexyl](/man/hexyl)(1), [xxd](/man/xxd)(1), [heh](/man/heh)(1)
