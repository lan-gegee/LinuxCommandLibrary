# TAGLINE

理解 YAML 结构的 YAML 模板工具

# TLDR

**渲染**模板

```ytt -f [template.yml]```

**覆盖**数据值

```ytt -f [template.yml] --data-value [key=value]```

**多个**文件/目录

```ytt -f [config/] -f [values.yml]```

**输出**到文件

```ytt -f [template.yml] > [out.yml]```

# SYNOPSIS

**ytt** [*options*]

# DESCRIPTION

**ytt**（来自 Carvel）通过操作 YAML 结构而非原始文本来模板化 YAML，减少了字符串模板常见的缩进错误。它支持数据值、叠加（overlay）、函数和模块化库——与 **kapp** 和 **kbld** 一起常用于 Kubernetes 清单。

文档：https://carvel.dev/ytt/

# PARAMETERS

**-f**, **--file** *path*

> 模板或数据文件/目录（可重复）。

**--data-value** *key=value*

> 设置一个数据值。

**--data-values-file** *path*

> 从 YAML 加载数据值。

**--output-files** *dir*

> 将结果写为文件。

严格模式、警告和库路径见 **ytt --help**。

# CAVEATS

学习曲线与 Helm/Go 模板不同。无效的 YAML 输入会导致直接失败。可与 **kapp** 组合构建部署工作流。

# INSTALL

```brew: brew install ytt```

```nix: nix profile install nixpkgs#ytt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kapp](/man/kapp)(1), [helm](/man/helm)(1), [gomplate](/man/gomplate)(1), [kustomize](/man/kustomize)(1)

# RESOURCES

```[Source code](https://github.com/carvel-dev/ytt)```

```[Homepage](https://carvel.dev/ytt/)```

```[Documentation](https://carvel.dev/ytt/docs/)```

<!-- verified: 2026-07-19 -->
