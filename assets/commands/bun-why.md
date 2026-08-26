# TAGLINE

显示包为何被安装

# TLDR

**显示包为何被安装**

```bun why [package]```

# SYNOPSIS

**bun** **why** _package_

# DESCRIPTION

**bun why** 显示项目中某个包为何被安装。它会列出指向该包的依赖链，标明哪些包直接或间接依赖它。

这有助于理解为什么某个包出现在 node_modules 中，对分析间接依赖尤其有用。

# SEE ALSO

[bun](/man/bun)(1), [bun-list](/man/bun-list)(1), [npm-explain](/man/npm-explain)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
