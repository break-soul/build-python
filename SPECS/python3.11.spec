%global python3_version 3.11
%global python3_sver 2
%global patch_ver 1

%global debug_package %{nil}
%global __brp_python_bytecompile %{nil}
%undefine __brp_mangle_shebangs

Name:     Python311
Version:  %{python3_version}.%{python3_sver}
Release:  %{patch_ver}%{?dist}
Summary:  self build python%{python3_version}

License:	GPL
Source0:  Python-%{version}.tar.xz

AutoReqProv: no

BuildRequires: autoconf
BuildRequires: bluez-libs-devel
BuildRequires: bzip2
BuildRequires: bzip2-devel
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
 
BuildRequires: findutils
BuildRequires: gcc-c++
BuildRequires: gdbm-devel

BuildRequires: git-core
BuildRequires: glibc-all-langpacks
BuildRequires: glibc-devel
BuildRequires: gmp-devel
BuildRequires: gnupg2
BuildRequires: libappstream-glib
BuildRequires: libb2-devel
BuildRequires: libffi-devel
BuildRequires: libnsl2-devel
BuildRequires: libtirpc-devel
BuildRequires: libGL-devel
BuildRequires: libuuid-devel
BuildRequires: libX11-devel
BuildRequires: make
BuildRequires: mpdecimal-devel
BuildRequires: ncurses-devel
 
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: readline-devel
BuildRequires: redhat-rpm-config >= 127
BuildRequires: sqlite-devel
BuildRequires: gdb
 
BuildRequires: tar
BuildRequires: tcl-devel
BuildRequires: tix-devel
BuildRequires: tk-devel
BuildRequires: tzdata

BuildRequires: xz-devel
BuildRequires: zlib-devel

BuildRequires: systemtap-sdt-devel

BuildRequires: net-tools

BuildRequires: python3-rpm-generators

%description
self build python%{python3_version} rpm

%prep
%setup -q -n Python-%{version}

%build
%configure \
  --prefix=/usr/local/python/%{python3_version} \
  --with-platlibdir=%{_lib} \
  --enable-optimizations \
  --with-lto \
  --without-doc-strings \
  --with-openssl-rpath=auto   \
  
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_bindir}/2to3
rm -f %{buildroot}/%{_bindir}/idle3
rm -f %{buildroot}/%{_bindir}/pydoc3
rm -f %{buildroot}/%{_bindir}/python3
rm -f %{buildroot}/%{_bindir}/python3-config

rm -f %{buildroot}/%{_libdir}/pkgconfig/python3-embed.pc
rm -f %{buildroot}/%{_libdir}/pkgconfig/python3.pc

rm -f %{buildroot}/%{_libdir}/libpython3.so
rm -f %{buildroot}/%{_mandir}/man1/python3.1

%files
%{_bindir}/2to3-%{python3_version}
%{_bindir}/idle%{python3_version}
%{_bindir}/pydoc%{python3_version}
%{_bindir}/python%{python3_version}
%{_bindir}/python%{python3_version}-config

%{_includedir}/python%{python3_version}/

%{_libdir}/pkgconfig/python-%{python3_version}-embed.pc
%{_libdir}/pkgconfig/python-%{python3_version}.pc
%{_libdir}/python%{python3_version}/
%{_libdir}/libpython%{python3_version}.a

%{_prefix}/local/python/%{python3_version}/

%{_mandir}/man1/python%{python3_version}.1.gz
