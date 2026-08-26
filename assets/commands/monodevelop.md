# TAGLINE

面向 .NET、Mono、C# 和 F# 的跨平台 IDE

# TLDR

**启动 MonoDevelop**

```monodevelop```

**打开解决方案文件**

```monodevelop [solution.sln]```

**打开项目文件**

```monodevelop [project.csproj]```

**在新窗口中打开**

```monodevelop --newwindow [solution.sln]```

**跳过启动画面**

```monodevelop --nologo```

# SYNOPSIS

**monodevelop** [_options_] [_files_...]

# PARAMETERS

**--newwindow**
> 在新窗口中打开给定文件或解决方案，而不是聚焦已有窗口。

**--nologo**
> 启动时跳过启动画面。

**--ipc-tcp**
> 使用 TCP 套接字进行进程间通信（在 Unix 套接字不可用时有用）。

**--perf-log**
> 启用性能日志以便诊断。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示用法信息。

# DESCRIPTION

**monodevelop** 是面向 .NET 和 Mono 的跨平台集成开发环境。它通过插件支持 C#、F#、Visual Basic 及多种其他语言。特性包括代码补全（相当于 IntelliSense）、集成调试器、版本控制集成（Git、Subversion）、重构、NuGet 支持，以及与 Microsoft Visual Studio 兼容的项目/解决方案模型。

在 macOS 上，同一套代码以 **Visual Studio for Mac** 的名义发行。Linux 发行版通常将其打包为 **monodevelop**。

# CAVEATS

MonoDevelop 的开发已明显放缓；**Visual Studio for Mac** 已于 **2024 年 8 月**被微软停止维护，Linux/macOS 上活跃的 .NET 开发大多已转向带 C# 扩展的 **Visual Studio Code** 或 **JetBrains Rider**。较新的 .NET SDK 可能得不到完整支持。

# HISTORY

MonoDevelop 始于约 **2003 年**，最初是把 **SharpDevelop** 移植到 Mono 平台的项目，由 Ximian/Novell 的 Mono 团队主导。**2016 年** Xamarin 被收购后，它演变为微软的 **Visual Studio for Mac**。微软于 **2024 年 8 月 31 日**退役了 Visual Studio for Mac。

# SEE ALSO

[dotnet](/man/dotnet)(1), [msbuild](/man/msbuild)(1), [code](/man/code)(1)
