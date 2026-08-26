# TAGLINE

ndiswrapper 内核模块的用户态 NDIS 驱动加载器（版本 1.9）

# TLDR

这是 ndiswrapper 内核模块使用的内部支持工具，不应由用户直接调用。请改用 **ndiswrapper** 管理 NDIS 驱动。

**改用 ndiswrapper 安装 Windows 驱动**

```sudo ndiswrapper -i [path/to/driver.inf]```

**列出已安装的 NDIS 驱动**

```ndiswrapper -l```

# SYNOPSIS

**loadndisdriver-1.9**

# DESCRIPTION

**loadndisdriver-1.9** 是 **ndiswrapper** Linux 内核模块的特定版本支持程序。ndiswrapper 内核模块使用它来加载通过 **ndiswrapper**(8) 工具安装的 Windows NDIS 驱动。

该工具不应直接使用。其选项属于内部实现，随时可能变化。它期望在 **/etc/ndiswrapper** 目录中找到 NDIS 驱动文件。

# CAVEATS

并非为直接使用而设计。ndiswrapper 这种无线网络方案已在很大程度上被弃用，原生 Linux 驱动是更好的选择。

# SEE ALSO

[loadndisdriver](/man/loadndisdriver)(8), [ndiswrapper](/man/ndiswrapper)(8), [ndiswrapper-1.9](/man/ndiswrapper-1.9)(8)
