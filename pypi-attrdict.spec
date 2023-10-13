#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-attrdict
Version  : 2.0.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/3f/72/614aae677d28e81a5bf830fadcf580803876ef76e0306902d3ca5790cd9a/attrdict-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3f/72/614aae677d28e81a5bf830fadcf580803876ef76e0306902d3ca5790cd9a/attrdict-2.0.1.tar.gz
Summary  : A dict with attribute-style access
Group    : Development/Tools
License  : MIT
Requires: pypi-attrdict-license = %{version}-%{release}
Requires: pypi-attrdict-python = %{version}-%{release}
Requires: pypi-attrdict-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(six)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-Support-Python-3.10.patch

%description
AttrDict
        ========

%package license
Summary: license components for the pypi-attrdict package.
Group: Default

%description license
license components for the pypi-attrdict package.


%package python
Summary: python components for the pypi-attrdict package.
Group: Default
Requires: pypi-attrdict-python3 = %{version}-%{release}

%description python
python components for the pypi-attrdict package.


%package python3
Summary: python3 components for the pypi-attrdict package.
Group: Default
Requires: python3-core
Provides: pypi(attrdict)
Requires: pypi(six)

%description python3
python3 components for the pypi-attrdict package.


%prep
%setup -q -n attrdict-2.0.1
cd %{_builddir}/attrdict-2.0.1
%patch1 -p1
pushd ..
cp -a attrdict-2.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679701864
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-attrdict
cp %{_builddir}/attrdict-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-attrdict/e0026f3103afe13d8c2138480c0cef4b4ca59def || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-attrdict/e0026f3103afe13d8c2138480c0cef4b4ca59def

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
