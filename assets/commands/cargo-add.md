# TAGLINE

向 Rust 项目添加依赖

# TLDR

**添加依赖**

```cargo add [serde]```

**添加指定版本的依赖**

```cargo add [serde@1.0]```

**添加带特性的依赖**

```cargo add [tokio] --features [full]```

**添加为开发依赖**

```cargo add [mockall] --dev```

**添加为构建依赖**

```cargo add [cc] --build```

**从 git 仓库添加**

```cargo add --git [https://github.com/user/repo]```

**从本地路径添加**

```cargo add --path [../my-crate]```

**添加为可选依赖**

```cargo add [feature-crate] --optional```

**重命名依赖**

```cargo add [serde] --rename [my_serde]```

# SYNOPSIS

**cargo add** [_options_] _crate_...
**cargo add** [_options_] --path _path_
**cargo add** [_options_] --git _url_ [_crate_...]

# DESCRIPTION

**cargo add** 在 Cargo.toml 中添加或修改依赖。它会从注册表获取 crate 信息，并以正确的版本约束更新清单文件。自 v1.62 起内置于 Cargo。

# PARAMETERS

**--dev**, **-D**
> 添加为开发依赖

**--build**, **-B**
> 添加为构建依赖

**--optional**
> 将依赖标记为可选

**--rename** _name_
> 重命名该依赖

**--features** _features_
> 启用指定的特性

**--no-default-features**
> 禁用默认特性

**--default-features**
> 重新启用默认特性

**--path** _path_
> 从本地路径添加依赖

**--git** _url_
> 从 git 仓库添加依赖

**--branch** _branch_
> 要使用的 git 分支

**--tag** _tag_
> 要使用的 git 标签

**--rev** _sha_
> 要使用的 git 提交

**-p**, **--package** _spec_
> 要修改的软件包

**--dry-run**
> 显示更改但不修改文件

# OUTPUT

列出所添加依赖已启用（+）和已禁用（-）的特性。

# CAVEATS

会按指定选项更新已有条目。对于 1.62 之前的 Cargo 版本，需安装 cargo-edit 才有此功能。

# INSTALL

```pacman: sudo pacman -S cargo-edit```

```apk: sudo apk add cargo-edit```

```brew: brew install cargo-edit```

```nix: nix profile install nixpkgs#cargo-edit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-remove](/man/cargo-remove)(1), [cargo-update](/man/cargo-update)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-add.html)```

<!-- verified: 2026-06-22 -->
