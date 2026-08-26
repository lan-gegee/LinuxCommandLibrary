# TAGLINE

Flatpak 应用程序的构建工具

# TLDR

**构建** Flatpak 并导出到新仓库

```flatpak-builder [path/to/build_directory] [path/to/manifest.json]```

构建 Flatpak 并导出到**指定的仓库**

```flatpak-builder --repo [repository_name] [path/to/build_directory] [path/to/manifest.json]```

构建 Flatpak 并将其**安装到本地**

```flatpak-builder --install [path/to/build_directory] [path/to/manifest.json]```

用 GPG **签名**构建的 Flatpak

```flatpak-builder --gpg-sign [key_id] --repo [repository_name] [path/to/build_directory] [path/to/manifest.json]```

不安装而在应用沙箱内**运行 shell**

```flatpak-builder --run [path/to/build_directory] [path/to/manifest.json] sh```

显示清单文件所需的**依赖**

```flatpak-builder --show-deps [path/to/manifest.json]```

启用 **ccache** 构建以加快重新构建速度

```flatpak-builder --ccache [path/to/build_directory] [path/to/manifest.json]```

# SYNOPSIS

**flatpak-builder** [_options_] _directory_ _manifest_

**flatpak-builder** **--run** [_options_] _directory_ _manifest_ _command_

**flatpak-builder** **--show-deps** [_options_] _manifest_

# PARAMETERS

**--repo** _name_
> 将构建结果导出到指定仓库

**--install**
> 为当前用户在本地安装构建好的应用程序

**--gpg-sign** _key_id_
> 用指定的 GPG 密钥为提交签名

**--arch** _arch_
> 指定目标架构

**--ccache**
> 启用编译器缓存以加快重新构建

**--disable-cache**
> 禁用构建缓存，强制完整重建

**--force-clean**
> 清除之前构建目录中的内容

**--run** _command_
> 在构建沙箱内运行命令

**--build-shell** _module_
> 在指定模块处打开交互式 shell 以便调试

**--stop-at** _module_
> 完成指定模块后停止构建

**--show-deps**
> 显示清单文件所需的依赖

**--show-manifest**
> 显示处理后的清单文件

# DESCRIPTION

**Flatpak-builder** 是一款构建自动化工具，用于从清单文件构建 Flatpak 应用程序。它封装了核心的 **flatpak build** 命令，提供了一套精简的工作流，可在 Flatpak 沙箱内编译应用及其依赖。

该工具处理 JSON 或 YAML 格式的清单文件，其中定义了应用元数据、运行时要求以及各模块的构建指令。它会自动执行标准的 **./configure && make && make install** 流程，并缓存中间结果以实现高效的增量构建。

构建阶段包括：下载源码、初始化应用目录、构建并安装每个模块、清理和收尾。结果按模块缓存，当只有特定组件变化时可以快速重新构建。

# CAVEATS

需要已安装有效的 Flatpak 运行时和 SDK。依赖众多的庞大应用在首次构建时可能耗费大量时间和磁盘空间。**--run** 选项提供的沙箱环境可能没有完整的系统访问权限。清单文件必须正确声明所有依赖，否则构建会失败。

# HISTORY

Flatpak-builder 由 Red Hat 的 Alexander Larsson 与 **Flatpak** 一同开发，最初发布于 **2015-2016 年**前后。它源自 xdg-app 项目，后来成为从源代码构建 Flatpak 应用的标准工具，实现了跨不同 Linux 发行版的可复现构建。

# INSTALL

```apt: sudo apt install flatpak-builder```

```dnf: sudo dnf install flatpak-builder```

```pacman: sudo pacman -S flatpak-builder```

```apk: sudo apk add flatpak-builder```

```zypper: sudo zypper install flatpak-builder```

```nix: nix profile install nixpkgs#flatpak-builder```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flatpak](/man/flatpak)(1), [flatpak-install](/man/flatpak-install)(1)
