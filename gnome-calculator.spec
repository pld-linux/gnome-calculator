Summary:	GNOME calculator
Summary(pl.UTF-8):	Kalkulator dla GNOME
Name:		gnome-calculator
Version:	3.12.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-calculator/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	ea00888a85ccc543325ad2ce156bfa7d
URL:		https://live.gnome.org/Calculator
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtksourceview3-devel >= 3.0.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.32.0
Requires:	dconf
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
%{__gnome_doc_common}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gcalccmd
%attr(755,root,root) %{_bindir}/gnome-calculator
%{_desktopdir}/gnome-calculator.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_datadir}/appdata/gnome-calculator.appdata.xml
%{_mandir}/man1/gcalccmd.1*
%{_mandir}/man1/gnome-calculator.1*
