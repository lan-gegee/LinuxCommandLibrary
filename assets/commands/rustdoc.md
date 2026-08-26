# TAGLINE

从 Rust 源代码生成文档

# TLDR

**生成文档**

```rustdoc [lib.rs]```

**为 crate 生成文档**

```rustdoc --crate-name [mylib] [lib.rs]```

**输出到目录**

```rustdoc -o [docs] [lib.rs]```

**对文档运行测试**

```rustdoc --test [lib.rs]```

**设置 edition**

```rustdoc --edition [2021] [lib.rs]```

# SYNOPSIS

**rustdoc** [_options_] _input_

# DESCRIPTION

**rustdoc** 从 Rust 源代码和文档注释生成 HTML 文档。它会提取特殊格式的注释并生成可导航的 API 文档。

该工具通常通过 `cargo doc` 调用而非直接使用，但也可用于自定义文档需求。

# PARAMETERS

**--crate-name** _name_
> crate 名称。

**-o** _dir_, **--out-dir** _dir_
> 输出目录。

**--test**
> 运行文档测试。

**--edition** _year_
> Rust 版本。

**-L** _path_
> 库搜索路径。

**--extern** _name=path_
> 外部 crate。

**--document-private-items**
> 包含私有条目。

**--html-in-header** _file_
> 插入到 header 中的 HTML。

**--markdown-css** _file_
> 用于 markdown 的 CSS。

# CAVEATS

通常应改用 cargo doc。依赖项需要正确的库路径。文档测试需要适当的配置。私有条目默认隐藏。

# HISTORY

**rustdoc** 自 Rust 早期开发起就是其组成部分。Rust 拥有浓厚的文档文化，rustdoc 通过文档注释实现了这一点——注释会编译成 HTML 并包含经过测试的代码示例。

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

[cargo](/man/cargo)(1), [rustc](/man/rustc)(1), [doxygen](/man/doxygen)(1)
