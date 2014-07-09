%global _hardened_build 1
%global proj accumulo
%global longproj Apache Accumulo
# monitor not included until dependent javascript libs are packaged
%global include_monitor 0

%global commit 06162580e885f11863d1a6d22f952bce35b78b68
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     %{proj}
Version:  1.6.0
Release:  2%{?dist}
Summary:  A software platform for processing vast amounts of data
License:  ASL 2.0
Group:    Development/Libraries
URL:      http://%{name}.apache.org
Source0:  https://github.com/apache/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

# systemd service files
Source1:  %{name}-master.service
Source2:  %{name}-tserver.service
Source3:  %{name}-gc.service
Source4:  %{name}-tracer.service
%if %{include_monitor}
Source5:  %{name}-monitor.service
%endif

# Upstream patches needed for Fedora
Patch0: ACCUMULO-1691.patch
Patch1: ACCUMULO-2950.patch
Patch2: ACCUMULO-2773.patch
Patch3: ACCUMULO-2762.patch
Patch4: ACCUMULO-2812.patch
Patch5: ACCUMULO-2808.patch

# Should be applied after upstream patches
Patch6: commons-configuration.patch
Patch7: commons-math.patch
Patch8: native-code.patch
Patch9: disabled-tests.patch

# Accumulo depends on Hadoop, and Hadoop is not built for ARM
ExcludeArch: %{arm}

BuildRequires: apache-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-configuration
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-math
BuildRequires: apache-commons-vfs
BuildRequires: beust-jcommander
BuildRequires: bouncycastle
BuildRequires: exec-maven-plugin
BuildRequires: google-gson
BuildRequires: guava
BuildRequires: hadoop-client
BuildRequires: hadoop-tests
BuildRequires: java-devel
BuildRequires: jetty-security
BuildRequires: jetty-server
BuildRequires: jetty-servlet
BuildRequires: jetty-util
BuildRequires: jline2
BuildRequires: jpackage-utils
BuildRequires: libthrift-java
%if 0%{?fedora} < 21
BuildRequires: log4j
%else
BuildRequires: log4j12
%endif
BuildRequires: maven-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: native-maven-plugin
BuildRequires: powermock-api-easymock
BuildRequires: powermock-core
BuildRequires: powermock-junit4
BuildRequires: slf4j
BuildRequires: systemd-units
BuildRequires: zookeeper-java

Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-master = %{version}-%{release}
Requires: %{name}-tserver = %{version}-%{release}
Requires: %{name}-gc = %{version}-%{release}
%if %{include_monitor}
Requires: %{name}-monitor = %{version}-%{release}
%endif
Requires: %{name}-tracer = %{version}-%{release}
Requires: %{name}-examples = %{version}-%{release}
Requires: %{name}-native%{?_isa} = %{version}-%{release}

%description
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

%package core
Summary: Libraries for %{longproj} Java clients
# the bloom filter code is BSD licensed, everything else is ASL 2.0
License: ASL 2.0 and BSD
Group: Applications/System
BuildArch: noarch
Requires(pre): /usr/sbin/useradd

%description core
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides libraries for %{longproj} clients.

%package server-base
Summary: The %{longproj} Server Base libraries
License:  ASL 2.0
Group: Applications/System
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}

%description server-base
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides jars for other %{longproj} services.

%package master
Summary: The %{longproj} Master service
License:  ASL 2.0
Group: Applications/System
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-server-base = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description master
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides the master service for %{longproj}.

%package tserver
Summary: The %{longproj} TServer service
License:  ASL 2.0
Group: Applications/System
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-server-base = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description tserver
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides the tserver service for %{longproj}.

%package gc
Summary: The %{longproj} Garbage Collector service
License:  ASL 2.0
Group: Applications/System
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-server-base = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description gc
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides the gc service for %{longproj}.

%if %{include_monitor}
%package monitor
Summary: The %{longproj} Monitor service
# jquery and flot are MIT licensed, everything else is ASL 2.0
License: ASL 2.0 and MIT
Group: Applications/System
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-server-base = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description monitor
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides the monitor service for %{longproj}.
%endif

%package tracer
Summary: The %{longproj} Tracer service
License:  ASL 2.0
Group: Applications/System
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-server-base = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description tracer
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides the tracer service for %{longproj}.

%package examples
Summary: Examples for %{longproj}
License:  ASL 2.0
Group: Applications/System
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}

%description examples
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides examples for %{longproj}.

%package native
Summary: Native libraries for %{longproj}
License:  ASL 2.0
Group: Development/Libraries
Requires: %{name}-tserver = %{version}-%{release}

%description native
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides native code for %{longproj}'s TServer.

%package javadoc
Summary: Javadoc for %{longproj}
License:  ASL 2.0
Group: Documentation
BuildArch: noarch

%description javadoc
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package contains the API documentation for %{longproj}.

%prep
%setup -qn %{name}-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

# Update dependency versions
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='jline']/pom:version" "2.10"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='zookeeper']/pom:version" "3.4.5"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='libthrift']/pom:version" "0.9.1"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='log4j']/pom:version" "1.2.17"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='commons-math']/pom:version" "3.2"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='commons-math']/pom:artifactId" "commons-math3"
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId='commons-math']/pom:artifactId" "commons-math3" core
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='bcprov-jdk15on']/pom:artifactId" "bcprov-jdk16"

# Fix javadoc
%pom_xpath_remove "pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:reportOutputDirectory"

# No need to deploy site with ssh
%pom_xpath_remove "pom:project/pom:build/pom:extensions/pom:extension[pom:artifactId='wagon-ssh']"

# Disable unneeded modules
%pom_disable_module test
%pom_disable_module proxy
%pom_disable_module maven-plugin
%pom_disable_module docs
%pom_disable_module assemble
%if !%{include_monitor}
%pom_disable_module server/monitor
%endif

# Remove unneeded plugins
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-sortpom-plugin
%pom_remove_plugin :mavanagaiata
%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-project-info-reports-plugin

%mvn_package ":%{name}-minicluster" __noinstall
%mvn_package ":%{name}-{project,core,fate,trace,start}" core
%mvn_package ":%{name}-examples-simple" examples
%mvn_package ":%{name}-gc" gc
%mvn_package ":%{name}-master" master
%if %{include_monitor}
%mvn_package ":%{name}-monitor" monitor
%endif
%mvn_package ":%{name}-server-base" server-base
%mvn_package ":%{name}-tracer" tracer
%mvn_package ":%{name}-tserver" tserver

%mvn_package ":%{name}-native" __noinstall

%build
# TODO Unit tests are skipped, because upstream tries to do some integration
# testing in the unit tests, and they expect certain resources and dependencies
# that are not typically available, or are too complicated to configure,
# especially in the start jar. These should be enabled when possible.
# ITs are skipped, because they time out frequently and take too many resources
# to run reliably. Failures do not reliably indicate meaningful issues.
%mvn_build -- -DforkCount=1C -DskipTests -DskipITs

%install
%mvn_install

# native libs
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -d -m 755 %{buildroot}%{_var}/cache/%{name}
cp -af server/native/target/%{name}-native-%{version}/%{name}-native-%{version}/lib%{name}.so %{buildroot}%{_libdir}/%{name}

# upstream scripts and config
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}
cp -af bin/%{name} bin/config.sh %{buildroot}%{_libexecdir}/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
bin/bootstrap_config.sh -o -d %{buildroot}%{_sysconfdir}/%{name} -s 3GB -n -v 2
for x in gc masters monitor slaves tracers; do rm -f %{buildroot}%{_sysconfdir}/%{name}/$x; done

# service shortcut files
install -d -m 755 %{buildroot}%{_bindir}
cat <<EOF >"%{name}"
#! /usr/bin/bash
[[ \$ACCUMULO_CONF_DIR ]] || export ACCUMULO_CONF_DIR=/%{_sysconfdir}/%{name}
%{_libexecdir}/%{name}/%{name} \$@
EOF
install -p -m 755 %{name} %{buildroot}%{_bindir}

%if %{include_monitor}
for service in master tserver shell init admin gc monitor tracer classpath version rfile-info login-info zookeeper create-token info jar; do
%else
for service in master tserver shell init admin gc tracer classpath version rfile-info login-info zookeeper create-token info jar; do
%endif
  cat <<EOF >"%{name}-$service"
#! /usr/bin/bash
%{_bindir}/%{name} $service
EOF
  install -p -m 755 %{name}-$service %{buildroot}%{_bindir}
done

# systemd services
install -d -m 755 %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}-master.service
install -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-tserver.service
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}-gc.service
install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}-tracer.service
%if %{include_monitor}
install -p -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}-monitor.service
%endif

%files

%files core -f .mfiles-core
%doc CHANGES
%doc LICENSE
%doc README
%doc NOTICE
%dir %{_javadir}/%{name}
%dir %{_libexecdir}/%{name}
%if 0%{?fedora} > 20
%dir %{_mavenpomdir}/%{name}
%endif
%{_libexecdir}/%{name}/%{name}
%{_libexecdir}/%{name}/config.sh
%{_bindir}/%{name}
%{_bindir}/%{name}-shell
%{_bindir}/%{name}-classpath
%{_bindir}/%{name}-version
%{_bindir}/%{name}-rfile-info
%{_bindir}/%{name}-login-info
%{_bindir}/%{name}-zookeeper
%{_bindir}/%{name}-create-token
%{_bindir}/%{name}-info
%{_bindir}/%{name}-jar
%attr(0750, %{name}, -) %dir %{_var}/cache/%{name}
%attr(0750, %{name}, -) %dir %{_sysconfdir}/%{name}
%attr(0750, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/accumulo-env.sh
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/accumulo-metrics.xml
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/accumulo.policy.example
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/accumulo-site.xml
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/auditLog.xml
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/generic_logger.xml
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/log4j.properties
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/monitor_logger.xml

%files server-base -f .mfiles-server-base
%{_bindir}/%{name}-init
%{_bindir}/%{name}-admin

%files master -f .mfiles-master
%{_bindir}/%{name}-master
%{_unitdir}/%{name}-master.service

%files tserver -f .mfiles-tserver
%dir %{_jnidir}/%{name}
%{_bindir}/%{name}-tserver
%{_unitdir}/%{name}-tserver.service

%files gc -f .mfiles-gc
%{_bindir}/%{name}-gc
%{_unitdir}/%{name}-gc.service

%if %{include_monitor}
%files monitor -f .mfiles-monitor
%{_bindir}/%{name}-monitor
%{_unitdir}/%{name}-monitor.service
%endif

%files tracer -f .mfiles-tracer
%{_bindir}/%{name}-tracer
%{_unitdir}/%{name}-tracer.service

%files examples -f .mfiles-examples

%files javadoc -f .mfiles-javadoc

%files native
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so

%preun master
%systemd_preun %{name}-master.service

%preun tserver
%systemd_preun %{name}-tserver.service

%preun gc
%systemd_preun %{name}-gc.service

%preun tracer
%systemd_preun %{name}-tracer.service

%if %{include_monitor}
%preun monitor
%systemd_preun %{name}-monitor.service
%endif

%postun master
%systemd_postun_with_restart %{name}-master.service

%postun tserver
%systemd_postun_with_restart %{name}-tserver.service

%postun gc
%systemd_postun_with_restart %{name}-gc.service

%postun tracer
%systemd_postun_with_restart %{name}-tracer.service

%if %{include_monitor}
%postun monitor
%systemd_postun_with_restart %{name}-monitor.service
%endif

%pre core
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || /usr/sbin/useradd --comment "%{longproj}" --shell /sbin/nologin -M -r -g %{name} --home %{_var}/cache/%{name} %{name}

%post master
%systemd_post %{name}-master.service

%post tserver
%systemd_post %{name}-tserver.service

%post gc
%systemd_post %{name}-gc.service

%post tracer
%systemd_post %{name}-tracer.service

%if %{include_monitor}
%post monitor
%systemd_post %{name}-monitor.service
%endif

%changelog
* Wed Jul  9 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.0-2
- Add conditional for pom directory to build for f20
- Remove fno-strict-aliasing flag based on upstream ACCUMULO-2762

* Wed Apr 30 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.0-1
- Initial packaging
