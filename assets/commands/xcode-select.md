# TAGLINE

管理 macOS 开发者工具目录

# TLDR

**安装命令行开发者工具**

```xcode-select --install```

**打印当前开发者目录路径**

```xcode-select -p```

**切换到另一个 Xcode 安装**

```sudo xcode-select -s [/Applications/Xcode.app]```

**切换到仅命令行工具**

```sudo xcode-select -s [/Library/Developer/CommandLineTools]```

**重置为默认开发者目录**

```sudo xcode-select -r```

**显示版本信息**

```xcode-select --version```

# SYNOPSIS

**xcode-select** [_-h_|_-help_] [_-s path_|_--switch path_] [_-p_|_--print-path_] [_-r_|_--reset_] [_-v_|_--version_] [_--install_]

# PARAMETERS

**--install**
> 安装命令行开发者工具（会打开安装对话框）

**-p**, **--print-path**
> 打印当前所选开发者目录的路径

**-s** _path_, **--switch** _path_
> 将活动开发者目录设置为指定路径（需要 sudo）

**-r**, **--reset**
> 重置为默认的开发者目录搜索（需要 sudo）

**-v**, **--version**
> 打印 xcode-select 版本

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**xcode-select** 管理 macOS 上的活动开发者目录，控制 xcrun、xcodebuild、clang 和 make 等构建工具使用哪个 Xcode 或 Command Line Tools 安装。

命令行工具包包含编译器（clang、gcc）、构建工具（make、cmake）、版本控制（git、svn）以及 macOS SDK。当安装了多个 Xcode 版本时，xcode-select 可以在它们之间切换。

使用 **--install** 而不安装完整 Xcode 时，工具被安装到 /Library/Developer/CommandLineTools；使用完整 IDE 时，工具位于 /Applications/Xcode.app 内。

# CAVEATS

**--switch** 和 **--reset** 选项需要超级用户权限，并会影响系统上的所有用户。macOS 更新后，命令行工具可能需要重新安装。**--install** 命令需要 GUI 交互。

# HISTORY

xcode-select 自 Xcode 3 起就是 macOS 开发者工具的一部分。Apple 大约在 **2012 年**将 Command Line Tools 从完整的 Xcode 中分离出来，使开发者无需下载完整 IDE 即可进行开发。

# SEE ALSO

[xcrun](/man/xcrun)(1), [xcodebuild](/man/xcodebuild)(1), [clang](/man/clang)(1), [make](/man/make)(1)
