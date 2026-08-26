# TAGLINE

类似 Neofetch 的国家信息展示工具

# TLDR

**显示**你当前所在国家的信息（通过 IP 自动检测）

```countryfetch```

用两位字母代码**显示**某个国家的信息

```countryfetch [us]```

按名称**显示**多个国家的信息

```countryfetch [UnitedStates] [UnitedKingdom]```

**列出**所有可用的国家名称和代码

```countryfetch --list-countries```

**显示**所有国家的信息

```countryfetch --all-countries```

只**显示**某个国家的特定字段

```countryfetch [us] --select flag population capital```

# SYNOPSIS

**countryfetch** [_OPTIONS_] [_COUNTRY_...]

# PARAMETERS

**COUNTRY**
> 一个或多个国家名称或两位字母 ISO 代码（不区分大小写）。省略时通过公网 IP 地理位置自动检测。

**--all-countries**
> 打印所有国家的信息。

**--list-countries**
> 打印所有可用国家名称和代码的列表。

**--select** _FIELD..._
> 选择要显示的字段：area、flag、emoji、continent、population、tlds、languages、currencies、neighbours、establishment-date、iso-code、driving-side、capital、dialing-code、palette、color。

**--version**
> 打印版本号。

**--help**
> 打印帮助信息。

# DESCRIPTION

**countryfetch** 以类似 neofetch 的终端布局显示国家信息。它会在展示国旗的 ASCII 艺术图的同时，呈现人口、面积、首都、语言、货币、邻国、顶级域名、电话区号、行车方向、建国日期和 ISO 代码等关键信息。输出文字的颜色取自该国国旗中最亮的颜色。所有国家数据都在编译期内嵌，因此无需在运行时调用 API 即可获得国家信息。

# CAVEATS

国家检测依赖公网 IP 查询，因此离线时无法工作，且检测结果可能反映的是 VPN 所在地而非实际位置。国家数据在编译期写入二进制文件，更新数据需要发布新版本。从源码构建需要 Rust/Cargo 1.85+。

# HISTORY

**countryfetch** 由 **Nik Revenco** 创建，首次发布于 **2025 年 3 月**。以 Rust 编写，采用 MIT/Apache-2.0 双许可证。最新版本为 v0.2.0。收录于 Arch Linux 官方仓库和 Homebrew，也可通过 Cargo 获取。其灵感来自 "fetch" 工具家族（neofetch、fastfetch），把同样的终端美学应用到了国家数据上。

# INSTALL

```pacman: sudo pacman -S countryfetch```

```nix: nix profile install nixpkgs#countryfetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [fastfetch](/man/fastfetch)(1), [onefetch](/man/onefetch)(1), [cpufetch](/man/cpufetch)(1)
