# TODO:
#	- everything + even more
#
Summary:	A spooler for PostScript printers
Summary(pl.UTF-8):	Spooler dla drukarek postscriptowych
Name:		ppr
Version:	1.53a1
Release:	0.1
License:	BSD
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/ppr/%{name}-%{version}.tar.gz
# Source0-md5:	89c89dbf0fea99407e1b60a3ca3077f2
URL:		http://ppr.trincoll.edu/
BuildRequires:	gdbm-devel
BuildRequires:	perl-base
BuildRequires:	tdb-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PPR is a print spooler for PostScript printers. It can print to
parallel, serial, AppleTalk, LPR/LPD, AppSocket, and SMB printers. It
works well with Ghostscript, Netatalk, CAP60, and Samba.

%description -l pl.UTF-8
PPR to program do kolejkowania wydruków (spooler) dla drukarek
postscriptowych. Może drukować na drukarkach podłączonych przez port
równoległy i szeregowy, po protokołach AppleTalk, LPR/LPD, AppSocket i
SMB. Działa dobrze z Ghostscriptem, Netatalkiem, CAP60 i Sambą.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
./Configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--datadir=%{_datadir} \
	--spooldir=/var/spool/%{name} \
	--with-gdbm \
	--with-tdb \
	--with-gettext \
	--user-ppr=nobody \
	--user-pprwww=http \
	--group-ppr=nobody
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

%{__make} RPM_BUILD_ROOT=$RPM_BUILD_ROOT \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
