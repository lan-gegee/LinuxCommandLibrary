# TAGLINE

在终端中交互式查找并恢复被删除或被覆盖的文件

# TLDR

**启动恢复 TUI**

```sudo recoverpy```

**通过 pip 安装**

```pip install recoverpy```

**不安装直接用 pipx 运行**

```sudo pipx run recoverpy```

# SYNOPSIS

**recoverpy** [_options_]

# DESCRIPTION

**recoverpy** 是一款用于交互式恢复被删除或被覆盖文件的 TUI（文本用户界面）工具。它直接扫描分区原始数据，在整个块设备上搜索字节模式。与其他恢复工具不同，通过扫描所选分区上的每个块，它既能恢复被删除的文件，也能恢复被覆盖的数据。

启动后，recoverpy 首先显示分区选择器，然后提示输入搜索字符串。它会扫描设备上的每个块并以交互方式显示匹配结果，让你可以浏览相邻的块并保存恢复出的内容。

# CAVEATS

访问块设备需要 **sudo** 或 root 权限。它不会自动重建文件或推断文件边界——结果可能是不完整或碎片化的。如果块已被覆盖，则无法恢复。在 ext4 和其他 Linux 原生文件系统上效果最佳。搜索是在原始块上进行的，因此扫描大分区可能耗时较长。

# HISTORY

**recoverpy** 由 **PabloLec** 创建，使用 **Python** 和 **Textual** TUI 框架编写。

# INSTALL

```brew: brew install recoverpy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[testdisk](/man/testdisk)(1), [photorec](/man/photorec)(1), [ddrescue](/man/ddrescue)(1), [foremost](/man/foremost)(1), [extundelete](/man/extundelete)(1)
