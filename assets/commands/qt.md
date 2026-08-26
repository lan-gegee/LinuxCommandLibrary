# TAGLINE

跨平台 C++ 应用程序框架工具

# TLDR

**创建 Qt 项目**

```qmake -project```

**生成 Makefile**

```qmake```

**使用 CMake 构建**

```cmake -DCMAKE_PREFIX_PATH=[/path/to/Qt] ..```

**运行 Qt Designer**

```designer```

**运行 Qt Creator**

```qtcreator```

# SYNOPSIS

Qt framework tools and utilities

# TOOLS

**qmake**
> 构建系统生成器。

**moc**
> 元对象编译器（Meta-Object Compiler）。

**uic**
> UI 编译器。

**rcc**
> 资源编译器。

**designer**
> 可视化 UI 设计器。

**qtcreator**
> IDE。

**qmlscene**
> QML 查看器。

# DESCRIPTION

**Qt** 是一个用于 GUI 应用程序的跨平台 C++ 框架，提供控件、图形、网络等功能。此处涵盖主要的 Qt 开发工具。

# EXAMPLES

```bash
# Create project file
qmake -project

# Generate Makefile
qmake myproject.pro

# Build
make

# Run UI designer
designer

# View QML file
qmlscene myapp.qml

# Get Qt version
qmake --version
```

# CMAKE INTEGRATION

```cmake
cmake_minimum_required(VERSION 3.16)
project(myapp)

find_package(Qt6 REQUIRED COMPONENTS Widgets)
qt_standard_project_setup()

qt_add_executable(myapp main.cpp)
target_link_libraries(myapp Qt6::Widgets)
```

# ENVIRONMENT

```bash
# Set Qt path
export PATH=/opt/Qt/6.x/gcc_64/bin:$PATH
export LD_LIBRARY_PATH=/opt/Qt/6.x/gcc_64/lib
```

# CAVEATS

框架庞大。许可协议：GPL、LGPL 或商业授权。Qt5 和 Qt6 的 API 有差异。

# HISTORY

Qt 由 **Trolltech** 于 1991 年创建，后被 **Nokia** 收购，随后归于 **Digia**，现为 **The Qt Company** 所有。

# INSTALL

```dnf: sudo dnf install qt```

```brew: brew install qt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qmake](/man/qmake)(1), [cmake](/man/cmake)(1)
