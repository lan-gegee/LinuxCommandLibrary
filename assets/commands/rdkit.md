# TAGLINE

开源化学信息学与分子工具包

# TLDR

**在 Python 中导入 RDKit**

```python -c "from rdkit import Chem"```

**从 SMILES 读取分子**

```python -c "from rdkit import Chem; m = Chem.MolFromSmiles('CCO'); print(m)"```

**计算分子量**

```python -c "from rdkit.Chem import Descriptors; from rdkit import Chem; print(Descriptors.MolWt(Chem.MolFromSmiles('CCO')))"```

# SYNOPSIS

**rdkit** Python library for cheminformatics

# DESCRIPTION

**RDKit** 是一款开源的化学信息学库。它提供读取、写入和操作化学结构、计算分子描述符以及执行子结构搜索等功能。

# EXAMPLES

```python
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, Draw

# Read molecule
mol = Chem.MolFromSmiles('c1ccccc1')  # Benzene

# Calculate properties
mw = Descriptors.MolWt(mol)
logp = Descriptors.MolLogP(mol)

# Generate 2D coordinates
AllChem.Compute2DCoords(mol)

# Generate 3D conformer
mol3d = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol3d)

# Substructure search
pattern = Chem.MolFromSmarts('c1ccccc1')
mol.HasSubstructMatch(pattern)

# Save as image
Draw.MolToFile(mol, 'molecule.png')
```

# INPUT FORMATS

```
SMILES - Chem.MolFromSmiles()
SDF    - Chem.SDMolSupplier()
MOL    - Chem.MolFromMolFile()
```

# CAVEATS

Python 库通过 conda 或 pip 安装（`pip install rdkit`）。需要 numpy。也提供 C++ 库版本。某些功能需要额外的可选依赖，例如绘图需要 matplotlib。

# HISTORY

RDKit 由 **Greg Landrum** 在 Rational Discovery 发起，于 2006 年开源发布。

# INSTALL

```pacman: sudo pacman -S rdkit```

```brew: brew install rdkit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[obabel](/man/obabel)(1), [pymol](/man/pymol)(1), [python](/man/python)(1), [conda](/man/conda)(1)
