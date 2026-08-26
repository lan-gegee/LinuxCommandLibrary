# TAGLINE

管理 Maven 依赖的 goals

# TLDR

**显示依赖树**

```mvn dependency:tree```

**分析依赖**

```mvn dependency:analyze```

**列出依赖**

```mvn dependency:list```

**复制依赖**

```mvn dependency:copy-dependencies```

**解析依赖**

```mvn dependency:resolve```

显示冲突解决细节的**详细依赖树**

```mvn dependency:tree -Dverbose```

按 scope **过滤依赖树**

```mvn dependency:tree -Dscope=[compile]```

**清除本地副本**并重新解析

```mvn dependency:purge-local-repository```

# SYNOPSIS

**mvn** **dependency:**_goal_ [_options_]

# PARAMETERS

_GOAL_
> Dependency 插件的 goal。

**tree**
> 显示依赖树。

**analyze**
> 分析已使用/未使用的依赖。

**list**
> 列出所有依赖。

**copy-dependencies**
> 将依赖复制到 target。

**resolve**
> 解析并将所有依赖下载到本地仓库。

**purge-local-repository**
> 从本地仓库移除项目依赖，并可选地重新解析它们。

**-Dscope** _SCOPE_
> 按依赖 scope 过滤（compile、runtime、test、provided、system）。

**-Dincludes** _PATTERN_
> 将输出过滤为匹配的构件（groupId:artifactId:type:version 模式，支持通配符）。

**-DoutputFile** _FILE_
> 将输出写入文件而非标准输出（tree、list、resolve 支持）。

# DESCRIPTION

**maven-dependency-plugin** 提供用于分析、列出、复制和解析 Maven 项目依赖的 goals。其中 **tree** goal 最常用，它显示完整的传递依赖树，启用 **-Dverbose** 时还会显示冲突解决细节。**analyze** goal 用于识别已声明但未使用的依赖，以及已使用但未显式声明的依赖。

# CAVEATS

需要有效的 **pom.xml**。首次解析需要网络访问。**analyze** goal 无法检测仅通过反射使用的依赖。

# HISTORY

Maven Dependency Plugin 是 **Apache Maven** 的组成部分，自早期 Maven 版本起就提供依赖分析功能。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```apk: sudo apk add maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [mvn-deploy](/man/mvn-deploy)(1), [gradle](/man/gradle)(1)
