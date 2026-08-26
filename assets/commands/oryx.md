# TAGLINE

面向 ZSA 键盘的网页版键盘配置器

# TLDR

**在浏览器中访问配置器**

```oryx```

# SYNOPSIS

**oryx** [_options_]

# DESCRIPTION

**Oryx** 是 ZSA 键盘（ErgoDox EZ、Moonlander、Voyager）的可视化配置器，构建于开源的 QMK 固件之上。它提供图形界面，用于创建和自定义复杂的键盘布局、管理层以及配置宏。

布局可以导出为 QMK 源代码以供进一步定制，并通过配套的 **Keymapp** 工具刷写到键盘上，后者还提供命令行和脚本集成。

# CAVEATS

仅适用于 ZSA 键盘。高级 QMK 功能可能需要直接编辑源代码，而这会导致无法继续使用图形编辑器。

# HISTORY

**Oryx** 由 **ZSA Technology Labs** 开发。

# INSTALL

```pacman: sudo pacman -S oryx```

<!-- packages: 2026-07-22 -->
