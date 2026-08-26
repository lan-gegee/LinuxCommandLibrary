# TAGLINE

为 Qt 项目生成构建文件

# TLDR

**从 .pro 文件生成 Makefile**

```qmake [project.pro]```

**为 debug 构建生成**

```qmake CONFIG+=debug [project.pro]```

**为 release 构建生成**

```qmake CONFIG+=release [project.pro]```

**生成 Xcode 项目**

```qmake -spec macx-xcode [project.pro]```

**生成 Visual Studio 项目**

```qmake -spec win32-msvc [project.pro] -tp vc```

**创建新的 .pro 文件**

```qmake -project```

**显示 Qt 配置**

```qmake -query```

# SYNOPSIS

**qmake** [_-o makefile_] [_-spec spec_] [_CONFIG+=options_] [_options_] [_project.pro_]

# PARAMETERS

**-o** _file_
> 将输出写入指定文件。未指定时，qmake 会自行选择合适的名称。

**-spec** _spec_
> 使用 spec 作为平台和编译器信息的路径，覆盖 QMAKESPEC。

**-makefile**
> 生成 Makefile（默认模式）。

**-project**
> 根据当前目录中的源文件生成 .pro 项目文件。

**-tp** _type_
> 目标项目类型（如 vc 表示 Visual Studio）。

**-query** [_var_]
> 查询 Qt 配置变量。不带 var 时列出所有值。

**-set** _var_ _value_
> 设置一个持久的 Qt 配置变量。

**-unset** _var_
> 取消一个持久的 Qt 配置变量。

**CONFIG+=**_value_
> 添加配置选项（如 debug、release、static）。

**-r**, **--recursive**
> 递归处理子目录。

**-after**
> 在项目文件之后处理命令行赋值。

**-early**
> 在项目文件之前处理命令行赋值。

**-t** _template_
> 覆盖 TEMPLATE 变量。

**-d**
> 启用调试输出。多个 -d 标志会增加详细程度。

**-v**
> 显示版本信息。

**-Wall**, **-Wnone**, **-Wparser**, **-Wlogic**
> 控制 qmake 的警告级别。

**-cache** _FILE_, **-nocache**
> 使用替代的 **.qmake.cache** 文件或完全跳过它。

**-nodepend**
> 禁用自动依赖关系生成。

**-help**
> 显示帮助信息（规范写法是单横线形式）。

# DESCRIPTION

**qmake** 为 Qt 项目生成构建系统文件。它读取 .pro 项目文件并生成 Makefile 或 IDE 项目文件。

项目文件（.pro）声明源文件、头文件、库和构建选项。qmake 的语法是声明式的，比手写 Makefile 更简单。

配置选项控制构建类型、特性和平台细节。debug 和 release 构建使用不同的编译器标志。

平台规格对应不同的构建系统。每个平台都有 makespec 文件，定义编译器、链接器和平台设置。

IDE 集成可以生成本地项目文件：macOS 上的 Xcode 项目，Windows 上的 Visual Studio 解决方案。

Qt 模块通过 QT 变量链接。Network、SQL、widgets 等模块按需添加。

# CAVEATS

新的 Qt6 项目正在改用 CMake。建议使用 shadow build 以保持源代码树整洁。部分特性是平台相关的。

# HISTORY

自上世纪 **90 年代末**以来，**qmake** 一直是 Qt 的构建系统，由 Trolltech（现 The Qt Company）开发。虽然 CMake 已成为 Qt 6 的主要构建系统，但 qmake 仍受支持并被现有项目广泛使用。

# INSTALL

```apt: sudo apt install qtchooser```

```dnf: sudo dnf install qtchooser```

```apk: sudo apk add qt5-qtbase-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmake](/man/cmake)(1), [make](/man/make)(1), [qt](/man/qt)(1), [moc](/man/moc)(1)
