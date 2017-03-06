%global _hardened_build 1
%global longproj Apache Accumulo

# jpackage main class
%global main_class org.apache.%{name}.start.Main

Name:    accumulo
Version: 1.8.1
Release: 1%{?dist}
Summary: A software platform for processing vast amounts of data
License: ASL 2.0
Group:   Development/Libraries
URL:     https://%{name}.apache.org
Source0: https://www.apache.org/dist/%{name}/%{version}/%{name}-%{version}-src.tar.gz

# systemd service files
Source1: %{name}-master.service
Source2: %{name}-tserver.service
Source3: %{name}-gc.service
Source4: %{name}-tracer.service
Source5: %{name}-monitor.service

# Java configuration file for Fedora
Source6: %{name}.conf

# Apply Fedora JNI conventions
Patch3: native-code.patch
# Patch upstream-provided example configuration for Fedora
Patch5: default-conf.patch
# Fix for updating to flot 0.8 from 0.7 (adds flot.time)
Patch8: flot8.patch
# Workaround for https://github.com/jline/jline2/issues/205
Patch9: jline-shell-workaround.patch
# Fix version number in thrift script
Patch10: thrift-0.10.0.patch
# Fix differences with guava version
Patch11: guava.patch

BuildRequires: apache-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-configuration
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-math
%if 0%{?fedora} > 24
BuildRequires: apache-commons-vfs >= 2.1-7
%else
BuildRequires: apache-commons-vfs < 2.1
%endif
BuildRequires: auto-service
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
BuildRequires: log4j12
BuildRequires: maven-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: native-maven-plugin
BuildRequires: powermock-api-easymock
BuildRequires: powermock-core
BuildRequires: powermock-junit4
BuildRequires: slf4j
BuildRequires: systemd-units
BuildRequires: thrift
BuildRequires: zookeeper-java

Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-master = %{version}-%{release}
Requires: %{name}-tserver = %{version}-%{release}
Requires: %{name}-gc = %{version}-%{release}
Requires: %{name}-monitor = %{version}-%{release}
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
Obsoletes: %{name}-javadoc < 1.6.0-5%{?dist}

%description core
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides libraries for %{longproj} clients.

%package server-base
Summary: The %{longproj} Server Base libraries
License: ASL 2.0
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
License: ASL 2.0
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
License: ASL 2.0
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
License: ASL 2.0
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

%package monitor
Summary: The %{longproj} Monitor service
License: ASL 2.0
Group: Applications/System
BuildArch: noarch
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-server-base = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: nodejs-flot
Requires: js-jquery1

%description monitor
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides the monitor service for %{longproj}.

%package tracer
Summary: The %{longproj} Tracer service
License: ASL 2.0
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
License: ASL 2.0
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
License: ASL 2.0
Group: Development/Libraries
Requires: %{name}-tserver = %{version}-%{release}

%description native
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides native code for %{longproj}'s TServer.

%package shell
Summary: Shell for %{longproj}
License: ASL 2.0
Group: Development/Libraries
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-tserver = %{version}-%{release}

%description shell
  %{longproj} is a sorted, distributed key/value store based on Google's
BigTable design. It is built on top of Apache Hadoop, Zookeeper, and Thrift. It
features a few novel improvements on the BigTable design in the form of
cell-level access labels and a server-side programming mechanism that can
modify key/value pairs at various points in the data management process.

This package provides the shell service for %{longproj}.

%prep
%autosetup -p1
# Remove flot and jquery bundling from upstream tarball
rm -rf server/monitor/src/main/resources/web/flot/

# Update dependency versions
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='jline']/pom:version" "2.10"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='zookeeper']/pom:version" "3.4.5"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='libthrift']/pom:version" "0.10.0"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='log4j']/pom:version" "1.2.17"
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='bcprov-jdk15on']/pom:artifactId" "bcprov-jdk16"

# Remove enforcer animal-sniffer rule
%pom_xpath_remove "pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-enforcer-plugin']/pom:dependencies"
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-enforcer-plugin']/pom:executions/pom:execution[pom:id='enforce-java-signatures']"

# Disable unneeded/unused modules
%pom_disable_module test
%pom_disable_module proxy
%pom_disable_module maven-plugin
%pom_disable_module docs
%pom_disable_module assemble
# Mini isn't needed
%pom_disable_module minicluster
%pom_disable_module iterator-test-harness

# Remove unneeded plugins
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :sortpom-maven-plugin
%pom_remove_plugin :mavanagaiata
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-java-formatter-plugin
%pom_remove_plugin :modernizer-maven-plugin
%pom_remove_plugin :apilyzer-maven-plugin core

# Mini isn't needed
#%%mvn_package ":%%{name}-minicluster" __noinstall
%mvn_package ":%{name}-{project,core,fate,trace,start}" core
%mvn_package ":%{name}-examples-simple" examples
%mvn_package ":%{name}-gc" gc
%mvn_package ":%{name}-master" master
%mvn_package ":%{name}-monitor" monitor
%mvn_package ":%{name}-server-base" server-base
%mvn_package ":%{name}-tracer" tracer
%mvn_package ":%{name}-tserver" tserver
%mvn_package ":%{name}-shell" shell

# build native, but skip install; JNI *.so is copied manually
%mvn_package ":%{name}-native" __noinstall

%build
# TODO Unit tests are skipped, because upstream tries to do some integration
# testing in the unit tests, and they expect certain resources and dependencies
# that are not typically available, or are too complicated to configure,
# especially in the start jar. These should be enabled when possible.
# ITs are skipped, because they time out frequently and take too many resources
# to run reliably. Failures do not reliably indicate meaningful issues.
%mvn_build -j -- -Pthrift -DforkCount=1C -DskipTests -DskipITs

%install
%mvn_install

# create symlink for system-provided web assets to be added to classpath
install -d -m 755 %{buildroot}%{_datadir}/%{name}/lib/web
rm -f %{buildroot}%{_datadir}/%{name}/lib/web/flot
ln -s %{_usr}/lib/node_modules/flot %{buildroot}%{_datadir}/%{name}/lib/web/flot

# native libs
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -d -m 755 %{buildroot}%{_var}/cache/%{name}
install -p -m 755 server/native/target/%{name}-native-%{version}/%{name}-native-%{version}/lib%{name}.so %{buildroot}%{_libdir}/%{name}

# generate default config for Fedora from upstream examples
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/lib
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}/lib/ext
assemble/bin/bootstrap_config.sh -o -d %{buildroot}%{_sysconfdir}/%{name} -s 3GB -n -v 2
for x in gc masters monitor slaves tracers %{name}-env.sh generic_logger.xml generic_logger.properties monitor_logger.xml monitor_logger.properties %{name}.policy.example; do rm -f %{buildroot}%{_sysconfdir}/%{name}/$x; done
cp %{buildroot}%{_sysconfdir}/%{name}/log4j.properties %{buildroot}%{_sysconfdir}/%{name}/generic_logger.properties
cp %{buildroot}%{_sysconfdir}/%{name}/log4j.properties %{buildroot}%{_sysconfdir}/%{name}/monitor_logger.properties

# main launcher
%jpackage_script %{main_class} "" "" %{name}:%{name}/%{name}-tserver:jetty:servlet:avro/avro:apache-commons-io:apache-commons-cli:apache-commons-codec:apache-commons-collections:apache-commons-configuration:apache-commons-lang:apache-commons-logging:apache-commons-math:apache-commons-vfs:beust-jcommander:google-gson:guava:hadoop/hadoop-auth:hadoop/hadoop-common:hadoop/hadoop-hdfs:jansi/jansi:jline/jline:libthrift:log4j-1.2.17:slf4j/slf4j-api:slf4j/slf4j-log4j12:zookeeper/zookeeper:protobuf-java:jackson/jackson-mapper-asl:jackson/jackson-core-asl:htrace/htrace-core %{name} true
# fixup the generated jpackage script
sed -i -e 's/^#!\/bin\/sh$/#!\/usr\/bin\/bash/' %{buildroot}%{_bindir}/%{name}
# ensure the java configuration options know which service is being called
sed -i -e 's/^\s*\.\s\s*\/etc\/java\/'%{name}'\.conf/& "\$1"/' %{buildroot}%{_bindir}/%{name}
sed -i -e 's/^\s*\.\s\s*\$HOME\/\.'%{name}'rc$/& "\$1"/' %{buildroot}%{_bindir}/%{name}
# options may have spaces in them, so replace run with an exec that properly
# parses arguments as arrays.
sed -i -e '/^run .*$/d' %{buildroot}%{_bindir}/%{name}
sed -i -e '/^set_flags .*$/d' %{buildroot}%{_bindir}/%{name}
sed -i -e '/^set_options .*$/d' %{buildroot}%{_bindir}/%{name}
cat <<EOF >>%{buildroot}%{_bindir}/%{name}
CLASSPATH="%{_sysconfdir}/%{name}:%{_datadir}/%{name}/lib/:\${CLASSPATH}"
set_javacmd

if [ -n "\${VERBOSE}" ]; then
  echo "Java virtual machine used: \${JAVACMD}"
  echo "classpath used: \${CLASSPATH}"
  echo "main class used: \${MAIN_CLASS}"
  echo "flags used: \${FLAGS[*]}"
  echo "options used: \${ACCUMULO_OPTS[*]}"
  echo "arguments used: \${*}"
fi

export CLASSPATH
exec "\${JAVACMD}" "\${FLAGS[@]}" "\${ACCUMULO_OPTS[@]}" "\${MAIN_CLASS}" "\${@}"
EOF

# scripts for services/utilities
for service in master tserver shell init admin gc tracer classpath version rfile-info login-info zookeeper create-token info jar; do
  cat <<EOF >"%{name}-$service"
#!/usr/bin/bash
echo "%{name}-$service script is deprecated. Use '%{name} $service' instead." 1>&2
%{_bindir}/%{name} $service "\$@"
EOF
  install -p -m 755 %{name}-$service %{buildroot}%{_bindir}
done

# systemd services
install -d -m 755 %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}-master.service
install -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-tserver.service
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}-gc.service
install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}-tracer.service
install -p -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}-monitor.service

# java configuration file for Fedora
install -d -m 755 %{buildroot}%{_javaconfdir}
install -p -m 755 %{SOURCE6} %{buildroot}%{_javaconfdir}/%{name}.conf

%files
%doc LICENSE
%doc README.md
%doc NOTICE

%files core -f .mfiles-core
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
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
%attr(0755, %{name}, -) %dir %{_sysconfdir}/%{name}
%attr(0755, %{name}, -) %dir %{_sysconfdir}/%{name}/lib
%attr(0755, %{name}, -) %dir %{_sysconfdir}/%{name}/lib/ext
%attr(0755, %{name}, -) %config(noreplace) %{_javaconfdir}/%{name}.conf
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/%{name}-metrics.xml
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/%{name}-site.xml
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/auditLog.xml
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/generic_logger.properties
%attr(0644, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/log4j.properties
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/monitor_logger.properties
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/client.conf
%attr(0640, %{name}, -) %config(noreplace) %{_sysconfdir}/%{name}/hadoop-metrics2-accumulo.properties


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

%files monitor -f .mfiles-monitor
%dir %{_datadir}/%{name}/lib/web
%{_datadir}/%{name}/lib/web/flot
%{_unitdir}/%{name}-monitor.service

%files tracer -f .mfiles-tracer
%{_bindir}/%{name}-tracer
%{_unitdir}/%{name}-tracer.service

%files examples -f .mfiles-examples

%files shell -f .mfiles-shell

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

%preun monitor
%systemd_preun %{name}-monitor.service

%postun master
%systemd_postun_with_restart %{name}-master.service

%postun tserver
%systemd_postun_with_restart %{name}-tserver.service

%postun gc
%systemd_postun_with_restart %{name}-gc.service

%postun tracer
%systemd_postun_with_restart %{name}-tracer.service

%postun monitor
%systemd_postun_with_restart %{name}-monitor.service

%pre core
getent group %{name} >/dev/null || /usr/sbin/groupadd -r %{name}
getent passwd %{name} >/dev/null || /usr/sbin/useradd --comment "%{longproj}" --shell /sbin/nologin -M -r -g %{name} --home %{_var}/cache/%{name} %{name}

%post master
%systemd_post %{name}-master.service

%post tserver
%systemd_post %{name}-tserver.service

%post gc
%systemd_post %{name}-gc.service

%post tracer
%systemd_post %{name}-tracer.service

%post monitor
%systemd_post %{name}-monitor.service

%changelog
* Wed Mar 15 2017 Mike Miller <mmiller@apache.org> - 1.8.1-1
- Update to 1.8.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-13
- Fix missing protobuf-java and hadoop config classpath bug, and systemd exit
  code problems

* Mon Dec 05 2016 Mike Miller <milleruntime@fedoraproject.org> - 1.6.6-12
- Another fix for Shell erroneously reading accumulo-site.xml

* Fri Dec 02 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-11
- Vastly simplify out-of-box configuration and fix missing avro jar

* Fri Dec 02 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-10
- Add google-gson to classpath for monitor REST service

* Fri Dec 02 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-9
- Include Monitor (bz#1132725)

* Thu Nov 03 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-8
- Re-enable VFS 2.1 HDFS Provider (bz#1387110)

* Wed Nov 02 2016 Mike Miller <mmiller@apache.org> - 1.6.6-7
- Fix for Shell erroneously reading accumulo-site.xml

* Fri Oct 28 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-6
- fix classpath (bz#1389325) and log to console

* Thu Oct 20 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-5
- Use commons-vfs 2.1 patch from upstream for f25+

* Thu Oct 20 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-4
- Fix whitespace in native patch for fuzz=0 opt in f25+

* Thu Oct 20 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-3
- Remove animal sniffer enforcer rule

* Thu Oct 20 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-2
- Remove modernizer plugin

* Wed Oct 19 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 1.6.6-1
- Update to 1.6.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Christopher Tubbs <ctubbsii-fedora@apache.org> - 1.6.4-4
- Use autosetup macro to apply patches

* Thu Nov 05 2015 Christopher Tubbs <ctubbsii-fedora@apache.org> - 1.6.4-3
- Remove unnecessary checkstyle plugin

* Thu Nov 05 2015 Christopher Tubbs <ctubbsii-fedora@apache.org> - 1.6.4-2
- Fix patches for 1.6.4

* Thu Nov 05 2015 Christopher Tubbs <ctubbsii-fedora@apache.org> - 1.6.4-1
- Update to 1.6.4

* Thu Jun 25 2015 Christopher Tubbs <ctubbsii@apache> - 1.6.2-1
- Update to 1.6.2 bugfix release

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 22 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.1-3
- ARMv7 now has hadoop

* Tue Dec 16 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.1-2
- Remove mortbay Jetty deps

* Tue Dec 16 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.1-1
- Update to 1.6.1

* Sun Sep  7 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.6.0-7
- Fix -debuginfo

* Thu Aug 21 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.0-6
- Skip javadoc generation in mvn_build when not used

* Wed Aug 20 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.0-5
- Use jpackage_script macro, standard java env, and working example config

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.0-3
- Fix broken service launch scripts
- Add conditional for lib directory to build for f20

* Wed Jul  9 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.0-2
- Add conditional for pom directory to build for f20
- Remove fno-strict-aliasing flag based on upstream ACCUMULO-2762

* Wed Apr 30 2014 Christopher Tubbs <ctubbsii@apache> - 1.6.0-1
- Initial packaging
