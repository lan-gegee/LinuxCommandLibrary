# TAGLINE

本地 rootkit 检测扫描器

# TLDR

**扫描系统中的 rootkit**

```sudo chkrootkit```

**安静模式（仅显示感染项）**

```sudo chkrootkit -q```

**专家模式，提供更多细节**

```sudo chkrootkit -x```

**使用备用根目录**

```sudo chkrootkit -r [/mnt/system]```

**测试特定检查项**

```sudo chkrootkit [chkwtmp]```

**列出可用的检查项**

```chkrootkit -l```

# SYNOPSIS

**chkrootkit** [_options_] [_test_...]

# DESCRIPTION

**chkrootkit** 在本地检查系统上 rootkit 的踪迹。它检查系统二进制文件是否被已知方式修改过、查找被删除的日志条目、检测可加载内核模块（LKM）木马，并识别处于混杂模式的网络接口。

该工具的原理是将系统二进制文件与已知的 rootkit 修改特征进行比较，并运行一系列测试来寻找常见的 rootkit 行为。它可以检测超过 70 种已知 rootkit 和蠕虫。为了获得最佳效果，应在干净的系统或 live CD 上用可信的二进制文件运行它，因为被攻陷系统的工具可能会隐藏感染痕迹。

# PARAMETERS

**-q**
> 安静模式，仅显示感染项

**-x**
> 专家模式：输出被分析二进制文件的原始字符串，供人工检查

**-e**
> 排除已知的误报文件/目录

**-r** _dir_
> 使用备用根目录

**-p** _dir1:dir2_
> 二进制文件的自定义路径

**-l**
> 列出可用的检查项

**-n**
> 跳过 NFS 挂载的目录

# TESTS

**chkwtmp**
> 检查 wtmp 删除记录

**chklastlog**
> 检查 lastlog 删除记录

**ifpromisc**
> 检查混杂模式的接口

**chkproc**
> 检查 LKM 木马

**strings**
> 快速 strings 检查

# CAVEATS

并非万无一失——高级 rootkit 可以隐藏自身。建议配合 rkhunter 进行全面扫描。可设置 cron 定期扫描。若发现感染，请隔离系统并进行排查。

# INSTALL

```apt: sudo apt install chkrootkit```

```dnf: sudo dnf install chkrootkit```

```brew: brew install chkrootkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rkhunter](/man/rkhunter)(1), [lynis](/man/lynis)(1), [clamav](/man/clamav)(1)
