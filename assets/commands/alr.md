# TAGLINE

Ada/SPARK 源码软件包管理器。

# TLDR

**搜索** crate

```alr search [package_name]```

**显示**可用版本

```alr show [package_name]```

**获取**一个 crate

```alr get [package_name]```

**初始化**新 crate

```alr init --bin [project_name]```

**构建**当前项目

```alr build```

**运行**当前项目

```alr run```

# SYNOPSIS

**alr** _command_ [_options_] [_arguments_]

# DESCRIPTION

**alr** 是 Ada 编程语言的 Alire 软件包管理器。它提供类似于 Rust 的 Cargo 或 Node.js 的 npm 的 crate（软件包）管理功能，处理 Ada 项目的依赖、构建和发布。

Alire 连接到社区维护的 crate 索引，便于发现和集成 Ada 库与工具。

# PARAMETERS

**search** _term_
> 搜索匹配词条的 crate

**show** _crate_
> 显示某个 crate 的信息

**get** _crate_
> 下载并设置一个 crate

**init**
> 初始化新项目

**build**
> 构建当前项目

**run**
> 构建并运行当前项目

**with** _crate_
> 为当前项目添加依赖

**publish**
> 将 crate 发布到索引

**update**
> 将依赖更新到最新版本

**toolchain**
> 管理 GNAT 编译器和构建工具（gprbuild）

**test**
> 以批处理模式运行 crate 测试套件

**settings**
> 查看或修改全局和本地配置

**--help**
> 显示命令帮助

# CAVEATS

需要已安装 GNAT Ada 编译器。某些 crate 可能存在平台特定的依赖。crate 索引由社区维护，独立于商业 Ada 工具供应商。

# HISTORY

**Alire** 由 Ada 社区开发，首个稳定版发布于 **2020** 年前后。它为 Ada 开发带来了与其他现代语言相当的软件包管理体验。

# INSTALL

```apt: sudo apt install alire```

```aur: yay -S alire```

```nix: nix profile install nixpkgs#alire```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[alr-help](/man/alr-help)(1), [alr-version](/man/alr-version)(1), [gnatmake](/man/gnatmake)(1), [gprbuild](/man/gprbuild)(1), [cargo](/man/cargo)(1), [opam](/man/opam)(1)

# RESOURCES

```[Source code](https://github.com/alire-project/alire)```

```[Homepage](https://alire.ada.dev/)```

```[Documentation](https://alire.ada.dev/docs/)```

<!-- verified: 2026-06-11 -->
