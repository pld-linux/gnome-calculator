Summary:	GNOME calculator
Summary(pl.UTF-8):	Kalkulator dla GNOME
Name:		gnome-calculator
Version:	3.28.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-calculator/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	6571339322e2efd92f8c93b1d0d25885
URL:		https://live.gnome.org/Calculator
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	gtksourceview3-devel >= 3.15.1
BuildRequires:	libmpc-devel
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxml2-progs
BuildRequires:	mpfr-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	dconf
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.20.0
Requires:	gtksourceview3 >= 3.15.1
Requires:	hicolor-icon-theme
Requires:	libsoup >= 2.42.0
Provides:	gcalctool = 6.6.3-1
Obsoletes:	gcalctool < 6.6.3-1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-calculator is a simple calculator that performs a variety of
functions.

%description -l pl.UTF-8
gnome-calculator jest prostym kalkulatorem spełniającym wiele funkcji.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-calculator/libcalculator.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gcalccmd
%attr(755,root,root) %{_bindir}/gnome-calculator
%dir %{_libdir}/gnome-calculator
%attr(755,root,root) %{_libdir}/gnome-calculator/libcalculator.so
%attr(755,root,root) %{_libexecdir}/gnome-calculator-search-provider
%{_desktopdir}/org.gnome.Calculator.desktop
%{_datadir}/metainfo/org.gnome.Calculator.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Calculator-search-provider.ini
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
%{_mandir}/man1/gcalccmd.1*
%{_mandir}/man1/gnome-calculator.1*
