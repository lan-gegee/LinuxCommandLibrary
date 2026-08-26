# TAGLINE

为 Rust 软件包生成文档

# TLDR

**构建文档**

```cargo doc```

**构建并在浏览器中打开**

```cargo doc --open```

**不包含依赖地构建**

```cargo doc --no-deps```

**包含私有条目**

```cargo doc --document-private-items```

**为所有工作空间成员构建**

```cargo doc --workspace```

**以 release profile 构建**

```cargo doc --release```

**以所有特性构建**

```cargo doc --all-features```

# SYNOPSIS

**cargo doc** [_options_]

# DESCRIPTION

**cargo doc** 使用 rustdoc 为本地软件包及所有依赖构建文档。输出为 HTML 格式，位于 target/doc/ 中。

# PARAMETERS

**--open**
> 构建后在浏览器中打开文档

**--no-deps**
> 不为依赖构建文档

**--document-private-items**
> 包含非公开条目（对二进制文件是默认行为）

**-r**, **--release**
> 以 release profile 构建

**--workspace**
> 为所有工作空间成员生成文档

**--exclude** _spec_
> 排除软件包（与 --workspace 搭配使用）

**-p**, **--package** _spec_
> 为指定软件包生成文档

**--lib**
> 只为库生成文档

**--bins**
> 为所有二进制文件生成文档

**--target** _triple_
> 为目标架构生成文档

**-j**, **--jobs** _n_
> 并行任务数（默认：CPU 核心数）

**--features** _features_
> 启用指定的特性

**--all-features**
> 启用所有特性

**--no-default-features**
> 禁用默认特性

# ENVIRONMENT

**BROWSER**
> 与 --open 配合使用的浏览器

# OUTPUT

文档生成于 target/doc/<crate_name>/index.html

# CAVEATS

跳过与库同名的二进制文件。跳过缺少必需特性的二进制文件。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustdoc](/man/rustdoc)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-doc.html)```

<!-- verified: 2026-06-22 -->
