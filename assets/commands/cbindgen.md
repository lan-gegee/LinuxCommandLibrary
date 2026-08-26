# TAGLINE

从 Rust FFI 库生成 C/C++ 头文件

# TLDR

**从 Rust 库生成 C 头文件**

```cbindgen -o [header.h]```

**生成 C++ 头文件**

```cbindgen --lang c++ -o [header.hpp]```

**显式生成 C 头文件**

```cbindgen --lang c -o [header.h]```

**使用指定配置文件**

```cbindgen --config [cbindgen.toml] -o [header.h]```

**从指定 crate 生成**

```cbindgen --crate [crate_name] -o [header.h]```

**显示帮助**

```cbindgen --help```

# SYNOPSIS

**cbindgen** [_options_] [_crate_directory_]

# DESCRIPTION

**cbindgen** 从暴露公开 C API 的 Rust 库生成 C 和 C++11 头文件。它解析 Rust 源代码，为 FFI 导出的类型和函数创建对应的 C 声明。

该工具由 Mozilla 开发，确保生成的头文件与 Rust 的类型布局和 ABI 保证相匹配。

# PARAMETERS

**-o**, **--output** _file_
> 输出头文件的路径

**--lang** _language_
> 输出语言：c 或 c++（默认：c++）

**--config** _file_
> cbindgen.toml 配置的路径

**--crate** _name_
> 要为其生成绑定的 crate 名称

**--profile** _name_
> 要使用的 Cargo profile

**-v**, **--verbose**
> 启用详细输出

**-q**, **--quiet**
> 抑制输出

**--verify**
> 校验已有头文件是否与生成结果一致

**--help**
> 显示帮助

# CONFIGURATION

**cbindgen.toml**
> 控制输出语言、头文件保护宏、include 指令、格式化风格以及类型重命名规则。

# BUILD SCRIPT USAGE

添加到 build.rs 中，即可在构建时自动生成。

# CAVEATS

只为 pub extern "C" 函数和 #[repr(C)] 类型生成头文件。要求 Rust 代码中有正确的 FFI 注解。可通过配置文件自定义输出格式。

# INSTALL

```apt: sudo apt install cbindgen```

```dnf: sudo dnf install cbindgen```

```pacman: sudo pacman -S cbindgen```

```apk: sudo apk add cbindgen```

```brew: brew install cbindgen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [bindgen](/man/bindgen)(1), [rustc](/man/rustc)(1)

# RESOURCES

```[Source code](https://github.com/mozilla/cbindgen)```

```[Documentation](https://github.com/mozilla/cbindgen/blob/master/docs.md)```

<!-- verified: 2026-06-22 -->
