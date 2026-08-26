# TAGLINE

Open Babel 命令行工具，用于在分子文件格式之间转换

# TLDR

将 **.mol** 文件转换为 XYZ 坐标

```obabel [path/to/file.mol] -O [path/to/output_file.xyz]```

将 **SMILES 字符串**转换为 500x500 的图片

```obabel -:"[SMILES]" -O [path/to/output_file.png] -xp 500```

将包含 SMILES 字符串的文件转换为多个独立的 **3D .mol** 文件

```obabel [path/to/file.smi] -O [path/to/output_file.mol] --gen3D -m```

将**多个输入**渲染为一张图片

```obabel [path/to/file1 path/to/file2 ...] -O [path/to/output_file.png]```

# SYNOPSIS

**obabel** [_OPTIONS_] [**-i** _input-type_] _infile_ [**-o** _output-type_] **-O** _outfile_

**obabel** **-:**"_SMILES-string_" [_OPTIONS_] **-O** _outfile_

# PARAMETERS

**-i** _format_
> 显式指定输入格式（例如 **-imol**、**-ismi**）

**-o** _format_
> 显式指定输出格式（例如 **-osmi**、**-opng**）

**-O** _outfile_
> 指定输出文件路径

**-:**"_SMILES_"
> 使用 SMILES 字符串代替文件作为输入

**-m**
> 生成多个输出文件（每个分子一个）

**-f** _#_
> 从指定的分子序号开始导入

**-l** _#_
> 在指定的分子序号处结束导入

**--gen3D**
> 为分子生成 3D 坐标

**-e**
> 出错后继续处理下一个对象

**-z**
> 使用 gzip 压缩输出

**-H**
> 显示帮助；使用 **-H**_format_ 可查看特定格式的帮助

**-V**
> 显示版本号

**-a**_option_
> 输入格式特有的选项

**-x**_option_
> 输出格式特有的选项

# DESCRIPTION

**obabel** 是 Open Babel 的命令行工具，用于在化学和计算建模中使用的分子文件格式之间进行转换。它支持超过 100 种化学数据格式，包括 SDF、MOL、PDB、SMILES、CML 以及用于可视化的图像格式。

除简单转换外，obabel 还能按属性过滤分子、生成 3D 坐标、使用力场（MMFF94、UFF、GAFF）执行能量最小化以及操作分子数据。它支持通配符模式的批处理，并可将多分子文件拆分为单独的输出。

# CAVEATS

格式检测依赖文件扩展名；当扩展名不明确时请显式使用 **-i** 和 **-o** 标志。如果目标格式缺少对应字段，某些转换可能会丢失数据。对大分子生成 3D 坐标（**--gen3D**）可能较慢。

# HISTORY

Open Babel 起源于 **1998 年**启动的 **OELib/OBabel** 项目。约在 2.3 版（2011 年）时，**obabel** 命令取代了旧的 **babel** 命令，按照 Unix 惯例改进了选项处理。Open Babel 3.0 于 **2019 年**发布，增强了立体化学支持。

# INSTALL

```apt: sudo apt install openbabel```

```dnf: sudo dnf install openbabel```

```pacman: sudo pacman -S openbabel```

```zypper: sudo zypper install openbabel```

```nix: nix profile install nixpkgs#openbabel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rdkit](/man/rdkit)(1), [pymol](/man/pymol)(1)
