# TAGLINE

CircuitPython 库的软件包管理器

# TLDR

**列出已安装的 CircuitPython 库**

```circup list```

**更新连接设备上的所有库**

```circup update```

**安装一个库**

```circup install [library_name]```

**卸载一个库**

```circup uninstall [library_name]```

**显示过期的库**

```circup show```

**将已安装的库冻结**到 requirements 文件

```circup freeze > [requirements.txt]```

# SYNOPSIS

**circup** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出设备上已安装的库。

**update**
> 更新设备上的库。

**install**
> 安装一个库。

**uninstall**
> 移除一个库。

**show**
> 显示过期的库。

**freeze**
> 以 requirements 格式输出已安装的库。

**bundle-show**
> 显示 bundle 中可用的库。

# DESCRIPTION

**circup** 是面向微控制器板上的 CircuitPython 库的软件包管理器。它管理已连接 CircuitPython 设备上的 lib 文件夹，对照 Adafruit CircuitPython Bundle 检查已安装库的可用更新。

该工具通过在挂载的文件系统中扫描有效的 CircuitPython 安装来自动检测已连接的 CircuitPython 设备。它负责下载、安装、更新和移除库，并可将当前库状态冻结为 requirements 文件以便复现。

circup 用 Python 编写，可通过 pip 安装。支持 Adafruit Feather、Circuit Playground 等开发板以及其他兼容 CircuitPython 的硬件。

# CAVEATS

需要连接并挂载 CircuitPython 设备。设备必须运行 CircuitPython（而非 MicroPython）。

# INSTALL

```nix: nix profile install nixpkgs#circup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [mpremote](/man/mpremote)(1)

# RESOURCES

```[Source code](https://github.com/adafruit/circup)```

```[Documentation](https://docs.circuitpython.org/projects/circup/)```

<!-- verified: 2026-06-22 -->
