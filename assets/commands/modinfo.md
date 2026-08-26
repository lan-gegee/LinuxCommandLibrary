# TAGLINE

提取并显示 Linux 内核模块的信息

# TLDR

列出模块的**所有属性**

```modinfo module_name```

只显示**特定字段**

```modinfo -F author module_name```

显示模块的**文件名**

```modinfo -F filename module_name```

显示模块的**参数**

```modinfo -F parm module_name```

显示模块的**许可证**

```modinfo -F license module_name```

# SYNOPSIS

**modinfo** [_-0_] [_-F field_] [_-k kernel_] _modulename_|_filename_...

# DESCRIPTION

**modinfo** 提取并显示 Linux 内核模块的信息。它可以显示全部属性或特定字段，如作者、描述、许可证、参数和依赖关系。

# PARAMETERS

**-F, --field FIELD**
> 只显示指定字段的值

**-k, --set-version VERSION**
> 使用指定内核版本的模块

**-b, --basedir DIR**
> 将指定目录用作模块的根目录

**-0, --null**
> 用 NUL 而非换行符分隔字段值

**-a, --author**
> -F author 的快捷方式

**-d, --description**
> -F description 的快捷方式

**-l, --license**
> -F license 的快捷方式

**-p, --parameters**
> -F parm 的快捷方式

**-n, --filename**
> -F filename 的快捷方式

# COMMON FIELDS

**filename**: 模块文件的路径
**author**: 模块作者
**description**: 模块描述
**license**: 许可证类型（GPL 等）
**version**: 模块版本
**parm**: 模块参数及其说明
**depends**: 模块依赖
**alias**: 模块别名
**srcversion**: 源码版本哈希

# CAVEATS

模块信息在编译时嵌入。并非所有模块都包含所有字段。**parm** 显示的参数可以传给 modprobe。

# HISTORY

**modinfo** 是 **kmod** 的一部分，kmod 是取代旧版 module-init-tools 的内核模块工具集。

# INSTALL

```apt: sudo apt install kmod```

```dnf: sudo dnf install kmod```

```pacman: sudo pacman -S kmod```

```apk: sudo apk add kmod```

```zypper: sudo zypper install kmod```

```brew: brew install kmod```

```nix: nix profile install nixpkgs#kmod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[modprobe](/man/modprobe)(8), [lsmod](/man/lsmod)(8), [insmod](/man/insmod)(8)
