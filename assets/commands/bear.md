# TAGLINE

为 clang 工具链生成编译数据库

# TLDR

**生成**编译数据库

```bear -- make```

**追加**到现有数据库

```bear --append -- make clean all```

**自定义输出**文件

```bear --output [compile_commands.json] -- ninja```

# SYNOPSIS

**bear** [_options_] **--** _build-command_

# DESCRIPTION

**bear**（Build EAR）通过拦截构建过程中的编译器调用生成编译数据库（compile_commands.json）。该数据库让 clangd、clang-tidy 和各类 IDE 等工具无需自定义配置即可理解项目结构。

该工具通过记录实际的编译器调用来兼容任何构建系统。从版本 3 起，构建命令必须用 `--` 与 bear 自身的选项分隔；较早的 2.4.x 软件包则省略它。

# PARAMETERS

**-o** _file_, **--output** _file_
> 输出文件（默认：compile_commands.json）

**-a**, **--append**
> 将结果追加到现有数据库而不是覆盖它

**-c** _file_, **--config** _file_
> 从配置文件读取设置（输出格式化、编译器/源文件过滤器）

**-h**, **--help**
> 打印帮助信息

**-V**, **--version**
> 打印版本信息

# WORKFLOW

```bash
# With Make
bear -- make

# With CMake/Ninja
bear -- ninja

# Clean build
bear -- make clean all

# Append incremental build
bear --append -- make module
```

# FEATURES

- 与构建系统无关
- 拦截编译器调用
- 支持并行构建
- 兼容 make、ninja 等
- 无需修改构建系统

# COMPILATION DATABASE

生成的 compile_commands.json 格式：
```json
[
  {
    "directory": "/path/to/project",
    "command": "gcc -c file.c -o file.o",
    "file": "file.c"
  }
]
```

# CAVEATS

需要运行完整构建。若使用了编译缓存，可能无法捕获所有编译单元。某些构建系统有原生支持（CMake: -DCMAKE_EXPORT_COMPILE_COMMANDS=ON）。不同平台采用不同的拦截方法。

# HISTORY

**bear** 由 László Nagy（rizsotto）于 **2012** 年前后创建，用于为使用任意构建系统的 C/C++ 项目生成编译数据库。版本 3 引入了 `--` 分隔符语法，版本 4 则用 Rust 重写了整个工具。

# INSTALL

```apt: sudo apt install bear```

```dnf: sudo dnf install bear```

```pacman: sudo pacman -S bear```

```apk: sudo apk add bear```

```brew: brew install bear```

```nix: nix profile install nixpkgs#bear```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[compiledb](/man/compiledb)(1), [cmake](/man/cmake)(1), [clangd](/man/clangd)(1), [make](/man/make)(1), [ninja](/man/ninja)(1), [clang](/man/clang)(1)

# RESOURCES

```[Source code](https://github.com/rizsotto/Bear)```

```[Documentation](https://github.com/rizsotto/Bear/blob/master/README.md)```

<!-- verified: 2026-06-19 -->
