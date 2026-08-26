# TAGLINE

使用额外的 rustdoc 标志构建文档

# TLDR

**带 rustdoc 选项构建文档**

```cargo rustdoc -- [rustdoc_flags]```

**文档中包含私有条目**

```cargo rustdoc -- --document-private-items```

**输出 JSON 格式（nightly）**

```cargo rustdoc -Z unstable-options --output-format json```

**为指定二进制生成文档**

```cargo rustdoc --bin [name] -- [flags]```

**以所有特性构建文档**

```cargo rustdoc --all-features```

# SYNOPSIS

**cargo rustdoc** [_options_] [-- _args_]

# DESCRIPTION

**cargo rustdoc** 为当前软件包构建文档，并将额外选项直接传递给 rustdoc 工具。`--` 之后的参数只转发给指定目标的最后一次 rustdoc 调用，不会传给依赖。

此命令与 `cargo doc` 类似，但可以对 rustdoc 标志进行细粒度控制。常见用途包括：在文档中包含私有条目、生成供工具使用的 JSON 输出（nightly），以及传入自定义 HTML 或 CSS 设置。提供额外参数时一次只能为一个目标生成文档。

# PARAMETERS

**--open**
> 构建后在浏览器中打开文档

**--lib**
> 只为库生成文档

**--bin** _name_
> 为指定的二进制文件生成文档

**--bins**
> 为所有二进制文件生成文档

**--example** _name_
> 为指定的示例生成文档

**--examples**
> 为所有示例生成文档

**-p**, **--package** _spec_
> 要为其生成文档的软件包

**--target** _triple_
> 为目标平台生成文档

**-j**, **--jobs** _n_
> 并行任务数

**--features** _features_
> 启用特性

**--all-features**
> 启用所有特性

**--no-default-features**
> 禁用默认特性

# OUTPUT FORMATS

**html**
> HTML 文档（默认）

**json**
> JSON 格式（nightly，实验性）

# CAVEATS

传入额外参数时只能为一个目标生成文档。请使用目标过滤器选择。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-doc](/man/cargo-doc)(1), [rustdoc](/man/rustdoc)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html)```

<!-- verified: 2026-06-22 -->
