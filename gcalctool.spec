Summary:	Gnome calculator
Summary(pl):	Kalkulator dla Gnome
Name:		gcalctool
Version:	4.2.103
Release:	2
License:	GPL
Group:		Applications/Math
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/4.2/%{name}-%{version}.tar.bz2
# Source0-md5:	7776950a7177926a2da32ab05e985b13
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	scrollkeeper
Requires(post):	/usr/bin/scrollkeeper-update
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcalctool is a simple calculator that performs a variety of functions.

%description -l pl
gcalctool jest prostym kalkulatorem spe³niaj±cym wiele funkcji.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS gcalctoolrc NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_mandir}/man1/*
