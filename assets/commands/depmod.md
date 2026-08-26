# TAGLINE

生成内核模块依赖文件

# TLDR

**为当前运行的内核生成模块依赖**

```depmod```

**为指定内核版本生成**

```depmod [6.8.0-generic]```

**探测所有模块**（未给出文件名时的默认行为）

```depmod -a```

**快速模式**：仅在模块比 modules.dep 更新时重新生成

```depmod -A```

**只预览不写入**（打印到标准输出）

```depmod -n```

**使用暂存目录作为模块树根**

```depmod -b [/path/to/root] [6.8.0-generic]```

**对照 System.map 报告未解析的符号**

```depmod -e -F [/boot/System.map-6.8.0] [6.8.0-generic]```

# SYNOPSIS

**depmod** [**-aAenvw**] [**-b** _basedir_] [**-F** _System.map_] [**-C** _config_] [_kernel_version_]

**depmod** [_options_] _module_files_...

# PARAMETERS

_KERNEL_VERSION_
> 要处理的内核版本。默认为当前运行的内核（`uname -r`）。

**-a**, **--all**
> 探测所有模块。未给出文件名时默认启用。

**-A**, **--quick**
> 除非有模块比 modules.dep 更新，否则静默退出。

**-b**, **--basedir** _DIR_
> 将 _DIR_ 前置到 /lib/modules/<version>；对暂存根很有用。

**-o**, **--outdir** _DIR_
> 将生成的文件写入 _DIR_ 而不是模块树。

**-e**, **--errsyms**
> 报告模块需要、但既未被其他模块提供也未被内核提供的符号。

**-F**, **--filesyms** _System.map_
> 使用 _System.map_ 解析内核提供的符号，配合 **-e** 使用。

**-E**, **--symvers** _Module.symvers_
> 与 **-e** 一起使用时，还报告符号版本（modversion）不匹配。

**-n**, **--show**, **--dry-run**
> 将生成的 modules.dep 和映射文件打印到标准输出，而不写入磁盘。

**-v**, **--verbose**
> 打印每个符号依赖及其提供模块。

**-w**
> 对重复的依赖、别名或符号版本发出警告。

**-C**, **--config** _FILE_
> 覆盖默认的配置文件或目录。

**-V**, **--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**depmod** 生成模块依赖文件（modules.dep 及相关文件），供 modprobe 自动加载内核模块及其依赖时使用。它分析内核模块目录中的所有模块，确定它们之间的相互依赖关系。

该工具扫描模块文件中导出和需要的符号，构建依赖树。有了这些信息，modprobe 在请求某个模块时就能自动加载其前置模块。

depmod 通常在安装内核或更新模块时自动运行。生成的文件保存在 /lib/modules/<kernel_version>/ 中。

# CONFIGURATION

**/etc/depmod.conf** 或 **/etc/depmod.d/*.conf**
> 指定模块搜索路径和覆盖规则的配置文件。

# CAVEATS

写入依赖文件需要 root 权限。添加或删除内核模块后应重新运行。正在运行的内核模块若不考虑相关进程则无法卸载。

# HISTORY

depmod 是 **kmod** 工具集（前身是 module-init-tools）的一部分，自 20 世纪 90 年代可加载内核模块出现之初就用于 Linux 内核模块管理。

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

[modprobe](/man/modprobe)(8), [lsmod](/man/lsmod)(8), [insmod](/man/insmod)(8), [rmmod](/man/rmmod)(8), [kmod](/man/kmod)(8)
