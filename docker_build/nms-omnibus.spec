Name: nms-omnibus
Release: %{build_number}
Summary: NMS Omnibus
Version: %{version}
Group: default 
License: Viasat License
URL: http://www.viasat.com

Requires: audit-libs(x86-64)
Requires: expat(x86-64)
Requires: fontconfig(x86-64)
Requires: freetype(x86-64)
Requires: glibc(x86-64)
Requires: libICE(x86-64)
Requires: libSM(x86-64)
Requires: libX11(x86-64)
Requires: libXau(x86-64)
Requires: libXext(x86-64)
Requires: libXft(x86-64)
Requires: libXmu(x86-64)
Requires: libXrender(x86-64)
Requires: libXt(x86-64)
Requires: libgcc(x86-64)
Requires: libidn(x86-64)
Requires: libjpeg-turbo(x86-64)
Requires: libpng(x86-64)
Requires: libstdc++(x86-64)
Requires: libuuid(x86-64)
Requires: libxcb(x86-64)
Requires: nss-softokn-freebl(x86-64)
Requires: pam(x86-64)
Requires: zlib(x86-64)
Requires: libXcursor(x86-64)
Requires: libXfixes(x86-64)
Requires: libXi(x86-64)
Requires: libXtst(x86-64)
Requires: libgcc(x86-64)
Requires: gtk2(x86-64)
Requires: libcanberra-gtk2(x86-64)

Requires: net-tools
Requires: scl-utils
Requires: unzip
Requires: yum-utils

Requires: compat-libstdc++-33(x86-32)
Requires: glibc(x86-32)
Requires: glibc-devel(x86-32)
Requires: libgcc(x86-32)
Requires: libstdc++(x86-32)
Requires: libpam.so.0
Requires: libX11.so.6

Requires: nms-tivoli-buildtools

AutoReq: no
AutoProv: no

# Disable binary stripping
%global _enable_debug_package 0  %global debug_package %{nil} %global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%description

%pre -p /bin/sh
#!/bin/bash

#GROUP=staff
#USER=pvuser
#INSTALL_DIR=/opt/IBM
#SERVICE=netpvmd

# Add application user if it doesn't exist
#getent group $GROUP >/dev/null || /usr/sbin/groupadd -g 5001 $GROUP
#getent passwd $USER >/dev/null || \
#  /usr/sbin/useradd -g $GROUP -s /bin/bash \
#    -d /home/$USER $USER

# Check if we are a package upgrade
if [ $1 -gt 1 ]
then
  /opt/viasat/deployments/makefile_lib/utils/before-nco-uninstall.sh
fi

%post -p /bin/sh
#!/bin/bash
/opt/viasat/deployments/makefile_lib/utils/after-nco-install.sh

#SERVICE=netpvmd

#ln -s /usr/lib/libcrypto.so.0.9.8e /usr/lib/libcrypto.so

# Start service backup up after install
#if [ $1 -gt 1 ]
#then
    # Start service after install
#    /sbin/service $SERVICE start >/dev/null
#fi

%preun -p /bin/sh
#!/bin/bash

# Only uninstall if we are a clean uninstall (not an upgrade)
if [ $1 -eq 0 ]
then
  /opt/viasat/deployments/makefile_lib/utils/before-nco-uninstall.sh
fi

%postun -p /bin/sh
#!/bin/bash

# If we are an upgrade, then start service
#if [ $1 != 0 ]
#then
#    /sbin/service $SERVICE start >/dev/null
#fi

%install
mkdir -p %{buildroot}/opt/viasat/deployments/makefile_lib
cp -a %{_sourcedir}/deployments/* %{buildroot}/opt/viasat/deployments/makefile_lib
find %{buildroot}/opt/viasat/deployments/makefile_lib -type d -exec chmod a+rx {} \;

%files
%attr(444, root, root) /opt/viasat/deployments/makefile_lib/media/CN4FYEN_SYSLOG.zip
%attr(444, root, root) /opt/viasat/deployments/makefile_lib/media/CN4FZEN_MTTRAPD_v20.zip
%attr(444, root, root) /opt/viasat/deployments/makefile_lib/media/TVL_NTCL_OMN_V8.1.0.19_CORE_LNX_M.zip
%attr(444, root, root) /opt/viasat/deployments/makefile_lib/media/im-nco-g-jdbc-5_0.zip
%attr(444, root, root) /opt/viasat/deployments/makefile_lib/media/im-nco-p-ping-7_0.zip
%attr(555, root, root) /opt/viasat/deployments/makefile_lib/products/omnibus_core_8_1_0_19.mk
%attr(740, root, root) /opt/viasat/deployments/makefile_lib/utils/after-nco-install.sh
%attr(740, root, root) /opt/viasat/deployments/makefile_lib/utils/before-nco-uninstall.sh
%attr(740, root, root) /opt/viasat/deployments/makefile_lib/utils/nco
%attr(740, root, root) /opt/viasat/deployments/makefile_lib/utils/nmsprofile

%doc

%changelog
