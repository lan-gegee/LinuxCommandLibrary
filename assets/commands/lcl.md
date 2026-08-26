# TAGLINE

原生 CLI，可离线访问数千条 Linux 命令参考资料

# TLDR

**启动交互模式**，浏览命令、基础知识和技巧

```lcl```

显示特定命令的**详情**

```lcl [grep]```

**列出库中所有可用命令**

```lcl --list```

显示**版本**信息

```lcl --version```

将列表输出通过管道传给 grep 来**查找命令**

```lcl --list | grep [network]```

# SYNOPSIS

**lcl** [_command_]

**lcl** [**--list** | **-l**]

**lcl** [**--version** | **-v**]

**lcl** [**--help** | **-h**]

# PARAMETERS

**command**
> 要直接显示的 Linux 命令名称。若找到完全匹配项，则显示该命令的详情；若存在多个部分匹配项，则列出它们供选择。

**-l**, **--list**
> 列出库中所有可用的命令。适合通过管道传给 grep 等其他工具。

**-v**, **--version**
> 显示 Linux Command Library 的当前版本。

**-h**, **--help**
> 显示帮助信息及用法示例。

# DESCRIPTION

**lcl**（Linux Command Library）是一个原生 CLI 应用，提供超过 **6200 条 Linux 命令** man page、**23+ 个基础分类**以及通用终端技巧的离线访问。它是一个基于终端的交互式 Unix 和 Linux 命令参考工具。

该应用有两种运行模式：不带参数运行时进入**交互模式**，呈现一个可导航的 TUI（终端用户界面），包含命令、基础知识和技巧菜单；给定命令名参数时进入**直接模式**，立即显示该命令的文档。

在交互模式下，界面同时支持方向键导航和 vim 风格按键绑定（**j/k** 表示向下/向上）。搜索屏幕支持输入字符进行实时过滤。所有内容都打包在二进制文件内，无需联网。

# INTERACTIVE CONTROLS

**Arrow Up / k**
> 向上移动选择

**Arrow Down / j**
> 向下移动选择

**Enter**
> 选择当前项

**Escape / q**
> 返回或退出

**Page Up / Page Down**
> 按页滚动

**Home / End**
> 跳转到列表开头或结尾

**Type characters**
> 在搜索屏幕中过滤命令

# CAVEATS

TUI 需要支持 ANSI 转义序列的终端。在 Windows 上，原始模式输入支持有限，会退回到按行输入。某些终端模拟器若缺乏正确的转义序列处理，可能无法正确渲染界面。

# HISTORY

Linux Command Library 最初是发布在 Google Play 商店和 F-Droid 上的一个 **Android 应用**，之后扩展到 **iOS**、**桌面端**（通过 Compose Multiplatform）和 **Web**。原生 CLI 版本于 **2025 年**推出，采用 **Kotlin/Native** 并使用 Mordant 库进行终端渲染，是一个轻量级的离线参考工具，可直接在终端中运行而无需 JVM。该项目维护的命令文档来自官方 man page 和 tldr-pages 社区项目。

# SEE ALSO

[man](/man/man)(1), [tldr](/man/tldr)(1), [cheat](/man/cheat)(1), [apropos](/man/apropos)(1)
