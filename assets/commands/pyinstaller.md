# TAGLINE

将 Python 应用打包为独立的可执行文件

# TLDR

**从脚本构建单文件夹包**（生成 **dist/myscript/**）

```pyinstaller [path/to/myscript.py]```

**构建不依赖外部资源的单文件可执行程序**

```pyinstaller --onefile [path/to/myscript.py]```

**构建无控制台窗口的 GUI 应用**（Windows/macOS）

```pyinstaller --windowed --onefile [path/to/app.py]```

**为打包的可执行文件设置自定义名称与图标**

```pyinstaller --name [MyApp] --icon [path/to/icon.ico] [path/to/app.py]```

**在脚本之外附加数据文件**（Windows 上用 **;**）

```pyinstaller --add-data "[path/to/data.json]:[data]" [path/to/app.py]```

**强制包含静态分析遗漏的模块**

```pyinstaller --hidden-import [package.module] [path/to/app.py]```

**根据已保存的 spec 文件重新构建**（可重复构建的首选方式）

```pyinstaller [path/to/myscript.spec]```

**清理缓存**并不再提示直接覆盖上一次输出

```pyinstaller --clean --noconfirm --onefile [path/to/app.py]```

# SYNOPSIS

**pyinstaller** [_options_] _script_ [_script_ ...] | _specfile_

# DESCRIPTION

**pyinstaller** 将 Python 程序连同其解释器和所有导入的模块一起打包成自包含的 bundle，可在未安装 Python 的机器上运行。它的工作原理是从入口脚本开始追踪导入，把得到的模块集合、共享库和数据文件复制到构建目录，最终生成单文件夹布局（**--onedir**，默认）或单个可执行文件（**--onefile**，运行时自解压到临时目录）。

构建分两个阶段进行。首先，PyInstaller 写出一个 **_脚本_.spec** 文件，记录脚本的路径、选项和分析器提示。其次，它处理这个 spec 文件并在 **dist/** 中组装出实际的 bundle。对于非平凡的项目，推荐直接编辑 spec 文件，因为 spec 就是纯 Python 文件，可以控制钩子、二进制文件、数据目录树以及 CLI 标志无法完全表达的运行时选项。

PyInstaller 跨平台但不支持交叉编译：在 Linux 上构建的 bundle 只能运行于 Linux，Windows bundle 必须在 Windows 上构建，macOS 同理。它支持 CPython 3.8 及更高版本，并为数百个流行软件包（NumPy、PyQt、Django、TensorFlow）内置了钩子，使其开箱即用地正确打包。

# PARAMETERS

**-F**, **--onefile**

> 生成单个可执行文件。启动时二进制会自解压到临时目录并从那里运行。

**-D**, **--onedir**

> 生成一个包含可执行文件及其依赖的文件夹。这是默认模式，启动也最快。

**-n** _NAME_, **--name** _NAME_

> 为打包的应用及生成的 **.spec** 文件指定名称。默认取脚本的基本名。

**-w**, **--windowed**, **--noconsole**

> 在 Windows 和 macOS 上不附加控制台窗口。适用于 GUI 应用。

**-c**, **--console**, **--nowindowed**

> 强制使用控制台窗口（多数平台上的默认行为）。

**--icon** _FILE_

> 应用自定义图标：Windows 用 **.ico**，macOS 用 **.icns**。用 **NONE** 可取消默认图标。

**--add-data** _SOURCE_**:**_DEST_

> 将额外的数据文件或目录打包到 bundle 内的 _DEST_ 下。在 Windows 上请用 **;** 代替 **:** 作为分隔符。

**--add-binary** _SOURCE_**:**_DEST_

> 与 **--add-data** 相同，但用于需要按二进制处理的共享库。

**--hidden-import** _MODULE_

> 即使静态分析无法看到导入也强制包含某模块（插件系统或动态导入的典型需求）。

**-p** _DIR_, **--paths** _DIR_

> 将 _DIR_ 加入模块搜索路径的前部，相当于仅为分析阶段添加 **PYTHONPATH**。

**--clean**

> 开始前清空 PyInstaller 的缓存和临时构建产物。

**-y**, **--noconfirm**

> 不询问确认直接替换输出目录。

**--log-level** _LEVEL_

> 设置日志级别：**TRACE**、**DEBUG**、**INFO**（默认）、**WARN**、**ERROR**、**FATAL**。

**--specpath** _DIR_

> 将生成的 **.spec** 文件放在 _DIR_ 而非当前目录。

**--distpath** _DIR_, **--workpath** _DIR_

> 覆盖 **dist/** 和 **build/** 输出目录。

**--upx-dir** _DIR_

> 使用 _DIR_ 中的 UPX 可执行文件压缩器来压缩打包的二进制文件。

# SPEC FILE WORKFLOW

首次运行会生成 **myscript.spec**——一个描述 **Analysis**、**PYZ**、**EXE** 和 **COLLECT** 步骤的 Python 文件。只要不是简单脚本，就应编辑 spec 来添加数据文件、运行时钩子、版本信息或启动画面，然后用以下命令重建：

```
pyinstaller myscript.spec
```

当以 spec 文件调用 PyInstaller 时，大多数 CLI 选项都不起作用：spec 文件具有最高优先级。

# CAVEATS

**不支持交叉编译。** 请在目标操作系统（最好是其最老的受支持版本）上进行构建，以最大化兼容性。

**杀毒软件误报**在使用 **--onefile** 的 Windows 二进制时很常见，因为自解压 stub 模式与恶意软件加壳器相似。对可执行文件做代码签名通常可以解决此问题。

**动态导入会破坏分析。** 通过 **importlib**、**\_\_import\_\_** 或基于字符串发现机制加载的插件必须用 **--hidden-import** 或自定义钩子声明，否则运行时会缺失。

**--onefile 启动更慢**，因为每次运行都要自解压到临时目录。对延迟敏感的应用建议使用 **--onedir**。

**打包产物体积较大。** 一个最小的 "hello world" 也会产生数十兆字节的二进制文件，因为嵌入了整个 CPython 运行时。可用 **--exclude-module** 排除未使用的标准库模块。

# HISTORY

**PyInstaller** 于 2005 年作为 Gordon McMillan 的 **Installer** 项目的一个分支起步，目标是让单一代码库产出可在 Linux、Windows 和 macOS 上运行的便携 Python 可执行程序。2.x 和 3.x 系列巩固了各平台支持并引入 spec 文件工作流；**PyInstaller 4**（2020 年）放弃 Python 2；**PyInstaller 5**（2022 年）重构了 bootloader 处理；**PyInstaller 6**（2023 年）为 **--add-data** 引入 **SOURCE:DEST** 语法，取代了旧的各平台专用分隔符。

# INSTALL

```apt: sudo apt install pyinstaller```

```apk: sudo apk add py3-pyinstaller```

```brew: brew install pyinstaller```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1)
