# TAGLINE

持续集成与交付服务器

# TLDR

**启动 Jenkins**

```java -jar jenkins.war```

**在指定端口启动**

```java -jar jenkins.war --httpPort=[8888]```

**以守护进程方式运行**

```java -jar jenkins.war &```

**指定主目录**

```JENKINS_HOME=[/var/jenkins] java -jar jenkins.war```

**使用 HTTPS**

```java -jar jenkins.war --httpsPort=[8443] --httpsKeyStore=[keystore.jks]```

# SYNOPSIS

**java -jar jenkins.war** [_options_]

# PARAMETERS

**--httpPort** _PORT_
> HTTP 端口（默认 8080）。

**--httpsPort** _PORT_
> HTTPS 端口。

**--httpsKeyStore** _FILE_
> SSL keystore 文件。

**--prefix** _PATH_
> URL 前缀。

**--daemon**
> 以守护进程方式运行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Jenkins** 是一款持续集成与交付服务器。它自动执行软件的构建、测试和部署。

该平台支持流水线、插件和分布式构建。它与版本控制系统和部署系统集成。

# CAVEATS

需要 Java。资源消耗较大。安全配置非常重要。

# HISTORY

Jenkins 于 2011 年由 **Kohsuke Kawaguchi** 从 **Hudson** 分支而来。它已成为领先的开源 CI/CD 服务器。

# INSTALL

```pacman: sudo pacman -S jenkins```

```brew: brew install jenkins```

```nix: nix profile install nixpkgs#jenkins```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[java](/man/java)(1), [docker](/man/docker)(1), [gitlab-runner](/man/gitlab-runner)(1)
