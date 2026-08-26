# TAGLINE

Pharo Smalltalk 的启动器，Pharo 是一个现代的开源 Smalltalk 环境

# TLDR

**启动 Pharo 镜像**

```pharo [image.image]```

**无界面运行**

```pharo --headless [image.image] [script.st]```

**求值表达式**

```pharo [image.image] eval "[expression]"```

**以 GUI 启动**

```pharo-ui [image.image]```

# SYNOPSIS

**pharo** [_options_] _image_ [_arguments_]

# PARAMETERS

**--headless**
> 无 GUI 运行。

**--no-quit**
> 脚本执行完后不退出。

**eval**
> 求值 Smalltalk 表达式。

**--version**
> 显示版本。

**image**
> Pharo 镜像文件。

# DESCRIPTION

**pharo** 是 Pharo Smalltalk 的启动器，Pharo 是一个现代的开源 Smalltalk 环境。Pharo 使用基于镜像的持久化方式，整个环境状态都会被保存。
# Launch GUI
pharo-ui Pharo.image

# Run script headless
pharo --headless Pharo.image script.st

# Evaluate and print
pharo Pharo.image eval "3 + 4"

# Save and quit
pharo Pharo.image eval "Smalltalk snapshot: true andQuit: true"

# Run tests
pharo --headless Pharo.image test MyPackage
```

# IMAGE MANAGEMENT

```bash
# Download fresh image
curl https://get.pharo.org/64/ | bash

# Create clean image
pharo Pharo.image save MyProject
```

# CAVEATS

需要 Pharo VM 和镜像。镜像文件是平台相关的。更改会持久化保存在镜像中。

# HISTORY

Pharo 于 2008 年从 **Squeak** Smalltalk 分叉而来，专注于简洁、创新的 Smalltalk 开发。

# SEE ALSO

[squeak](/man/squeak)(1)

# INSTALL

```nix: nix profile install nixpkgs#pharo```

<!-- packages: 2026-07-22 -->
