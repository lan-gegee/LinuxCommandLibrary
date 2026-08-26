# TAGLINE

重新启用已冻结的流水线阶段

# TLDR

**解冻一个阶段**

```dvc unfreeze [stage_name]```

**解冻文件中的所有阶段**

```dvc unfreeze [dvc.yaml]```

# SYNOPSIS

**dvc** **unfreeze** [_options_] _targets_...

# DESCRIPTION

**dvc unfreeze** 解除之前冻结的流水线阶段，使其可以在 dvc repro 期间再次执行。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc-freeze](/man/dvc-freeze)(1)
