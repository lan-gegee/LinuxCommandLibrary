# TAGLINE

现代的自举 Object Pascal 编译器

# TLDR

**编译单个** Pascal 源文件

```blaise --source [Hello.pas] --output [Hello]```

**编译由项目 XML 文件描述的项目**

```blaise --project [project.xml] --output [myapp]```

**以指定的构建配置文件编译**（debug、release 等）

```blaise --project [project.xml] --config [debug] --output [myapp]```

**输出 QBE 中间表示**以供检查

```blaise --source [Hello.pas] --emit-ir```

**显示**版本 / 帮助

```blaise --version```

# SYNOPSIS

**blaise** **--source** _file_ [**--output** _file_] [**--emit-ir**]

**blaise** **--project** _file_ [**--config** _profile_] [**--output** _file_]

# PARAMETERS

**--source** _FILE_
> 编译单个 Pascal 源文件 _FILE_。

**--output** _FILE_
> 输出可执行文件的路径。省略时默认为源文件的主名。

**--project** _FILE_
> 从 _FILE_ 读取构建设置（单元、搜索路径、库、宏定义）——通常是 **project.xml**。

**--config** _PROFILE_
> 选择项目文件中定义的构建配置文件。常见取值为 **debug** 和 **release**。

**--emit-ir**
> 在输出 QBE 中间表示后停止；适合检查代码生成结果。

**--version**
> 打印编译器版本并退出。

**--help**
> 显示用法信息并退出。

# DESCRIPTION

**Blaise** 是一个从零编写的现代自举 **Object Pascal** 编译器，不依赖 Free Pascal 或 Delphi 的源代码。它通过 **QBE** 后端生成原生代码（LLVM 后端正在开发中），并以数学家 **Blaise Pascal（布莱士·帕斯卡）** 命名——最初的 Pascal 语言也是为纪念他而得名的。

Blaise 编译的语言是"2020 年代的 Pascal"：单一语言模式（不再区分 Delphi/Free Pascal/Turbo 方言）、内部使用 **UTF-8** 的单一字符串类型、用**自动引用计数（ARC）**取代手动内存管理、实体化的泛型以及零 GUID 的接口。工具链自带调试格式（**OPDF**），提供一流的调试器支持。

支持两种调用方式。**--source** 以 **fpc hello.pas** 的风格编译单个文件，最适合教程和一次性程序。**--project** 读取结构化的 XML 项目文件，其中描述了单元、搜索路径、库依赖和构建配置文件，这是非小型应用推荐的工作流程。

Blaise 自举自身：发布的二进制文件由上一个版本的编译器编译其自身源码产生，且该项目将**逐字节完全一致的重构建**作为正确性不变量来跟踪。

# CAVEATS

Blaise 是一个年轻且处于积极开发中的编译器——语言和编译器标志可能在版本之间变化。当前后端为 **QBE**，仅支持少量架构（x86_64、arm64、riscv64）；能够扩展架构覆盖面的 LLVM 后端仍在建设中。与 **Delphi** 和 **Free Pascal** 代码的源码兼容性被有意排除在目标之外：来自这些生态的许多程序不经修改无法编译。

# HISTORY

**Blaise** 由 **Graeme Geldenhuys** 创建，是一个白板重来的 Object Pascal 编译器，明确目标是"不带历史包袱"——完整的 ARC、统一的 UTF-8 以及单一语言模式。项目托管于 **github.com/graemeg/blaise**，以开源许可证发布。它延续了可追溯到 **1970 年 Niklaus Wirth** 在苏黎世联邦理工学院编写最初的 Pascal 编译器的悠久传统。

# SEE ALSO
