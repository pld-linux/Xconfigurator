Summary:	Red Hat X Window System Configuration tool
Summary(pl):	Narzêdzie do konfiguracji X Window System
Name:		Xconfigurator
Version:	4.2.3
Release:	1
Copyright:	distributable
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
Patch0:		Xconfigurator-config.patch
Requires:	XFree86 >= 3.3.2,  kbdconfig, mouseconfig >= 2.8, kbd
#Requires:	initscripts >= 3.60
ExcludeArch:	sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
This is the Red Hat X Configuration tool. It is based on the sources
for xf86config, a utility from XFree86. It has a nicer user interface
added to make it easier for the end user.

NOTE - use mouseconfig to change your mouse type, then re-run
Xconfigurator to set X up for your new mouse type.

%description -l pl
Narzêdzie do konfiguracji X Window System stworzone przez firmê Red
Hat Software. Jest oparte na xf86config - narzêdziu z XFree86. Ma
przyjemniejszy interfejs i jest ³atwiejszy w obs³udze.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT

strip Xconfigurator
%{__make} PREFIX=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,TODO}.gz
%attr(755,root,root) %{_bindir}/Xconfigurator
%attr(755,root,root) %{_bindir}/Xtest
%{_datadir}/Xconfigurator
%{_mandir}/man1/Xconfigurator.1x.gz
