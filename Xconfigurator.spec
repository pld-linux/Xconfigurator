Summary:	Red Hat X Window System Configuration tool
Summary(pl.UTF-8):	Narzędzie do konfiguracji X Window System
Name:		Xconfigurator
Version:	4.10.7
Release:	1
License:	distributable
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	13b8af4364419e959396df2b1f50d87e
#Patch0:		%{name}-config.patch
Patch1:		%{name}-kudzu.patch
#Requires:	initscripts >= 3.60
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	kudzu-devel
Requires:	XFree86 >= 3.3.2
Requires:	kbd
Requires:	kbdconfig
Requires:	mouseconfig >= 2.8
ExcludeArch:	sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
This is the Red Hat X Configuration tool. It is based on the sources
for xf86config, a utility from XFree86. It has a nicer user interface
added to make it easier for the end user.

NOTE - use mouseconfig to change your mouse type, then re-run
Xconfigurator to set X up for your new mouse type.

%description -l pl.UTF-8
Narzędzie do konfiguracji X Window System stworzone przez firmę Red
Hat Software. Jest oparte na xf86config - narzędziu z XFree86. Ma
przyjemniejszy interfejs i jest łatwiejszy w obsłudze.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/Xconfigurator
%attr(755,root,root) %{_bindir}/Xtest
%{_datadir}/Xconfigurator
%{_mandir}/man1/Xconfigurator.1x*
