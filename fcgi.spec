Summary:	FastCGI development kit - shared libraries
Summary(pl):	Zestaw dla programistów FastCGI - biblioteki wspó³dzielone
Name:		fcgi
Version:	2.4.0
Release:	1
License:	distributable
Group:		Libraries
Source0:	http://www.fastcgi.com/dist/%{name}-%{version}.tar.gz
Patch0:		%{name}-no-libs.patch
URL:		http://www.fastcgi.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.4d-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/fastcgi

%description
FastCGI is an open extension to CGI that provides high performance for
all Internet applications without the penalties of Web server APIs.

FastCGI is designed to be layered on top of existing Web server APIs.
For instance, the mod_fastcgi Apache module adds FastCGI support to
the Apache server. FastCGI can also be used, with reduced
functionality and reduced performance, on any Web server that supports
CGI.

This FastCGI Developer's Kit is designed to make developing FastCGI
applications easy. The kit currently supports FastCGI applications
written in C/C++, Perl, Tcl, and Java.

This package contains only shared libraries used by programs developed
using FastCGI Developer's Kit and cgi-fcgi (bridge from CGI to
FastCGI).

%description -l pl
FastCGI to otwarte rozszerzenie CGI daj±ce wysok± wydajno¶æ dla
wszystkich aplikacjach internetowych bez obci±¿ania API serwera WWW.

FastCGI zosta³ zaprojektowany "na wierzchu" instniej±cych API
serwerów. Na przyk³ad, modu³ Apache mod_fastcgi dodaje obs³ugê FastCGI
do serwera Apache. FastCGI mo¿e byæ u¿ywany, ze zmniejszon±
funkcjonalno¶ci± i wydajno¶ci±, z dowolnym serwerem obs³uguj±cym CGI.

Zestaw Programisty FastCGI jest tak zaprojektowany, by uczyniæ ³atwym
tworzenie aplikacji FastCGI. Aktualnie wspiera tworzenie aplikacji
FastCGI w C/C++, Perlu, Tcl i Javie.

Ten pakiet zawiera tylko biblioteki wspó³dzielone u¿ywane przez
programy stworzone przy u¿yciu FastCGI developer's Kit oraz program
cgi-fcgi (bramkê pomiêdzy CGI a FastCGI).

%package devel
Summary:	FastCGI development kit
Summary(pl):	Zestaw dla programistów FastCGI
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	fastcgi-devkit
Provides:	fastcgi-devkit = %{version}

%description devel
This package contains FastCGI Developer's Kit, which is designed to
make developing FastCGI applications easy. The kit currently supports
FastCGI applications written in C/C++, Perl, Tcl, and Java.

%description devel -l pl
Ten pakiet zawiera Zestaw Programisty FastCGI, który jest tak
zaprojektowany, by uczyniæ ³atwym tworzenie aplikacji FastCGI.
Aktualnie wspiera tworzenie aplikacji FastCGI w C/C++, Perlu, Tcl i
Javie.

%package static
Summary:	FastCGI static library
Summary(pl):	Statyczna biblioteka FastCGI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
FastCGI static library.

%description static -l pl
Statyczna biblioteka FastCGI.

%prep
%setup -q
%patch -p1

%build
# supplied libtool is broken (relink, C++)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-global \
	--with-nodebug \
	--with-noassert \
	--with-notest

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/fastcgi

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples/{Makefile*,*.c} $RPM_BUILD_ROOT%{_examplesdir}/fastcgi

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README LICENSE.TERMS doc/*.1
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.htm* doc/*.gif doc/fastcgi-* doc/*.3
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}
%{_examplesdir}/fastcgi

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
