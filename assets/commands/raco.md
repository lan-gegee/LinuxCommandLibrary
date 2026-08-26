# TAGLINE

Racket 软件包和项目管理工具

# TLDR

**安装软件包**

```raco pkg install [package-name]```

**更新软件包**

```raco pkg update```

**移除软件包**

```raco pkg remove [package-name]```

**显示已安装的软件包**

```raco pkg show```

**创建可执行文件**

```raco exe [program.rkt]```

**运行测试**

```raco test [file.rkt]```

**构建文档**

```raco docs```

**生成分发包**

```raco distribute [dir] [executable]```

# SYNOPSIS

**raco** _command_ [_options_] [_args_]

# PARAMETERS

**pkg**
> 软件包管理。

**exe**
> 创建可执行文件。

**test**
> 运行测试。

**docs**
> 文档。

**setup**
> 安装配置 collection。

**distribute**
> 创建分发包。

**make**
> 编译文件。

**check-requires**
> 检查依赖。

# DESCRIPTION

**raco** 是 Racket 用于管理软件包和构建程序的命令行工具。

软件包管理从 Racket 软件包目录安装，依赖自动解析。

可执行文件创建功能会编译 Racket 程序，生成的独立二进制文件包含运行时。

测试功能运行源文件中的单元测试，test 子模块会被自动发现。

文档生成构建 HTML 文档，Scribble 文档会被编译。

分发功能将可执行文件连同依赖打包在一起，生成可移植的软件包。

# CAVEATS

部分命令需要先执行 setup。大型软件包可能耗时较长。可执行文件与平台相关。

# HISTORY

**raco** 是随 **Racket**（前身为 PLT Scheme）分发的标准工具。它整合了软件包管理、构建和开发任务。

# INSTALL

```apt: sudo apt install racket```

```dnf: sudo dnf install racket```

```pacman: sudo pacman -S racket```

```apk: sudo apk add racket```

```zypper: sudo zypper install racket```

```brew: brew install racket```

```nix: nix profile install nixpkgs#racket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[racket](/man/racket)(1), [drracket](/man/drracket)(1)
