# TAGLINE

防止流水线阶段被自动重新执行

# TLDR

**冻结一个阶段**

```dvc freeze [stage_name]```

**冻结多个阶段**

```dvc freeze [stage1] [stage2]```

**冻结并显示详细输出**

```dvc freeze -v [stage_name]```

# SYNOPSIS

**dvc** **freeze** [_-h_] [_-q_] [_-v_] _targets_...

# PARAMETERS

_targets_
> 要冻结的阶段名或 .dvc 文件。

**-h**, **--help**
> 显示帮助消息并退出。

**-q**, **--quiet**
> 不向标准输出写入任何内容。

**-v**, **--verbose**
> 显示详细的跟踪信息。

# DESCRIPTION

**dvc freeze** 冻结流水线阶段，使 **dvc status** 将其视为未更改，且在 **dvc repro** 期间不会被重新执行。即使其依赖项发生了变化，已冻结的阶段也不会重新生成输出，即使使用 **--force** 也是如此。

在流水线的下游阶段进行迭代时，冻结可用于避免重新运行开销较大的上游阶段。

# CAVEATS

即使依赖项发生变化，已冻结的阶段也不会被重现。使用 **dvc unfreeze** 可恢复正常行为。冻结状态以 `frozen: true` 字段的形式存储在阶段对应的 **dvc.yaml** 文件中。在 DVC 2.0 及以上版本，你也可以直接在 **dvc.yaml** 中手动设置该字段，而不使用此命令。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc-unfreeze](/man/dvc-unfreeze)(1), [dvc](/man/dvc)(1)
