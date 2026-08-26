# TAGLINE

面向 Python 和数据科学的软件包与环境管理器

# TLDR

**创建**环境

```conda create -n [myenv] [python=3.11]```

**激活**环境

```conda activate [myenv]```

**安装**软件包

```conda install [numpy]```

**列出**环境

```conda env list```

**导出**环境

```conda env export > [environment.yml]```

**停用**环境

```conda deactivate```

# SYNOPSIS

**conda** _command_ [_options_]

# DESCRIPTION

**conda** 是一个跨平台的软件包与环境管理系统，最初为 Python 而开发，后来扩展到支持 R、Ruby、Lua、Scala、Java、JavaScript、C/C++ 等其他语言。与只管理 Python 包的 pip 不同，conda 能处理完整的环境，包括系统级依赖和编译库，这使它在原生依赖常见的科学计算领域尤为宝贵。

环境隔离特性允许多个依赖需求相互冲突的项目在同一系统上共存。每个 conda 环境都是一个目录，包含特定的一组软件包；在环境之间切换会改变可用的软件包集合。这对数据科学工作流至关重要——不同项目可能需要不同版本的 NumPy、TensorFlow 或其他基础库。

Conda 分发二进制软件包而非从源码构建，这极大加快了安装速度，并消除了困扰 pip 工作流的编译错误。软件包生态按频道组织，其中 conda-forge 是最大的社区维护频道。conda 包含在 Anaconda（含 1500+ 软件包的大型发行版）和 Miniconda（仅含 conda 和 Python 的最小安装器）之中。该工具已成为数据科学、机器学习和科学计算社区的事实标准。

# PARAMETERS

**create** **-n** _name_
> 创建新环境

**install** _package_
> 安装软件包

**update** _package_
> 更新软件包

**remove** _package_
> 移除软件包

**list**
> 列出已安装的软件包

**search** _package_
> 搜索软件包

**env list**
> 列出环境

**activate** _name_
> 激活环境

**deactivate**
> 停用环境

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置文件。

**/opt/conda/.condarc**
> 系统级 conda 配置。

**environment.yml**
> 用于实现可复现环境的环境规格文件。

# ENVIRONMENT MANAGEMENT

```bash
# Create environment with Python
conda create -n myenv python=3.11

# Create with packages
conda create -n dataenv python=3.11 numpy pandas matplotlib

# Create from file
conda env create -f environment.yml

# Clone environment
conda create --clone myenv -n myenv_copy

# Remove environment
conda env remove -n myenv

# List all environments
conda env list
```

# PACKAGE MANAGEMENT

```bash
# Install package
conda install numpy

# Install specific version
conda install numpy=1.24.0

# Install from channel
conda install -c conda-forge package

# Update package
conda update numpy

# Update all packages
conda update --all

# Remove package
conda remove numpy
```

# ENVIRONMENT.YML

```yaml
name: myenv
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - pip:
    - some-pip-package
```

# FEATURES

- 跨平台
- 支持多种语言
- 二进制软件包分发
- 依赖解析
- 环境隔离
- 频道系统
- 与 pip 集成

# CAVEATS

磁盘空间占用较大。环境激活需要 shell 集成。频道优先级可能引起困惑。某些软件包仅存在于 conda-forge。对纯 Python 软件包而言比 pip 慢。混用 conda 和 pip 可能引发问题。

# HISTORY

**Conda** 由 Travis Oliphant 和 Peter Wang 于 **2012** 年前后在 Continuum Analytics（现为 Anaconda, Inc.）为 Anaconda 发行版而创建。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [virtualenv](/man/virtualenv)(1), [mamba](/man/mamba)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Homepage](https://conda.io)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/)```

<!-- verified: 2026-06-22 -->
