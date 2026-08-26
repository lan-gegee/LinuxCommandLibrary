# TAGLINE

Shell 脚本软件包管理器

# TLDR

从 GitHub **安装软件包**

```basher install [username/repository]```

**列出已安装的软件包**

```basher list```

**卸载软件包**

```basher uninstall [username/repository]```

**更新软件包**

```basher upgrade [username/repository]```

**更新所有软件包**

```basher upgrade --all```

**链接本地软件包**用于开发

```basher link [path/to/directory] [package_name]```

在 Shell 配置中**初始化 basher**

```basher init - [bash]```

**显示软件包信息**

```basher package-path [username/repository]```

# SYNOPSIS

**basher** _command_ [_arguments_]

# DESCRIPTION

**basher** 是面向托管在 GitHub 及其他 git 仓库上的 Shell 脚本的软件包管理器。它安装 Shell 脚本并使其命令直接出现在 PATH 中，无需手动下载或创建符号链接。

软件包安装到 ~/.basher/cellar 并链接到 ~/.basher/bin。包格式要求可执行文件位于 bin/ 目录或根目录下，man 手册页和补全脚本可选。

Basher 支持 GitHub、GitLab、Bitbucket 或任意 git URL 的软件包。软件包可以包含一个 **package.sh** 文件，声明二进制文件、依赖（DEPS）和补全；basher 可与 bash、zsh 和 fish 协同工作。

# PARAMETERS

**install** _package_
> 从仓库安装软件包。

**uninstall** _package_
> 移除已安装的软件包。

**list**
> 显示所有已安装的软件包。

**upgrade** _package_
> 更新指定软件包。

**upgrade --all**
> 更新所有已安装的软件包。

**link** _directory_ _name_
> 将本地目录链接为软件包。

**unlink** _name_
> 移除已链接的软件包。

**init -** _shell_
> 输出 bash、zsh 或 fish 的初始化代码（对其输出执行 eval）。

**commands** _package_
> 列出软件包提供的命令。

**package-path** _package_
> 显示安装路径。

**outdated**
> 列出有可用更新的软件包。

# CAVEATS

安装软件包需要 git。Shell 配置必须 source basher init 的输出。结构不规范的软件包可能无法正常工作。没有内置的安全验证；从不可信来源安装前请先审查代码。对专为 basher 设计的软件包支持最好。

# HISTORY

**Basher** 由 **Juan Ibiapina** 于 **2013** 年创建，是一个简单的 bash 脚本软件包管理器，灵感来自 Homebrew 和 rbenv 等工具。它旨在解决无需复杂安装流程即可共享和分发 Shell 脚本的问题。该项目作为开源工具仍在 GitHub 上持续维护。

# SEE ALSO

[bash](/man/bash)(1), [bpkg](/man/bpkg)(1), [git](/man/git)(1), [brew](/man/brew)(1)

# RESOURCES

```[Source code](https://github.com/basherpm/basher)```

<!-- verified: 2026-06-19 -->
