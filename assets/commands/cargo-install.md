# TAGLINE

构建并安装 Rust 二进制 crate

# TLDR

**从 crates.io 安装**

```cargo install [ripgrep]```

**安装指定版本**

```cargo install [tokei@12.1.0]```

**从 git 仓库安装**

```cargo install --git [https://github.com/user/repo]```

**从本地路径安装**

```cargo install --path [.]```

**强制重新安装**

```cargo install --force [package]```

**列出已安装的软件包**

```cargo install --list```

**安装到自定义位置**

```cargo install --root [~/.local] [package]```

# SYNOPSIS

**cargo install** [_options_] _crate_[@_version_]...

# DESCRIPTION

**cargo install** 从 crates.io、git 仓库或本地路径构建并安装 Rust 二进制 crate。二进制文件默认安装到 ~/.cargo/bin/。只有包含 [[bin]] 或 [[example]] 目标的软件包才能被安装。

# PARAMETERS

**--version** _version_
> 版本要求（例如 ~1.2、^1.0）

**--git** _url_
> 从 git 仓库安装

**--branch** _branch_
> git 分支

**--tag** _tag_
> git 标签

**--rev** _sha_
> git 提交

**--path** _path_
> 从本地路径安装

**--root** _dir_
> 安装目录

**-f**, **--force**
> 覆盖已有的二进制文件

**--list**
> 列出已安装的软件包

**--bins**
> 安装所有二进制文件

**--examples**
> 安装所有示例

**--no-track**
> 不保存跟踪信息

**--locked**
> 使用 Cargo.lock 中的版本

**-j**, **--jobs** _n_
> 并行构建任务数

**--features** _features_
> 启用指定的特性

**--all-features**
> 启用所有特性

**--no-default-features**
> 禁用该软件包的默认特性集。

**--target** _TRIPLE_
> 为指定的目标三元组交叉编译二进制文件。

**--profile** _NAME_
> 以指定名称的 profile 构建（如 _release_、_dev_）。

**--debug**
> 以 dev profile 构建（编译更快，运行更慢）。

# INSTALLATION ROOT

按以下顺序确定：--root、CARGO_INSTALL_ROOT、install.root 配置项、CARGO_HOME、~/.cargo

# CAVEATS

从源码编译（较慢）。如需预构建的二进制文件，请使用 cargo-binstall。更新需要用 --force 重新安装。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-uninstall](/man/cargo-uninstall)(1), [cargo-binstall](/man/cargo-binstall)(1)
