# TAGLINE

可视化分子三维结构

# TLDR

**启动 PyMOL 图形界面**

```pymol```

**打开结构文件**

```pymol [structure.pdb]```

**运行脚本**

```pymol [script.pml]```

**命令行模式**

```pymol -c [script.pml]```

**渲染图像**

```pymol -c -d "load [file.pdb]; ray; png [output.png]"```

# SYNOPSIS

**pymol** [_options_] [_files_...]

# PARAMETERS

**-c**
> 仅命令行模式（无 GUI）。

**-d** _command_
> 执行命令。

**-p**
> 从 stdin 读取命令。

**-q**
> 安静模式。

**-r** _script_
> 运行 Python 脚本。

**-e**
> 脚本执行后退出。

# DESCRIPTION

**PyMOL** 是一个分子可视化系统，用于呈现蛋白质、核酸和小分子的三维结构。它提供出版级质量的图形和丰富的脚本能力。

# EXAMPLES

```bash
# Launch and load structure
pymol protein.pdb

# Batch rendering
pymol -c -d "load 1abc.pdb; hide all; show cartoon; ray; png output.png; quit"

# Run script
pymol script.pml

# Fetch from PDB
pymol -d "fetch 1crn; show cartoon"
```

# COMMANDS (PML)

```
load file.pdb           # Load structure
fetch 1abc              # Download from PDB
show cartoon            # Display style
color red, chain A      # Coloring
ray                     # Render
png output.png          # Save image
```

# CAVEATS

开源版本存在一些限制。提供教育版和商业版许可。处理大型结构时内存占用较高。

# HISTORY

PyMOL 由 **Warren DeLano** 于 1998 年起创建，现由 **Schrödinger, Inc.** 维护并进行开源开发。

# INSTALL

```dnf: sudo dnf install pymol```

```pacman: sudo pacman -S pymol```

```brew: brew install pymol```

```nix: nix profile install nixpkgs#pymol```

<!-- packages: 2026-07-22 -->

# SEE ALSO
