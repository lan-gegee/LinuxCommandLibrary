# TAGLINE

为 Sailfish 项目生成编译数据库

# TLDR

为当前项目**生成 compile_commands.json**

```sfdk compiledb```

在干净构建之后**生成编译数据库**

```sfdk build && sfdk compiledb```

# SYNOPSIS

**sfdk compiledb** [_options_]

# DESCRIPTION

**sfdk compiledb** 生成 **compile_commands.json** 编译数据库，用于 IDE 集成和工具链。该文件被基于 clang 的工具、语言服务器和 IDE 用来理解每个源文件的构建标志、包含路径和编译器调用方式。

必须在成功构建之后运行此命令，以便从构建日志中提取编译命令。它是 **Sailfish SDK**（sfdk）工具链的一部分。

# CAVEATS

需要先完成一次成功的构建才能提取编译命令。生成的数据库仅反映最近一次构建的配置。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-cmake](/man/sfdk-cmake)(1), [sfdk-qmake](/man/sfdk-qmake)(1), [sfdk-deploy](/man/sfdk-deploy)(1)
