# TAGLINE

Rust 工具链安装与管理工具

# TLDR

**安装 Rust 工具链**

```rustup install [stable]```

**设置默认工具链**

```rustup default [stable]```

**更新所有工具链**

```rustup update```

**显示已安装的工具链**

```rustup show```

**添加组件**

```rustup component add [rustfmt]```

为交叉编译**添加目标平台**

```rustup target add [x86_64-unknown-linux-musl]```

**使用指定工具链运行命令**

```rustup run [nightly] [cargo build]```

为当前目录**覆盖工具链设置**

```rustup override set [nightly]```

**安装 nightly 版本**

```rustup install nightly```

**卸载某个工具链**

```rustup uninstall [nightly]```

# SYNOPSIS

**rustup** [_options_] _command_ [_args_]

# DESCRIPTION

**rustup** 是 Rust 工具链的安装器和版本管理器。它负责安装和管理多个 Rust 版本（stable、beta、nightly）、组件（rustfmt、clippy）以及交叉编译目标平台。

工具链按用户安装在 ~/.rustup 中。Rustup 管理当前生效的工具链，可以在全局范围或按项目（通过 rust-toolchain.toml 文件）轻松切换版本。

rustup 还负责更新 Rust，只需一条命令即可让所有已安装的工具链保持最新。

# PARAMETERS

**install** _toolchain_
> 安装一个工具链。

**uninstall** _toolchain_
> 移除一个工具链。

**update**
> 更新已安装的工具链。

**default** _toolchain_
> 设置默认工具链。

**show**
> 显示已安装的工具链。

**run** _toolchain_ _command_
> 使用指定工具链运行命令。

**override set** _toolchain_
> 为特定目录设置工具链覆盖。

**override unset**
> 移除目录级覆盖。

**component add** _name_
> 向工具链添加组件。

**component list**
> 列出可用组件。

**target add** _target_
> 添加编译目标平台。

**target list**
> 列出可用的目标平台。

**self update**
> 更新 rustup 自身。

**doc**
> 打开 Rust 文档。

# CONFIGURATION

**~/.rustup/**
> 所有 rustup 数据的根目录，包括已安装的工具链、组件和元数据。

**rust-toolchain.toml**
> 项目级文件，指定所需的 Rust 工具链版本、组件和目标平台。进入该目录时，rustup 会自动安装指定的工具链。

**RUSTUP_HOME**
> 覆盖默认 rustup 安装目录的环境变量。

**RUSTUP_TOOLCHAIN**
> 覆盖当前会话所使用的工具链的环境变量。

# CAVEATS

Nightly 版本可能包含破坏性变更或缺陷。某些组件并非对所有工具链可用。交叉编译目标平台可能需要额外的链接器。安装多个工具链会占用更多磁盘空间。

# HISTORY

**rustup** 由 **Brian Anderson** 和 Rust 团队开发，于 **2016 年**发布，作为官方的 Rust 安装器取代了 multirust。它统一了各平台的 Rust 安装方式并简化了版本管理。Rustup 成为了安装 Rust 的推荐方式，对大多数开发者而言已取代发行版软件包。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustc](/man/rustc)(1), [cargo](/man/cargo)(1), [rustfmt](/man/rustfmt)(1), [clippy](/man/clippy)(1)
