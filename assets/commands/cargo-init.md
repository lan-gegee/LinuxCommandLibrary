# TAGLINE

在现有目录中创建新的 Rust 软件包

# TLDR

**在当前目录中初始化**

```cargo init```

**初始化二进制项目**

```cargo init --bin```

**初始化库**

```cargo init --lib```

**不使用 git 初始化**

```cargo init --vcs none```

**以指定名称初始化**

```cargo init --name [myproject]```

**以指定 edition 初始化**

```cargo init --edition [2021]```

**在指定目录中初始化**

```cargo init [path/to/dir]```

# SYNOPSIS

**cargo init** [_options_] [_path_]

# DESCRIPTION

**cargo init** 在现有目录中创建新的 Cargo 软件包。它会生成 Cargo.toml 和 src/ 目录，其中包含 main.rs（二进制）或 lib.rs（库）。与 cargo new 不同，它不会创建新目录。

# PARAMETERS

**--bin**
> 创建带 src/main.rs 的二进制目标（默认）。

**--lib**
> 创建带 src/lib.rs 的库目标。

**--name** _name_
> 设置软件包名称（默认为目录名）。

**--edition** _year_
> Rust edition（2015、2018、2021、2024）。

**--vcs** _type_
> 初始化版本控制（git、hg、pijul、fossil、none）。

**--registry** _name_
> 用于发布的注册表。

**--force**
> 强制覆盖已有的 Cargo.toml 或 src 目录。

**-v**, **--verbose**
> 详细输出。

**-q**, **--quiet**
> 抑制输出。

# GENERATED FILES

```
.
├── Cargo.toml
├── .gitignore (if using git)
└── src
    └── main.rs (or lib.rs)
```

# CAVEATS

近期 Rust 版本中的默认 edition 为 2024。若尚未处于某个 git 仓库中，默认会初始化一个 git 仓库。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-new](/man/cargo-new)(1), [cargo-build](/man/cargo-build)(1)
