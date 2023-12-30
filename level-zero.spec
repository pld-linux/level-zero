Summary:	oneAPI Level Zero components
Summary(pl.UTF-8):	Komponenty oneAPI Level Zero
Name:		level-zero
Version:	1.15.8
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/oneapi-src/level-zero/releases
Source0:	https://github.com/oneapi-src/level-zero/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	609eec9753bbc194fc7a4ac9bac607a1
URL:		https://github.com/oneapi-src/level-zero
BuildRequires:	cmake >= 3.2.0
BuildRequires:	libstdc++-devel >= 6:5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The level-zero package contains the following components of oneAPI:
- Copies of the Level Zero Specification API C/C++ header files
- Level Zero Loader
- Level Zero Validation Layer
- Level Zero Tracing Layer

%description -l pl.UTF-8
Pakiet level-zero zawiera następujące komponenty projektu oneAPI:
- kopie plików nagłówkowych C/C++ specyfikacji API Level Zero
- moduł ładujący Level Zero (Loader)
- warstwę sprawdzania poprawności Level Zero (Validation Layer)
- warstwę śledzenia Level Zero (Tracing Layer)

%package devel
Summary:	Header files for oneAPI Level Zero libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek oneAPI Level Zero
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for oneAPI Level Zero libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek oneAPI Level Zero.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md SECURITY.md
%attr(755,root,root) %{_libdir}/libze_loader.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libze_loader.so.1
%attr(755,root,root) %{_libdir}/libze_tracing_layer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libze_tracing_layer.so.1
%attr(755,root,root) %{_libdir}/libze_validation_layer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libze_validation_layer.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/loader_api.md
%attr(755,root,root) %{_libdir}/libze_loader.so
%attr(755,root,root) %{_libdir}/libze_tracing_layer.so
%attr(755,root,root) %{_libdir}/libze_validation_layer.so
%{_includedir}/level_zero
%{_pkgconfigdir}/level-zero.pc
%{_pkgconfigdir}/libze_loader.pc
