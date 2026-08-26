# TAGLINE

功能强大的剪贴板管理器

# TLDR

**在系统托盘启动 CopyQ**

```copyq```

**显示剪贴板历史**窗口

```copyq show```

**复制文本**到剪贴板

```copyq copy "[text to copy]"```

**粘贴剪贴板**内容

```copyq paste```

**读取当前剪贴板**内容

```copyq clipboard```

**读取指定下标的条目**（0 为最新）

```copyq read [0]```

**向剪贴板历史添加文本**

```copyq add "[text to add]"```

按下标**从历史中选择条目**

```copyq select [5]```

# SYNOPSIS

**copyq** [_command_] [_arguments_]

# PARAMETERS

**show**
> 显示主剪贴板历史窗口。

**hide**
> 隐藏主窗口。

**toggle**
> 切换主窗口的可见性。

**copy** _TEXT_
> 复制文本到剪贴板。

**paste**
> 粘贴当前剪贴板内容。

**clipboard**
> 打印当前剪贴板内容。

**read** _INDEX_
> 读取指定下标处的剪贴板历史条目。

**add** _TEXT_
> 向剪贴板历史添加文本。

**select** _INDEX_
> 将指定下标处的条目复制到剪贴板。

**remove** _INDEX_
> 从历史中移除指定下标处的条目。

**count**
> 打印剪贴板历史中的条目数量。

**exit**
> 退出 CopyQ。

# DESCRIPTION

**CopyQ** 是一个具备编辑和脚本功能的高级剪贴板管理器。它会监控系统剪贴板，保存可搜索的已复制内容历史，支持文本、图像和其他数据类型。

该应用既提供用于浏览历史的图形界面，也提供强大的命令行接口，可用于脚本化剪贴板操作。条目可以按标签页组织、打标签并进行过滤。还可以根据剪贴板内容触发自定义命令和脚本。

CopyQ 支持跨设备同步、加密存储，并可通过其脚本 API 进行大量定制。它与系统快捷键集成，方便快速访问剪贴板历史和执行粘贴操作。

# CAVEATS

运行多个实例可能引发冲突。部分 Wayland 合成器对剪贴板管理器的支持有限。密码等敏感数据可能会被存入历史，除非用规则将其排除。命令行界面必须在图形界面运行时才能工作。

# HISTORY

CopyQ 作为一个开源剪贴板管理器诞生，首次发布于约 **2009** 年。它逐步加入了脚本、同步和标签页组织等高级特性，成为 Linux、Windows 和 macOS 平台上功能最丰富的剪贴板管理器之一。

# INSTALL

```apt: sudo apt install copyq```

```dnf: sudo dnf install copyq```

```pacman: sudo pacman -S copyq```

```nix: nix profile install nixpkgs#copyq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xclip](/man/xclip)(1), [xsel](/man/xsel)(1), [wl-copy](/man/wl-copy)(1), [pbcopy](/man/pbcopy)(1)

# RESOURCES

```[Source code](https://github.com/hluk/CopyQ)```

```[Homepage](https://hluk.github.io/CopyQ/)```

```[Documentation](https://copyq.readthedocs.io/)```

<!-- verified: 2026-06-23 -->
