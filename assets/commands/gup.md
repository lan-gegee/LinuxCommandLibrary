# TAGLINE

并行更新通过 "go install" 安装的二进制文件

# TLDR

**并行更新** $GOPATH/bin 下安装的所有二进制文件

```gup update```

**列出所有已安装的** Go 二进制文件的路径和版本

```gup list```

**更新所有二进制文件**但排除指定项

```gup update --exclude=[binary1,binary2]```

**预览更新**而不做任何更改

```gup update --dry-run```

**检查**已安装的二进制文件是否为最新版本

```gup check```

**移除**已安装的 Go 二进制文件

```gup remove [binary_name]```

将当前二进制文件配置**导出**到 gup.json

```gup export```

从 gup.json 配置文件**重新安装**所有二进制文件

```gup import --input=[path/to/gup.json]```

# SYNOPSIS

**gup** _subcommand_ [_options_]

# PARAMETERS

**update**
> 使用 goroutine 将 $GOPATH/bin 下的所有二进制文件更新到最新版本。

**list**
> 显示所有已安装的二进制文件及其导入路径和版本。

**remove** _binary_
> 从 $GOPATH/bin 或 $GOBIN 中删除指定的二进制文件。

**check**
> 检查每个已安装的二进制文件是否为最新版本，但不执行更新。

**export**
> 将当前的二进制文件集合写入 gup.json 配置文件。

**import**
> 安装或恢复 gup.json 文件中列出的二进制文件。

**man**
> 生成 man page（Linux/macOS）。

**completion**
> 生成 Shell 补全脚本。

**version**
> 打印版本信息。

**-e**, **--exclude** _list_
> 更新时要跳过的二进制文件列表，以逗号分隔。

**--dry-run**
> 显示将要执行的操作，但不进行任何更新。

**--notify**
> 操作完成时显示桌面通知。

**--main**
> 更新时使用 @main 模块通道。

**--master**
> 更新时使用 @master 模块通道。

**--latest**
> 更新时使用 @latest 模块通道。

**--force**
> 跳过确认提示（与 **remove** 配合使用）。

# DESCRIPTION

**gup** 用于将通过 **go install** 安装的二进制文件更新到最新版本。它会扫描 **GOBIN**（或 **$GOPATH/bin**）指向的目录，检查每个二进制文件内嵌的模块信息，并使用 goroutine 并行重建它们。这使得升级大量基于 Go 的 CLI 工具比逐个手动运行 **go install** 快得多。

该工具读取 Go 1.17 起嵌入在 Go 二进制文件中的版本元数据，并将原始模块路径重新传给 **go install**。没有模块信息的二进制文件无法更新，会被跳过并给出警告。

除更新外，**gup** 还提供列出、移除、检查、导出和重新导入二进制文件的子命令，便于在多台机器之间复制同一套 Go 工具链。

# CAVEATS

需要安装 **go** 工具链且在 **$PATH** 中可用。只有带模块信息构建的二进制文件（Go 1.17+ 的默认行为）才能被更新。通过 **GOPROXY=off** 安装或从本地路径安装的二进制文件无法重新安装。更新通道（**@latest**、**@main**、**@master**）必须得到上游模块的支持。

# CONFIGURATION

**gup.json**
> 由 **gup export** 写入、由 **gup import** 使用的配置文件。存储每个二进制文件的模块路径和所选的更新通道。在 v1.0.0 中取代了旧的 **gup.conf** 格式。

**$GOPATH/bin** / **$GOBIN**
> 扫描二进制文件的目标目录。设置 **$GOBIN** 时以其为准。

# HISTORY

**gup** 由 **nao1215** 创建，首次发布于 **2022 年**。它使用 Go 编写，旨在通过并发更新让管理以 go install 方式安装的 CLI 工具更加轻松。版本 **1.0.0** 引入了 JSON 配置格式以及按二进制文件选择更新通道的功能。

# INSTALL

```brew: brew install gup```

```nix: nix profile install nixpkgs#gup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [asdf](/man/asdf)(1)
