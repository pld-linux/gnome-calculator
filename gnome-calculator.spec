Summary:	GNOME calculator
Summary(pl.UTF-8):	Kalkulator dla GNOME
Name:		gnome-calculator
Version:	40.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-calculator/40/%{name}-%{version}.tar.xz
# Source0-md5:	57e05479d89a68a3649aa4bad69a02da
Patch0:		%{name}-gci.patch
URL:		https://wiki.gnome.org/Apps/Calculator
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gtk+3-devel >= 3.24.1
BuildRequires:	gtksourceview4-devel >= 4.0.2
BuildRequires:	libgee-devel >= 0.20.0
BuildRequires:	libhandy1-devel >= 1.0.0
BuildRequires:	libmpc-devel
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxml2-progs
BuildRequires:	meson >= 0.52.0
BuildRequires:	mpfr-devel
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.50
Requires(post,postun):	gtk-update-icon-cache
Requires:	dconf
Requires:	gtk+3 >= 3.24.1
Requires:	gtksourceview4 >= 4.0.2
Requires:	hicolor-icon-theme
Requires:	libgcalc = %{version}-%{release}
Requires:	libhandy1 >= 1.0.0
Requires:	libsoup >= 2.42.0
Provides:	gcalctool = 6.6.3-1
Obsoletes:	gcalctool < 6.6.3-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-calculator is a simple calculator that performs a variety of
functions.

%description -l pl.UTF-8
gnome-calculator jest prostym kalkulatorem spełniającym wiele funkcji.

%package -n libgcalc
Summary:	GNOME Calculator library
Summary(pl.UTF-8):	Biblioteka kalkulatora GNOME
Group:		Libraries
Requires:	glib2 >= 1:2.50
# gtk+3 for libgci only
Requires:	gtk+3 >= 3.24.1
Requires:	libgee >= 0.20.0

%description -n libgcalc
GNOME Calculator library.

%description -n libgcalc -l pl.UTF-8
Biblioteka kalkulatora GNOME.

%package -n libgcalc-devel
Summary:	Header files for GNOME Calculator library
Summary(pl.UTF-8):	Pliki nagłówkowe kalkulatora GNOME
Group:		Development/Libraries
Requires:	libgcalc = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50
Requires:	gtk+3-devel >= 3.24.1
Requires:	libgee-devel >= 0.20.0

%description -n libgcalc-devel
Header files for GNOME Calculator library.

%description -n libgcalc-devel -l pl.UTF-8
Pliki nagłówkowe kalkulatora GNOME.

%package -n libgcalc-apidocs
Summary:	API documentation for GNOME Calculator library
Summary(pl.UTF-8):	Dokumentacja API biblioteki GNOME Calculator
Group:		Documentation

%description -n libgcalc-apidocs
API documentation for GNOME Calculator library.

%description -n libgcalc-apidocs -l pl.UTF-8
Dokumentacja API biblioteki GNOME Calculator.

%package -n vala-libgcalc
Summary:	Vala API for gcalc library
Summary(pl.UTF-8):	API języka Vala do biblioteki gcalc
Group:		Development/Libraries
Requires:	libgcalc-devel = %{version}-%{release}
Requires:	vala >= 2:0.24.0
Requires:	vala-libgee >= 0.20.0
BuildArch:	noarch

%description -n vala-libgcalc
Vala API for gcalc library.

%description -n vala-libgcalc -l pl.UTF-8
API języka Vala do biblioteki gcalc.

%prep
%setup -q
%patch0 -p1

%build
# --default-library=both causes duplicate ninja rules for gcalc/gcalc.h
%meson build \
	--default-library=shared

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%post	-n libgcalc -p /sbin/ldconfig
%postun	-n libgcalc -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gcalccmd
%attr(755,root,root) %{_bindir}/gnome-calculator
%attr(755,root,root) %{_libexecdir}/gnome-calculator-search-provider
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Calculator-search-provider.ini
%{_datadir}/metainfo/org.gnome.Calculator.appdata.xml
%{_desktopdir}/org.gnome.Calculator.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Calculator.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Calculator.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Calculator-symbolic.svg
%{_mandir}/man1/gcalccmd.1*
%{_mandir}/man1/gnome-calculator.1*

%files -n libgcalc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgcalc-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgcalc-2.so.1
%attr(755,root,root) %{_libdir}/libgci-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgci-1.so.0
%{_libdir}/girepository-1.0/GCalc-2.typelib
%{_libdir}/girepository-1.0/GCi-1.typelib

%files -n libgcalc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgcalc-2.so
%attr(755,root,root) %{_libdir}/libgci-1.so
%{_includedir}/gcalc-2
%{_includedir}/gci-1
%{_datadir}/gir-1.0/GCalc-2.gir
%{_datadir}/gir-1.0/GCi-1.gir
%{_pkgconfigdir}/gcalc-2.pc
%{_pkgconfigdir}/gci-1.pc

%files -n libgcalc-apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/GCalc-2
%{_datadir}/devhelp/books/GCi-1

%files -n vala-libgcalc
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gcalc-2.deps
%{_datadir}/vala/vapi/gcalc-2.vapi
%{_datadir}/vala/vapi/gci-1.deps
%{_datadir}/vala/vapi/gci-1.vapi
