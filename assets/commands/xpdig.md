# TAGLINE

像 k9s 一样探索 Crossplane 追踪信息的 TUI

# TLDR

**启动 Crossplane 追踪浏览器**

```xpdig```

**指定 kubeconfig 文件**

```xpdig --kubeconfig [~/.kube/config]```

# SYNOPSIS

**xpdig** [_options_]

# DESCRIPTION

**xpdig** 提供一个类似 k9s 的终端 UI，用于交互式地探索 Crossplane 资源追踪信息。它支持带问题高亮的展开详情，可以对对象执行 get、describe、edit 和 delete 操作，并能自动监视资源变化。

# HISTORY

**xpdig** 由 **Bruno Luiz Silva**（brunoluiz）创建，使用 **Go** 编写。

# SEE ALSO

[k9s](/man/k9s)(1), [kubectl](/man/kubectl)(1)
