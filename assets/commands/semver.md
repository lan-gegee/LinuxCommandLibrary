# TAGLINE

校验并操作语义化版本字符串

# TLDR

**检查版本是否有效**

```semver [1.2.3]```

**递增主版本号**

```semver -i major [1.2.3]```

**递增次版本号**

```semver -i minor [1.2.3]```

**递增修订号**

```semver -i patch [1.2.3]```

**比较版本**

```semver -r "[>=1.0.0 <2.0.0]" [1.5.0]```

**强制转换不规范版本字符串**

```semver -c [v1.2]```

**带标识符递增预发布版本**

```semver -i prerelease --preid [beta] [1.2.3]```

**对版本排序**

```semver [1.2.3] [1.0.0] [2.0.0]```

# SYNOPSIS

**semver** [_options_] _version_ [_version_ ...]

# PARAMETERS

**-i**, **--increment** _TYPE_
> 按指定级别递增版本。默认级别为 patch。

**-r**, **--range** _RANGE_
> 输出匹配指定范围的版本。

**-c**, **--coerce**
> 尽可能将字符串强制转换为有效的 semver。

**-l**, **--loose**
> 以宽松方式解释版本和范围。

**-p**, **--include-prerelease**
> 在范围匹配中始终包含预发布版本。

**--preid** _IDENTIFIER_
> 预发布版本递增时使用的标识符。

**-n** _BASE_
> 预发布标识符的基数（0 或 1）。

**--rtl**
> 从右到左转换版本字符串。

**--ltr**
> 从左到右转换版本字符串（默认）。

# INCREMENT TYPES

**major** - 1.2.3 -> 2.0.0
**minor** - 1.2.3 -> 1.3.0
**patch** - 1.2.3 -> 1.2.4
**premajor** - 1.2.3 -> 2.0.0-0
**preminor** - 1.2.3 -> 1.3.0-0
**prepatch** - 1.2.3 -> 1.2.4-0
**prerelease** - 1.2.3 -> 1.2.4-0

# DESCRIPTION

**semver** 遵循 semver.org 规范，用于校验、比较和操作语义化版本字符串。它提供版本递增功能（提升 major、minor、patch 或 prerelease 组件）、基于 NPM 风格范围语法的范围匹配，以及版本排序。

范围匹配用于测试版本是否满足诸如 **>=1.0.0 <2.0.0**、**^1.2.3** 或 **~1.2.3** 之类的约束，其范围语法与 npm 的 package.json 版本说明符相同。强制转换可将 "v1.2" 这类不规范的版本字符串转换为有效的 semver 格式（1.2.0）。作为参数传入的多个版本会按排序后的顺序输出。

# CAVEATS

这是一个 Node.js 软件包。严格模式可能会拒绝看似合法的版本。范围语法可能较为复杂。

# HISTORY

**semver** 是语义化版本规范的 Node.js 实现，npm 使用它进行软件包版本解析。

# INSTALL

```pacman: sudo pacman -S semver```

```brew: brew install semver```

```nix: nix profile install nixpkgs#semver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [node](/man/node)(1)
