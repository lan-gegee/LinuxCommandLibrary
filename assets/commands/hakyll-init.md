# TAGLINE

创建具有基本结构的新 Hakyll 静态网站项目

# TLDR

**创建新的 Hakyll 网站**

```hakyll-init [my-site]```

**在当前目录创建**

```hakyll-init .```

# SYNOPSIS

**hakyll-init** _directory_

# DESCRIPTION

**hakyll-init** 创建一个具有基本结构的新 Hakyll 静态网站项目。Hakyll 是基于 Haskell 的静态网站生成器，集成了 Pandoc。生成的项目包括 site.hs（主配置）、templates、CSS、示例文章和图片。初始化完成后，用 GHC 编译 site.hs，再使用得到的二进制文件来构建和托管网站。

# INSTALL

```apt: sudo apt install libghc-hakyll-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hugo](/man/hugo)(1), [jekyll](/man/jekyll)(1), [ghc](/man/ghc)(1), [cabal](/man/cabal)(1), [stack](/man/stack)(1)
