# TAGLINE

为 kubectl 输出添加颜色

# TLDR

**运行 kubectl 命令**并带彩色输出

```kubecolor get pods```

**以浅色背景主题**获取资源

```kubecolor get pods --light-background```

**用颜色描述资源**

```kubecolor describe pod [pod_name]```

# SYNOPSIS

**kubecolor** [_kubectl_arguments_...]

# PARAMETERS

**--light-background**
> 使用针对浅色终端背景优化的配色方案。

**--force-colors**
> 即使未写入终端也强制彩色输出。

**--kubecolor-theme** _THEME_
> 选择颜色主题。包含针对绿色盲（deuteranopia）和蓝色盲（tritanopia）调整的主题。

# DESCRIPTION

**kubecolor** 是一个 kubectl 包装器，为 kubectl 输出添加颜色。它在内部调用 kubectl 并对响应进行着色，因此可以通过将 `kubectl` 别名指向 `kubecolor` 来作为无缝替代品使用。

当输出被管道传输或重定向到文件时，着色会自动禁用，以确保与脚本和其他命令的兼容性。只有读取类命令（get、describe 等）会被着色；写入类命令（apply、edit、exec）原样透传，不做修改。

# CONFIGURATION

**别名设置**
> 在 Shell 配置文件中添加 `alias kubectl="kubecolor"` 即可实现无缝集成。

# CAVEATS

需要已安装并配置好 kubectl。只对读取类操作的输出着色。某些自定义输出格式可能无法正确着色。

# HISTORY

**kubecolor** 最初由 **Hidetatsu Yaginuma**（hidetatz）创建，使用 **Go** 编写。该项目现由 GitHub 上的 **kubecolor** 组织维护。

# INSTALL

```apt: sudo apt install kubecolor```

```zypper: sudo zypper install kubecolor```

```brew: brew install kubecolor```

```nix: nix profile install nixpkgs#kubecolor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [k9s](/man/k9s)(1)
