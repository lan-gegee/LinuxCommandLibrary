# TAGLINE

将构件上传到远程仓库

# TLDR

**部署到仓库**

```mvn deploy```

**部署指定文件**

```mvn deploy:deploy-file -Dfile=[file.jar] -DgroupId=[com.example] -DartifactId=[my-lib] -Dversion=[1.0] -Durl=[repo-url] -DrepositoryId=[repo-id]```

**以指定 profile 部署**

```mvn deploy -P [profile-name]```

**跳过测试并部署**

```mvn deploy -DskipTests```

**部署到备用仓库**

```mvn deploy -DaltDeploymentRepository=[id::url]```

**部署单个模块**

```mvn deploy -pl [module-name]```

# SYNOPSIS

**mvn** **deploy** [_options_]

# PARAMETERS

**-Dfile** _JAR_
> 要部署的文件。

**-DrepositoryId** _ID_
> 仓库标识符。

**-Durl** _URL_
> 仓库 URL。

**-DgroupId** _GROUP_
> deploy-file goal 的 Group ID。

**-DartifactId** _ARTIFACT_
> deploy-file goal 的 Artifact ID。

**-Dversion** _VERSION_
> deploy-file goal 的版本。

**-DaltDeploymentRepository** _id::url_
> 用于部署的备用仓库（格式：id::url）。

**-DskipTests**
> 构建期间跳过测试运行。

**-P** _PROFILE_
> 激活 profile。

**-pl** _MODULE_
> 构建指定模块。

# DESCRIPTION

**mvn deploy** 将构件上传到远程仓库。它是 Maven 生命周期的最后一个阶段。

该 goal 发布已构建的构件。需要在 settings.xml 中配置仓库信息。

# CAVEATS

需要仓库访问权限。凭据存放在 settings.xml 中。属于网络操作。

# HISTORY

deploy goal 是 **Apache Maven** 构建生命周期中用于分发构建产物的组成部分。

# INSTALL

```dnf: sudo dnf install maven```

```pacman: sudo pacman -S maven```

```apk: sudo apk add maven```

```zypper: sudo zypper install maven```

```brew: brew install maven```

```nix: nix profile install nixpkgs#maven```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mvn](/man/mvn)(1), [mvn-dependency](/man/mvn-dependency)(1), [gradle](/man/gradle)(1)
