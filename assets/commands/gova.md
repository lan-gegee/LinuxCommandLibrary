# TAGLINE

构建并热重载用 Gova Go GUI 框架编写的原生桌面应用

# TLDR

**安装** CLI

```go install github.com/nv404/gova/cmd/gova@latest```

**启动开发循环**，支持文件监听和热重载

```gova dev```

**一次性构建并运行**，不监听变更

```gova run```

**为当前平台编译发布二进制文件**

```gova build```

**构建去除符号、体积更小的发布二进制文件**

```gova build -ldflags "-s -w"```

**以自定义名称构建输出**

```gova build -o [myapp]```

**针对指定的入口包运行开发循环**

```gova dev [./cmd/myapp]```

# SYNOPSIS

**gova** _command_ [_flags_] [_package_]

# PARAMETERS

**dev**
> 监听工作目录，在文件保存时重新构建并重启窗口。忽略 **.git**、**node_modules**、**vendor** 和 **_test.go** 文件。

**run**
> 构建并启动应用一次，不开启文件监听。适用于 CI 流水线或一次性验证。

**build**
> 为宿主平台编译单个静态二进制文件。接受 **-ldflags** 和 **-o** 等 Go 构建标志。

**-ldflags** _flags_
> 将链接器标志传递给底层的 **go build** 调用（例如用 **"-s -w"** 去除符号）。

**-o** _name_
> 设置 **gova build** 生成的二进制文件名。

# DESCRIPTION

**Gova** 是一个面向 Go 的声明式 GUI 框架，可为 macOS、Windows 和 Linux 生成单个静态二进制文件。**gova** CLI 在 **go build** 和 **go run** 之上封装了文件监听、cgo 设置以及平台相关的原生工具链处理，让开发者无需手写构建工具即可快速迭代 Gova 应用。

组件用纯 Go 编写，采用响应式状态模型和类型化的 props。框架暴露了类型化的平台对话框（文件选择器、提醒、通知），并通过 cgo 链接到原生系统库。

在 **gova dev** 过程中，保存任何被监听的 **.go** 文件都会触发增量重建并重启窗口，从而保持开发流畅性。**gova build** 生成的发布级二进制文件分发时不依赖 Go 运行环境。

# CAVEATS

该项目尚处于 **pre-1.0** 阶段——CLI 接口和框架 API 仍在演进中。由于依赖 cgo，每个目标平台都需要 **Go 1.26+** 和可用的 **C 工具链**。其名称与无关的 Go 软件包（**golang-collections/gova**）、**govc**（VMware vSphere CLI）以及 **govm**（Go 版本管理器）重名——它们之间没有任何关联。

# HISTORY

Gova 由 **NV404** 创建，发布于 **github.com/NV404/gova**，文档见 **gova.dev**。它源自用 Go 构建原生桌面 UI 的更大潮流（与 Fyne、Wails 并列），同时让开发者体验更接近现代响应式框架。

# SEE ALSO

[go](/man/go)(1)
