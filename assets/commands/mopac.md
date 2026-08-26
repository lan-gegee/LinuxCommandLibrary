# TAGLINE

半经验量子化学计算程序

# TLDR

**从输入文件运行计算**

```mopac [path/to/input_file.mop]```

**使用 .dat 输入文件运行计算**

```mopac [path/to/input_file.dat]```

**从 .arc 归档文件恢复计算**

```mopac [path/to/input_file.arc]```

# SYNOPSIS

**mopac** _input_file_

# DESCRIPTION

**MOPAC**（Molecular Orbital PACkage）是一个用于计算化学的半经验量子化学程序。它实现了多种基于 Dewar 和 Thiel 提出的 NDDO（Neglect of Diatomic Differential Overlap，忽略双原子微分重叠）近似的方法。

程序从输入文件（.mop、.dat 或 .arc）读取分子几何结构和计算参数，执行电子结构计算、几何优化、过渡态搜索和性质预测。输出文件（.out 为主结果，.arc 为存档数据）会写入输入文件所在的目录，而非当前工作目录。

无需任何关键词；默认行为是使用 PM7 方法进行几何弛豫。常用方法包括 PM7、PM6、AM1 和 MNDO，可用于计算分子性质、反应能和优化几何结构。

# INPUT FILE FORMAT

输入文件的第一行是关键词，第二行是标题/注释，第三行为空行，随后是以元素符号和笛卡尔或内坐标表示的原子坐标。示例：

```
PM7
HF molecule optimization

H 0.0 0.0 0.0
F 0.95 0.0 0.0
```

常见关键词包括：**PM7**、**PM6**、**AM1**、**MNDO**（方法选择）、**CHARGE=n**（分子电荷）、**EF**（过渡态搜索）、**1SCF**（单点能）。

# CAVEATS

半经验方法比从头算（ab initio）方法更快但精度更低。结果高度依赖所选方法（PM7、AM1 等），对某些分子体系可能并不可靠。大分子需要大量计算时间。

# HISTORY

**MOPAC** 最初由 **James J.P. Stewart** 于 20 世纪 80 年代起开发。该程序持续更新并引入新方法，PM7 是最新的参数化方案之一。**OpenMOPAC** 提供该软件的开源版本。

# INSTALL

```apt: sudo apt install mopac```

```dnf: sudo dnf install mopac```

```nix: nix profile install nixpkgs#mopac```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pymol](/man/pymol)(1)
