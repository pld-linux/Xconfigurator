Summary:     Red Hat X Window System Configuration tool.
Name:        Xconfigurator
Version:     3.84
Release:     2
Copyright:   distributable
Group:       X11/Utilities
Source:      %{name}-%{version}.tar.gz
Patch:       Xconfigurator-config.patch
Requires:    XFree86 >= 3.3.2,  kbdconfig, mouseconfig >= 2.8, kbd
Requires:    initscripts >= 3.60
ExcludeArch: sparc
BuildRoot:   /tmp/%{name}-%{version}-root

%description
This is the Red Hat X Configuration tool.  It is based on the sources
for xf86config, a utility from XFree86.  It has a nicer user interface
added to make it easier for the end user.

NOTE - use mouseconfig to change your mouse type, then re-run Xconfigurator
to set X up for your new mouse type.

%prep
%setup -q
%patch -p1

%build
make
strip Xconfigurator

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README TODO
%attr(755, root, root) /usr/X11R6/bin/Xconfigurator
/usr/X11R6/share/Xconfigurator
%attr(644, root,  man) /usr/X11R6/man/man1/Xconfigurator.1x
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/Xconfigurator.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/Xconfigurator.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/Xconfigurator.mo
%lang(en) /usr/X11R6/share/locale/en*/LC_MESSAGES/Xconfigurator.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/Xconfigurator.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/Xconfigurator.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/Xconfigurator.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/Xconfigurator.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/Xconfigurator.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/Xconfigurator.mo
%lang(tr) /usr/X11R6/share/locale/tr/LC_MESSAGES/Xconfigurator.mo

%changelog
* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- adjusted FontPath entries

* Thu Nov 12 1998 Matt Wilson <msw@redhat.com>
- Added pci probing for Riva 128 cards, made VideoRam exception 
  (the server can't figure out how much video ram Rive 128 cards have.)

* Thu Oct 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.82-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added full %attr description in %files,
- .mo files moved to /usr/X11R6/share/locale.

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide (slang-1.2.2)

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- translation updates

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com.br>
- updated pt_BR translations
- more i18n strings: ramdac_name, clockchip_name, monitortype_name

* Tue Oct 06 1998 Preston Brown <pbrown@redhat.com>
- updated pci probing to handle S3V GX2 and MX cards

* Mon Sep 28 1998 Preston Brown <pbrown@redhat.com>
- fixed autoprobing for S3V based cards, and for AGP Millennium II

* Fri Sep 25 1998 Preston Brown <pbrown@redhat.com>
- merged back in mouseconfig stuff, somehow lost!??
- merge back erik's changes, also lost!

* Fri Sep 25 1998 Cristian Gafton <gafton@redhat.com>
- turkish update

* Fri Sep 25 1998 Matthew Wilson <msw@redhat.com>
- More backbutton changes, state saving changes.  Much work left to do.

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- NeoMagic video list update

* Thu Sep 24 1998 Preston Brown <pbrown@redhat.com>
- tiny update for new mouseconfig

* Wed Sep 23 1998 Erik Troan <ewt@redhat.com>
- added support for new /etc/sysconfig/keyboard format

* Thu Sep 17 1998 Preston Brown <pbrown@redhat.com>
- fixed problem with path to keyboard map being wrong with new kbd package

* Tue Sep 15 1998 Preston Brown <pbrown@redhat.com>
- added support for new XMOUSETYPE from mouseconfig
- merged changes into cvs (whoops)

* Mon Aug 10 1998 Erik Troan <ewt@redhat.com>
- incorporated Back button mods from Matt Wilson

* Sun Aug 02 1998 Erik Troan <ewt@redhat.com>
- built against newt 0.30

* Wed Jun 10 1998 Erik Troan <ewt@redhat.com>
- was using wrong domain name for translations

* Thu May 14 1998 Cristian Gafton <gafton@redhat.com>
- fixed alpha version

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- use /sbin/setsysfont to restore the system font
- added tr, no, cz, de, no, fr translations (maybe a couple of others)

* Fri Apr 17 1998 Erik Troan <ewt@redhat.com>
- include translations in build

* Sun Apr 05 1998 Erik Troan <ewt@redhat.com>
- updated for new newt, i18n-ready
- removed tons of extraneous code
- doesn't use imake anymore
- buildrooted
- moved monitor database to /usr/X11R6/share
- requires X11R6 > 3.3.2 rather then xserver-wrapper

* Wed Jan 21 1998 Erik Troan <ewt@redhat.com>
- don't install /usr/X11R6/bin/X symlink, just require xserver-wrapper instead

* Sun Nov  9 1997 Michael Fulbright <msf@redhat.com>
- fixed --pick/--continue and --expert interaction

* Sat Nov 08 1997 Erik Troan <ewt@redhat.com>
- added checks for bad parameters

* Fri Nov  7 1997 Michael Fulbright <msf@redhat.com>
- added new video card entries from 2.0.31 kernel pci.c

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- changed /etc/X11/X symlink to be relative, not absolute

* Thu Oct 30 1997 Michael Fulbright <msf@redhat.com>
- fixed VGA16 kickstart support
- fixed version string

* Mon Oct 27 1997 Michael Fulbright <msf@redhat.com>
- Fixed Mach64 autoprobing problems
- Added more user options when selecting from autoprobed video modes

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- fixed handling of temp files to be more safe
- added option for interactive mode to autoprobe ram,color depth, etc.

* Mon Oct  6 1997 Michael Fulbright <msf@redhat.com>
- made 'Unlisted Card' work again
- added more monitors
- added a beta man page

* Thu Oct  2 1997 Michael Fulbright <msf@redhat.com>
- added generic monitor types

* Wed Oct  1 1997 Michael Fulbright <msf@redhat.com>
- made it run /etc/X11/X explicitely
- added --expert flag
- fixed memory allocation problem in SplitString()

* Tue Sep 30 1997 Michael Fulbright <msf@redhat.com>
- added kickstart support
- added PCI probing for PCI video card autodetection
- added use of --probeonly to get video card information
