# TAGLINE

验证 Android App Bundle 文件

# TLDR

**验证一个 Android App Bundle**

```bundletool validate --bundle=[app.aab]```

# SYNOPSIS

**bundletool** **validate** **--bundle**=_path_

# PARAMETERS

**--bundle** _path_
> 要验证的 Android App Bundle（.aab）文件的路径。

# DESCRIPTION

**bundletool validate** 检查 Android App Bundle（.aab）文件在结构上是否有效，是否符合 App Bundle 格式规范。它会验证 bundle 的内部结构、清单文件和配置。

这有助于在上传到 Google Play 或其他应用分发商店之前发现问题。

# CAVEATS

需要 Java 运行时环境（JRE）11 或更高版本。验证仅针对结构；它不会验证运行时行为或业务逻辑。

# INSTALL

```brew: brew install bundletool```

```nix: nix profile install nixpkgs#bundletool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bundletool](/man/bundletool)(1), [bundletool-dump](/man/bundletool-dump)(1)

# RESOURCES

```[Source code](https://github.com/google/bundletool)```

```[Documentation](https://developer.android.com/tools/bundletool)```

<!-- verified: 2026-06-22 -->
