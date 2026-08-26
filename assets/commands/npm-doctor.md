# TAGLINE

运行诊断以检查 npm 环境健康状况

# TLDR

**运行 npm 环境诊断**

```npm doctor```

**使用指定的 registry 运行**

```npm doctor --registry [https://registry.npmjs.org]```

# SYNOPSIS

**npm** **doctor** [_--registry registry_]

# DESCRIPTION

**npm doctor** 运行一组诊断来验证 npm 环境是否健康。它会检查：npm 能否访问所配置的 registry、已安装的 node 和 npm 版本是否受支持、npm 缓存是否损坏、全局和本地 bin 目录是否存在且位于 **PATH** 中、包树的所有权是否正确，以及 git 可执行文件是否可用。

每项检查都会报告为 **OK** 或显示具体问题。任何一项检查失败时，退出码为非零。

# CAVEATS

部分检查需要网络访问。在受限系统（CI、隔离网络）上，registry 连通性检查会失败。缓存较大时校验可能很慢。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-cache](/man/npm-cache)(1), [npm-install](/man/npm-install)(1)
