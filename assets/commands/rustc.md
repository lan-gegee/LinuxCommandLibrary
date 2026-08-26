# TAGLINE

Rust 编程语言编译器

# TLDR

**编译 Rust 文件**

```rustc [main.rs]```

**编译并指定输出名称**

```rustc [main.rs] -o [program]```

**开启优化编译**

```rustc -O [main.rs]```

**以 release 模式编译**

```rustc -C opt-level=3 [main.rs]```

**附带调试信息编译**

```rustc -g [main.rs]```

**显示警告**

```rustc -W warnings [main.rs]```

**输出汇编代码**

```rustc --emit=asm [main.rs]```

**输出 LLVM IR**

```rustc --emit=llvm-ir [main.rs]```

**只检查而不编译**

```rustc --emit=metadata [main.rs]```

**显示版本**

```rustc --version```

# SYNOPSIS

**rustc** [_options_] _input_

# DESCRIPTION

**rustc** 是 Rust 编程语言的编译器。它将 Rust 源代码（.rs 文件）编译为可执行文件或库。编译器会执行类型检查、借用检查和优化。

虽然可以直接使用 rustc，但大多数 Rust 开发都通过 Cargo 进行，由 Cargo 以合适的设置调用 rustc。直接使用 rustc 常见于简单程序、学习场景或高级构建定制。

rustc 使用 LLVM 进行代码生成，提供出色的优化效果并支持众多目标平台。

# PARAMETERS

**-o** _file_
> 输出文件名。

**-O**
> 开启优化（等价于 -C opt-level=3）。

**-g**
> 包含调试信息。

**-C** _option_
> 代码生成选项。

**-W** _lint_
> 设置 lint 警告级别。

**-A** _lint_
> 允许某个 lint。

**-D** _lint_
> 拒绝某个 lint（使其成为错误）。

**--emit=** _type_
> 输出类型（asm、llvm-ir、llvm-bc、obj、link、metadata、dep-info、mir）。

**--crate-type=** _type_
> crate 类型（bin、lib、rlib、dylib、cdylib、staticlib、proc-macro）。

**--edition=** _year_
> Rust 版本（2015、2018、2021、2024）。

**--test**
> 构建测试套件（test harness）。

**--print** _info_
> 打印编译器信息（例如 target-list、cfg、sysroot）。

**-F** _lint_
> 禁止某个 lint（不可被覆盖）。

**--target=** _triple_
> 目标平台。

**--explain** _code_
> 解释某个错误代码。

**-L** _path_
> 添加库搜索路径。

**--extern** _name=path_
> 指定外部 crate 的位置。

# CAVEATS

直接使用 rustc 需要手动管理依赖。大多数项目应改用 Cargo。不同 edition 的差异可能导致兼容性问题。交叉编译需要安装对应目标的工具链。

# HISTORY

**rustc** 作为 **Rust 编程语言**项目的一部分开发，该项目由 **Graydon Hoare** 于 **2006 年**在 Mozilla 启动。Rust 于 **2015 年 5 月**达到 1.0 版本。编译器最初用 OCaml 编写，但在 1.0 版本之前已用 Rust 重写（自举）。开发工作目前在 **2021 年**成立的 Rust 基金会之下持续进行。

# INSTALL

```apt: sudo apt install rustc```

```dnf: sudo dnf install rust```

```pacman: sudo pacman -S rust```

```apk: sudo apk add rust```

```zypper: sudo zypper install rust```

```brew: brew install rust```

```nix: nix profile install nixpkgs#rustc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustup](/man/rustup)(1), [rustfmt](/man/rustfmt)(1), [clippy](/man/clippy)(1)
