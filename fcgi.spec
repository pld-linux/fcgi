Summary:	FastCGI development kit - shared libraries
Summary(pl.UTF-8):	Zestaw dla programistów FastCGI - biblioteki współdzielone
Name:		fcgi
Version:	2.4.0
Release:	3
License:	distributable
Group:		Libraries
Source0:	http://www.fastcgi.com/dist/%{name}-%{version}.tar.gz
# Source0-md5:	d15060a813b91383a9f3c66faf84867e
Patch0:		%{name}-no-libs.patch
Patch1:		%{name}-listen-backlog.patch
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

%description -l pl.UTF-8
FastCGI to otwarte rozszerzenie CGI dające wysoką wydajność dla
wszystkich aplikacjach internetowych bez obciążania API serwera WWW.

FastCGI został zaprojektowany "na wierzchu" istniejących API serwerów.
Na przykład, moduł Apache mod_fastcgi dodaje obsługę FastCGI do serwera
Apache. FastCGI może być używany, ze zmniejszoną funkcjonalnością
i wydajnością, z dowolnym serwerem obsługującym CGI.

Zestaw Programisty FastCGI jest tak zaprojektowany, by uczynić łatwym
tworzenie aplikacji FastCGI. Aktualnie wspiera tworzenie aplikacji
FastCGI w C/C++, Perlu, Tcl i Javie.

Ten pakiet zawiera tylko biblioteki współdzielone używane przez programy
stworzone przy użyciu FastCGI developer's Kit oraz program cgi-fcgi
(bramkę pomiędzy CGI a FastCGI).

%package devel
Summary:	FastCGI development kit
Summary(pl.UTF-8):	Zestaw dla programistów FastCGI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	fastcgi-devkit

%description devel
This package contains FastCGI Developer's Kit, which is designed to
make developing FastCGI applications easy. The kit currently supports
FastCGI applications written in C/C++, Perl, Tcl, and Java.

%description devel -l pl.UTF-8
Ten pakiet zawiera Zestaw Programisty FastCGI, który jest tak
zaprojektowany, by uczynić łatwym tworzenie aplikacji FastCGI.
Aktualnie wspiera tworzenie aplikacji FastCGI w C/C++, Perlu, Tcl i
Javie.

%package static
Summary:	FastCGI static library
Summary(pl.UTF-8):	Statyczna biblioteka FastCGI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FastCGI static library.

%description static -l pl.UTF-8
Statyczna biblioteka FastCGI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# supplied libtool is broken (relink, C++)
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

CPPFLAGS="-DLISTEN_BACKLOG=1024"
%configure \
	--with-global \
	--with-nodebug \
	--with-noassert \
	--with-notest

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples/{Makefile*,*.c} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
