# TAGLINE

显示 Linux 内核中当前已加载模块的状态

# TLDR

**列出所有已加载的内核模块**

```lsmod```

**按名称过滤**

```lsmod | grep [nvidia]```

**按大小排序模块**（从大到小）

```lsmod | sort -k 2 -n -r```

**统计已加载模块的数量**

```lsmod | tail -n +2 | wc -l```

**查找谁在使用某模块**

```lsmod | awk '$1 == "[btusb]" { print $4 }'```

# SYNOPSIS

**lsmod**

# DESCRIPTION

**lsmod** 是一个简单的小程序，将 `/proc/modules` 的内容以美观的格式展示，显示当前哪些可加载内核模块驻留在内存中。它不接受参数（部分发行版支持 `--help` / `--version`）。

输出每行一个模块，共三列：

- **Module** — 模块名
- **Size** — 内存占用（字节）
- **Used by** — 引用计数，后跟依赖它的模块或子系统的逗号分隔列表

引用计数大于零意味着模块正在使用中，必须先卸载其依赖方才能 `rmmod`。

# OUTPUT COLUMNS

**Module**
> 在内核中注册的模块名。

**Size**
> 模块代码和数据占用的内存（字节）。

**Used by**
> 使用计数，后跟依赖此模块的模块名。短横线（`-`）表示当前没有使用者。

# CAVEATS

`lsmod` 只报告内核已加载的内容；直接编译进内核镜像的内建模块不会出现。要了解特定模块的更多信息（作者、许可证、参数、依赖），请使用 `modinfo`。

# HISTORY

**lsmod** 最初随较早的 **modutils**/**module-init-tools** 套件发布。现在属于 **kmod**——由 **Lucas De Marchi** 等人编写的现行内核模块用户空间工具，约在 Linux 3.2 时取代了 module-init-tools。

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

[modprobe](/man/modprobe)(8), [rmmod](/man/rmmod)(8), [insmod](/man/insmod)(8), [modinfo](/man/modinfo)(8), [depmod](/man/depmod)(8), [kmod](/man/kmod)(8)
