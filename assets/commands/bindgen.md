# TAGLINE

从 C/C++ 头文件生成 Rust FFI 绑定

# TLDR

**从 C 头文件生成 Rust 绑定**

```bindgen [input.h] -o [bindings.rs]```

**使用白名单生成绑定**

```bindgen [input.h] --allowlist-function "[regex]" --allowlist-type "[regex]" -o [bindings.rs]```

**使用黑名单生成绑定**

```bindgen [input.h] --blocklist-type "[type_name]" -o [bindings.rs]```

**为头文件添加包含路径**

```bindgen [input.h] -o [bindings.rs] -- -I[/path/to/includes]```

**为 C++ 头文件生成绑定**

```bindgen [input.hpp] --enable-cxx-namespaces -o [bindings.rs]```

**传递特定的 clang 参数**

```bindgen [input.h] -o [bindings.rs] -- -std=c11 -DFOO=1```

**生成带 derive trait 的绑定**

```bindgen [input.h] --with-derive-default --with-derive-eq -o [bindings.rs]```

# SYNOPSIS

**bindgen** [_options_] _header_ [**--**] [_clang-args_]

# DESCRIPTION

**bindgen** 自动为 C 和 C++ 库生成 Rust FFI（外部函数接口）绑定。它使用 libclang 解析 C/C++ 头文件，并产出允许在 Rust 中调用原生函数的 Rust 代码。

生成的绑定包括函数声明、结构体定义、枚举、常量和类型别名。bindgen 能处理函数指针、联合体和不透明类型等复杂类型，并将它们映射到合适的 Rust 对应物。

它通常用于 build.rs 脚本中，在编译期生成绑定，确保绑定与库头文件保持同步。它是 Rust 生态中与现有 C/C++ 代码交互的关键工具。

# PARAMETERS

**-o** _file_
> 将输出写入文件而不是 stdout。

**--allowlist-function** _regex_
> 只为匹配的函数生成绑定。

**--allowlist-type** _regex_
> 只为匹配的类型生成绑定。

**--blocklist-type** _regex_
> 从绑定中排除匹配的类型。

**--blocklist-function** _regex_
> 排除匹配的函数。

**--enable-cxx-namespaces**
> 启用 C++ 命名空间支持。

**--with-derive-default**
> 为结构体添加 Default derive。

**--with-derive-eq**
> 为适用的类型添加 Eq derive。

**--with-derive-hash**
> 为适用的类型添加 Hash derive。

**--no-layout-tests**
> 跳过布局测试的生成。

**--generate** _items_
> 指定要生成的内容（functions、types、vars、methods）。

**--opaque-type** _regex_
> 将匹配的类型视为不透明类型。

**--wrap-static-fns**
> 为 static 和 static inline 函数生成包装器。

**--rust-target** _version_
> 生成的绑定支持的最低 Rust 版本。

**--**
> 分隔符，之后的 clang 参数将传给 libclang。

# CAVEATS

需要安装 libclang。对 C++ 的支持比 C 更有限。位域等某些 C 构造可能需要手动调整。生成的代码可能需要 libc crate。编译期生成要求所有构建机器上都装有 libclang。复杂宏不会被翻译。

# HISTORY

**bindgen** 由 **Jyun-Yan You** 于 **2013 年**创建，此后由 Rust 项目社区维护。它成为 rust-lang 官方项目，现由 **rust-lang/rust-bindgen** 仓库维护。该工具经过大幅演进，能够处理更复杂的 C/C++ 模式并提升生成代码的质量，已成为 Rust 互操作能力的重要一环。

# INSTALL

```apt: sudo apt install bindgen```

```pacman: sudo pacman -S rust-bindgen```

```apk: sudo apk add rust-bindgen```

```zypper: sudo zypper install rust-bindgen```

```brew: brew install bindgen```

```nix: nix profile install nixpkgs#rust-bindgen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustc](/man/rustc)(1), [cbindgen](/man/cbindgen)(1), [clang](/man/clang)(1)
