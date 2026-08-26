# TAGLINE

停用当前的 conda 环境

# TLDR

**停用当前环境**

```conda deactivate```

# SYNOPSIS

**conda** **deactivate**

# DESCRIPTION

**conda deactivate** 退出当前活动的 conda 环境，撤销 conda activate 对 shell 所做的修改。这会将 PATH 和环境变量恢复到先前的状态——要么回到 base conda 环境，要么在通过多次激活调用嵌套环境的情况下，回到上一个活动的环境。

停用过程会将当前环境的 bin 目录从 PATH 中移除，取消设置 CONDA_PREFIX 等环境专属变量，并执行软件包可能安装的任何停用脚本。shell 提示符通常也会随之更新，移除环境名称标识，直观地确认环境已被停用。

与某些需要显式清理的环境管理系统不同，conda deactivate 可以随时安全调用，状态管理都在内部处理。如果当前除 base 环境外没有其他活动环境，停用后就会回到非 conda 的 shell 状态。Conda 支持环境嵌套，因此多次 activate 调用可以用对应的 deactivate 调用逐层回退，不过这属于进阶用法。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-activate](/man/conda-activate)(1), [conda-create](/man/conda-create)(1), [conda-env](/man/conda-env)(1)
