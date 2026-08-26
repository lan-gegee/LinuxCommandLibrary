# TAGLINE

用 Nim 编写的小巧快速的系统信息工具

# TLDR

显示**系统信息**

```nitch```

显示**帮助**

```nitch -h```

显示**版本**

```nitch -v```

# SYNOPSIS

**nitch** [**-h**|**--help**] [**-v**|**--version**]

# PARAMETERS

**-h, --help**
> 显示帮助信息

**-v, --version**
> 显示版本信息

# DESCRIPTION

**nitch** 是用 Nim 编写的小巧快速的系统信息获取工具。它显示主机名、用户名、操作系统、内核版本、运行时长、Shell、软件包数量以及内存占用等系统信息。

该工具为速度和极简而设计，没有配置选项，专注于以干净而富有色彩的输出格式快速展示关键系统信息。

# OUTPUT

显示内容包括：
- 用户名与主机名
- 操作系统
- 内核版本
- 运行时长
- Shell
- 软件包数量
- 内存使用情况（已用/总量）

# CAVEATS

软件包数量的准确性取决于检测到的包管理器。部分信息在某些系统上可能无法获取。没有配置或自定义选项。

# HISTORY

**nitch** 由 **ssleert** 开发，用来替代 neofetch、fastfetch 等较为臃肿的系统信息工具。它以 Nim 编写以追求高性能，专注于以最小的资源开销只显示必要的系统信息。它面向 Linux 系统，直接从 /proc 和 /etc/os-release 等系统文件读取数据。

# INSTALL

```nix: nix profile install nixpkgs#nitch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [fastfetch](/man/fastfetch)(1), [screenfetch](/man/screenfetch)(1), [pfetch](/man/pfetch)(1), [cpufetch](/man/cpufetch)(1)
