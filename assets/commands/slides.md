# TAGLINE

基于终端的 Markdown 演示工具

# TLDR

从 Markdown 文件**开始演示**

```slides [presentation.md]```

**从指定幻灯片开始**

```slides [presentation.md] --slide [3]```

通过 SSH **提供演示服务**

```slides serve [presentation.md]```

演示期间**执行代码块**

```slides [presentation.md]```
> 在包含代码块的幻灯片上按 **Ctrl+E** 执行它

# SYNOPSIS

**slides** [_options_] [_file_]

**slides** **serve** [_file_]

# PARAMETERS

**--slide** _N_
> 从第 N 张幻灯片开始演示。

**--theme** _theme_
> 为演示使用指定的主题。

**serve**
> 通过 SSH 托管演示，允许远程观看。

# NAVIGATION

**h**, **Left**, **Page Up**, **Backspace**
> 上一张幻灯片。

**l**, **Right**, **Page Down**, **Space**, **Enter**
> 下一张幻灯片。

**g**, **Home**
> 跳到第一张幻灯片。

**G**, **End**
> 跳到最后一张幻灯片。

**1**-**9**
> 跳到第 N 张幻灯片。

**/**
> 搜索幻灯片（支持正则表达式，/i 表示不区分大小写）。

**Ctrl+E**
> 执行当前幻灯片上的代码块。

**q**, **Ctrl+C**
> 退出演示。

# DESCRIPTION

**slides** 是一个基于终端的演示工具，可将 Markdown 文件渲染为幻灯片。在 Markdown 文件中，幻灯片以水平分隔线（**---**）分隔。它支持代码块语法高亮、动态内容和实时代码执行。

该工具会自动监视源文件的变化并实时更新演示，非常适合迭代式地制作演示文稿。演示期间可以直接按 **Ctrl+E** 执行代码块，并在行内显示输出。

slides 还可以使用 **serve** 子命令通过 SSH 提供演示服务，让听众在自己的终端上同步观看。

# CAVEATS

需要支持 ANSI 转义码的终端才能正确渲染。代码执行会在你的本地环境中运行命令，因此对不可信的演示文件要谨慎。演示的呈现效果取决于终端能力和字体支持。

# HISTORY

**slides** 由 Maas Lalani 创建，是一个用 Go 编写的开源终端演示工具。它的设计目标是提供一种简单、无干扰的方式，直接从终端用熟悉的 Markdown 语法进行演示。该项目在偏好终端工作流和现场编程演示的开发者中颇受欢迎。

# INSTALL

```apk: sudo apk add slides```

```brew: brew install slides```

```nix: nix profile install nixpkgs#slides```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdp](/man/mdp)(1), [patat](/man/patat)(1), [presenterm](/man/presenterm)(1), [tpp](/man/tpp)(1)
