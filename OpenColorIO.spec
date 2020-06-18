#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : OpenColorIO
Version  : 1.1.1
Release  : 19
URL      : https://github.com/imageworks/OpenColorIO/archive/v1.1.1/OpenColorIO-1.1.1.tar.gz
Source0  : https://github.com/imageworks/OpenColorIO/archive/v1.1.1/OpenColorIO-1.1.1.tar.gz
Summary  : A color management framework for visual effects and animation
Group    : Development/Tools
License  : BSD-3-Clause
Requires: OpenColorIO-bin = %{version}-%{release}
Requires: OpenColorIO-data = %{version}-%{release}
Requires: OpenColorIO-lib = %{version}-%{release}
Requires: OpenColorIO-license = %{version}-%{release}
Requires: OpenColorIO-python = %{version}-%{release}
Requires: OpenColorIO-python3 = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : freeglut-dev
BuildRequires : git
BuildRequires : glew-dev
BuildRequires : glu-dev
BuildRequires : lcms2-dev
BuildRequires : markupsafe-python
BuildRequires : mesa-dev
BuildRequires : oiio-dev
BuildRequires : openexr-dev
BuildRequires : openjdk11
BuildRequires : openjdk11-dev
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(yaml-cpp)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : setuptools-python
BuildRequires : texlive
BuildRequires : yaml-cpp-dev
Patch1: OpenColorIO-setuptools.patch
Patch2: ocio-1.1.0-gcc8.patch
Patch3: ocio-1.1.0-yamlcpp060.patch
Patch4: ocio-1.1.0-gl-include.patch

%description
This is a prototype implemetation for a python display integration, which worked
in early Mari versions.  It's provided as a simple example of how to use the
OCIO python API to query the GPU interface functions.

%package bin
Summary: bin components for the OpenColorIO package.
Group: Binaries
Requires: OpenColorIO-data = %{version}-%{release}
Requires: OpenColorIO-license = %{version}-%{release}

%description bin
bin components for the OpenColorIO package.


%package data
Summary: data components for the OpenColorIO package.
Group: Data

%description data
data components for the OpenColorIO package.


%package dev
Summary: dev components for the OpenColorIO package.
Group: Development
Requires: OpenColorIO-lib = %{version}-%{release}
Requires: OpenColorIO-bin = %{version}-%{release}
Requires: OpenColorIO-data = %{version}-%{release}
Provides: OpenColorIO-devel = %{version}-%{release}
Requires: OpenColorIO = %{version}-%{release}

%description dev
dev components for the OpenColorIO package.


%package lib
Summary: lib components for the OpenColorIO package.
Group: Libraries
Requires: OpenColorIO-data = %{version}-%{release}
Requires: OpenColorIO-license = %{version}-%{release}

%description lib
lib components for the OpenColorIO package.


%package license
Summary: license components for the OpenColorIO package.
Group: Default

%description license
license components for the OpenColorIO package.


%package python
Summary: python components for the OpenColorIO package.
Group: Default
Requires: OpenColorIO-python3 = %{version}-%{release}
Provides: opencolorio-python

%description python
python components for the OpenColorIO package.


%package python3
Summary: python3 components for the OpenColorIO package.
Group: Default
Requires: python3-core

%description python3
python3 components for the OpenColorIO package.


%prep
%setup -q -n OpenColorIO-1.1.1
cd %{_builddir}/OpenColorIO-1.1.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592457563
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DOCIO_BUILD_STATIC=OFF \
-DOCIO_BUILD_DOCS=OFF \
-DOCIO_BUILD_TESTS=ON \
-DOCIO_PYGLUE_SONAME=OFF \
-DPYTHON=python$(pkg-config python3 --modversion) \
-DUSE_EXTERNAL_YAML=TRUE \
-DUSE_EXTERNAL_TINYXML=FALSE \
-DUSE_EXTERNAL_LCMS=TRUE \
-DUSE_EXTERNAL_SETUPTOOLS=TRUE \
-DOpenGL_GL_PREFERENCE=GLVND
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build; make test; popd

%install
export SOURCE_DATE_EPOCH=1592457563
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/OpenColorIO
cp %{_builddir}/OpenColorIO-1.1.1/LICENSE %{buildroot}/usr/share/package-licenses/OpenColorIO/aebde2c9b3c7336f785ac928e2ef98959f70ac27
pushd clr-build
%make_install
popd
## install_append content
# Fix location of cmake files.
mkdir -p %{buildroot}%{_datadir}/cmake/Modules
find %{buildroot} -name "*.cmake" -exec mv {} %{buildroot}%{_datadir}/cmake/Modules/ \;
# Relocate site-packages content
ver=$(pkg-config python3 --modversion)
mkdir -p %{buildroot}/usr/lib/python$ver/site-packages
cp -a %{buildroot}/usr/lib64/python$ver/site-packages/* %{buildroot}/usr/lib/python$ver/site-packages/
rm -rf %{buildroot}/usr/lib64/python$ver/site-packages
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ociobakelut
/usr/bin/ociocheck
/usr/bin/ocioconvert
/usr/bin/ociodisplay
/usr/bin/ociolutimage

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*
/usr/share/ocio/setup_ocio.sh

%files dev
%defattr(-,root,root,-)
/usr/include/OpenColorIO/OpenColorABI.h
/usr/include/OpenColorIO/OpenColorIO.h
/usr/include/OpenColorIO/OpenColorTransforms.h
/usr/include/OpenColorIO/OpenColorTypes.h
/usr/include/PyOpenColorIO/PyOpenColorIO.h
/usr/lib64/libOpenColorIO.so
/usr/lib64/pkgconfig/OpenColorIO.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libOpenColorIO.so.1
/usr/lib64/libOpenColorIO.so.1.1.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/OpenColorIO/aebde2c9b3c7336f785ac928e2ef98959f70ac27

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
