# TAGLINE

Qt 集成开发环境

# TLDR

**启动 Qt Creator**

```qtcreator```

**打开项目**

```qtcreator [project.pro]```

**打开 CMake 项目**

```qtcreator [CMakeLists.txt]```

**打开文件**

```qtcreator [file.cpp]```

**定位到指定行打开**

```qtcreator [file.cpp:42]```

**以干净的设置启动**

```qtcreator -noload all```

**客户端模式**（在已运行的实例中打开）

```qtcreator -client [file.cpp]```

# SYNOPSIS

**qtcreator** [_-client_] [_-noload plugins_] [_options_] [_files_]

# PARAMETERS

**-client**
> 在已运行的实例中打开。

**-noload** _PLUGINS_
> 不加载插件。

**-load** _PLUGINS_
> 仅加载指定的插件。

**-settingspath** _PATH_
> 设置目录。

**-pid** _PID_
> 附加到进程。

**-lastsession**
> 恢复上一次会话。

**-block**
> 阻塞直到文件关闭。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**qtcreator** 是 Qt 官方的集成开发环境。它为 Qt 和 C++ 项目提供编辑、调试、性能分析和部署功能。

该 IDE 支持 Qt 项目（qmake、CMake）、纯 CMake 以及其他构建系统。项目向导可以创建新的应用程序、库和插件。

代码编辑功能包括语法高亮、补全、重构以及基于 clang 的代码模型。编辑器能够理解 Qt 特有的语法结构。

调试集成了 GDB、LLDB 和 CDB。可视化调试能正确显示 Qt 类型。QML 调试可处理 JavaScript 和 UI 元素。

性能分析工具用于分析 CPU 使用率、内存分配和 QML 性能，帮助优化应用程序性能。

部署配置面向桌面、嵌入式、Android、iOS 等平台。交叉编译工具链可自由配置。

# CAVEATS

大型项目下资源占用较高。初次加载项目可能较慢。部分功能需要 Qt 商业许可。

# HISTORY

**Qt Creator** 由 **Nokia**（当时的 Qt 所有者）于 **2008 年**发布。它将 Qt 开发工具整合为一个现代 IDE。目前由 **The Qt Company** 持续开发。

# INSTALL

```apt: sudo apt install qtcreator```

```pacman: sudo pacman -S qtcreator```

```nix: nix profile install nixpkgs#qtcreator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qmake](/man/qmake)(1), [cmake](/man/cmake)(1), [gdb](/man/gdb)(1), [clang](/man/clang)(1)
