%define gettext_package gnome-panel-2.0
%define _default_patch_fuzz 999

%define gnome_desktop_version 2.11.1
%define glib2_version 2.15.5
%define gtk2_version 2.11.3
%define libgnome_version 2.13.0
%define libgnomeui_version 2.5.4
%define libbonoboui_version 2.3.0
%define orbit_version 2.4.0
%define libwnck_version 2.19.5
%define gconf_version 2.14
%define gnome_menus_version 2.27.92
%define evolution_data_server_version 1.9.1
%define cairo_version 1.0.0
%define dbus_version 0.60
%define dbus_glib_version 0.60
%define gnome_doc_utils_version 0.3.2
%define libgweather_version 2.27.90

%define use_evolution_data_server 1

Summary: GNOME panel
Name: gnome-panel
Version: 2.30.2
Release: 5%{?dist}
URL: http://www.gnome.org
Source0: http://download.gnome.org/sources/gnome-panel/2.28/%{name}-%{version}.tar.bz2

Source3: redhat-panel-default-setup.entries
Source4: gnome-compiler-flags.m4
Source5: redhat-panel-backwards-compat-config.schemas
Source6: add-translations.sh
License: GPLv2+ and LGPLv2+ and GFDL
Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: gnome-desktop >= %{gnome_desktop_version}
Requires: libwnck >= %{libwnck_version}
Requires: gnome-menus >= %{gnome_menus_version}
%if %{use_evolution_data_server}
Requires: evolution-data-server >= %{evolution_data_server_version}
%endif
Requires: gnome-session-xsession
Requires: %{name}-libs = %{version}-%{release}

Requires(post): GConf2 >= %{gconf_version}
Requires(post): scrollkeeper
Requires(post): hicolor-icon-theme
Requires(pre): GConf2 >= %{gconf_version}
Requires(preun): GConf2 >= %{gconf_version}
Requires(postun): scrollkeeper

BuildRequires: libxml2-python
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: scrollkeeper
BuildRequires: libxslt
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libcanberra-devel
BuildRequires: gnome-desktop-devel >= %{gnome_desktop_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libgnome-devel >= %{libgnome_version}
BuildRequires: libgnomeui-devel >= %{libgnomeui_version}
BuildRequires: libbonoboui-devel >= %{libbonoboui_version}
BuildRequires: libwnck-devel >= %{libwnck_version}
BuildRequires: GConf2-devel >= %{gconf_version}
BuildRequires: gnome-menus-devel >= %{gnome_menus_version}
BuildRequires: cairo-devel >= %{cairo_version}
BuildRequires: gnome-doc-utils >= %{gnome_doc_utils_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: gtk-doc
BuildRequires: pango-devel
BuildRequires: libbonobo-devel
BuildRequires: libXau-devel
%if %{use_evolution_data_server}
BuildRequires: evolution-data-server-devel >= %{evolution_data_server_version}
BuildRequires: ORBit2-devel >= %{orbit_version}
BuildRequires: dbus-devel >= %{dbus_version}
%endif
BuildRequires: polkit-devel >= 0.92
BuildRequires: libgweather-devel >= %{libgweather_version}
BuildRequires: librsvg2-devel
BuildRequires: NetworkManager-devel
BuildRequires: intltool
BuildRequires: gettext-devel
BuildRequires: libtool

Patch0: gnome-panel-vendor.patch
Patch1: gnome-panel-2.10.1-speak-to-us-ye-old-wise-fish.patch
Patch2: old-gtk.patch
Patch3: gnome-panel-about.patch

# the next three patches belong together
# http://bugzilla.gnome.org/show_bug.cgi?id=470966
Patch8: launcher-desktop-files.patch
Patch9: desktop-file-monitoring.patch
Patch10: preferred-apps.patch

# don't pop up an error dialog if an applet from the
# default configuration is missing; we don't want to
# add a hard dependency on e.g. tomboy
Patch11: applet-error.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=587762
Patch12: fix-workspace-properties-crash.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=520111
Patch24: gnome-panel-2.21.92-allow-spurious-view-done-signals.patch

Patch40: clock-home.patch
Patch41: bookmarks-submenu.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=537798
Patch47: fix-clock-crash.patch

Patch48: strict-clock.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=357934
Patch50: link-places.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=614032
Patch51: gnome-panel-dir-prefix.patch

# make docs show up in rarian/yelp
Patch52: gnome-panel-doc-category.patch

# updated translations
# https://bugzilla.redhat.com/show_bug.cgi?id=563030
Patch53: gnome-panel-translations.patch

Patch54: allow-super-mouse-modifier.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=343436
Patch143: panel-padding.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=583273
Patch145: icon-padding.patch


Conflicts: gnome-power-manager < 2.15.3

%description
The GNOME panel provides the window list, workspace switcher, menus, and other
features for the GNOME desktop.

%package libs
Summary: Libraries for Panel Applets
License: LGPLv2+
Group: Development/Libraries

%description libs
This package contains the libpanel-applet library that
is needed by Panel Applets.

%package devel
Summary: Headers and libraries for Panel Applet development
License: LGPLv2+
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release}
Requires: gtk2-devel >= %{gtk2_version}
Requires: libbonoboui-devel >= %{libbonoboui_version}
Requires: libgnomeui-devel >= %{libgnomeui_version}
Requires: pkgconfig
# for /usr/share/gtk-doc/html
Requires: gtk-doc

%description devel
Panel Applet development package. Contains files needed for developing
Panel Applets using the libpanel-applet library.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .vendor
%patch1 -p1 -b .speak-to-us-ye-old-wise-fish
%patch2 -p1 -b .old-gtk
%patch3 -p1 -b .about
%patch8 -p1 -b .launcher-desktop-files
%patch9 -p1 -b .desktop-file-monitoring
%patch10 -p1 -b .preferred-apps
%patch11 -p1 -b .applet-error
%patch12 -p1 -b .fix-workspace-properties-crash
%patch24 -p1 -b .allow-spurious-view-done-signals
%patch40 -p1 -b .clock-home
%patch41 -p1 -b .bookmarks-submenu
%patch47 -p1 -b .fix-clock-crash
%patch48 -p1 -b .strict-clock
%patch50 -p1 -b .link-places
%patch51 -p1 -b .dir-prefix
%patch52 -p1 -b .doc-category
%patch54 -p1 -b .allow-super-mouse-modifier
%patch143 -p1 -b .panel-padding
%patch145 -p1 -b .icon-padding

. %{SOURCE6}

cp -f %{SOURCE3} gnome-panel/panel-default-setup.entries
cp -f %{SOURCE4} m4
cp -f %{SOURCE5} gnome-panel/panel-compatibility.schemas

libtoolize -f
aclocal -I m4
automake
autoconf

%patch53 -p1 -b .translations

%build
%configure \
   --disable-shave \
   --disable-gtk-doc \
   --disable-scrollkeeper \
%if %{use_evolution_data_server}
   --enable-eds=yes
%else
   --enable-eds=no
%endif

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


# truncate NEWS
awk '/^========/ { seen+=1 }
{ if (seen < 3) print }
{ if (seen == 3) { print "For older news, see http://git.gnome.org/cgit/gnome-panel/plain/NEWS"; exit } }' NEWS > tmp; mv tmp NEWS


%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

#
# Create pager and tasklist schemas for compatibility with older
# configurations which reference the old schema names
#
sed -e 's|/schemas/apps/window_list_applet/prefs/|/schemas/apps/tasklist_applet/prefs/|' $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/window-list.schemas > $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/tasklist.schemas
sed -e 's|/schemas/apps/workspace_switcher_applet/prefs/|/schemas/apps/pager_applet/prefs/|; s|<default>1</default>|<default>2</default>|' $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/workspace-switcher.schemas > $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/pager.schemas

## blow away stuff we don't want
/bin/rm -rf $RPM_BUILD_ROOT/var/scrollkeeper
/bin/rm -f $RPM_BUILD_ROOT%{_libdir}/libpanel-applet-2.*a

desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/gnome-panel.desktop

%find_lang %{gettext_package} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`

#
# Clear out the old defaults
#
gconftool-2 --direct --config-source=$GCONF_CONFIG_SOURCE --recursive-unset /apps/panel > /dev/null || :
gconftool-2 --direct --config-source=$GCONF_CONFIG_SOURCE --recursive-unset /schemas/apps/panel > /dev/null || :

#
# Install the schemas
#
gconftool-2 --makefile-install-rule \
        %{_sysconfdir}/gconf/schemas/clock.schemas \
        %{_sysconfdir}/gconf/schemas/fish.schemas \
        %{_sysconfdir}/gconf/schemas/pager.schemas \
        %{_sysconfdir}/gconf/schemas/panel-compatibility.schemas \
        %{_sysconfdir}/gconf/schemas/panel-general.schemas \
        %{_sysconfdir}/gconf/schemas/panel-global.schemas \
        %{_sysconfdir}/gconf/schemas/panel-object.schemas \
        %{_sysconfdir}/gconf/schemas/panel-toplevel.schemas \
        %{_sysconfdir}/gconf/schemas/tasklist.schemas \
        %{_sysconfdir}/gconf/schemas/window-list.schemas \
        %{_sysconfdir}/gconf/schemas/workspace-switcher.schemas \
        %{_sysconfdir}/gconf/schemas/notification_area_applet.schemas \
  > /dev/null || :

#
# Install the default setup into /apps/panel and /apps/panel/default_setup
#
gconftool-2 --direct --config-source=$GCONF_CONFIG_SOURCE --load %{_sysconfdir}/gconf/schemas/panel-default-setup.entries > /dev/null || :
gconftool-2 --direct --config-source=$GCONF_CONFIG_SOURCE --load %{_sysconfdir}/gconf/schemas/panel-default-setup.entries /apps/panel > /dev/null || :

/sbin/ldconfig

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
        %{_sysconfdir}/gconf/schemas/clock.schemas \
        %{_sysconfdir}/gconf/schemas/fish.schemas \
        %{_sysconfdir}/gconf/schemas/pager.schemas \
        %{_sysconfdir}/gconf/schemas/panel-compatibility.schemas \
        %{_sysconfdir}/gconf/schemas/panel-general.schemas \
        %{_sysconfdir}/gconf/schemas/panel-global.schemas \
        %{_sysconfdir}/gconf/schemas/panel-object.schemas \
        %{_sysconfdir}/gconf/schemas/panel-toplevel.schemas \
        %{_sysconfdir}/gconf/schemas/tasklist.schemas \
        %{_sysconfdir}/gconf/schemas/window-list.schemas \
        %{_sysconfdir}/gconf/schemas/workspace-switcher.schemas \
  > /dev/null || :
  if [ -f %{_sysconfdir}/gconf/schemas/notification_area_applet.schemas ]; then
    gconftool-2 --makefile-uninstall-rule \
        %{_sysconfdir}/gconf/schemas/notification_area_applet.schemas > /dev/null || :
  fi
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
        %{_sysconfdir}/gconf/schemas/clock.schemas \
        %{_sysconfdir}/gconf/schemas/fish.schemas \
        %{_sysconfdir}/gconf/schemas/pager.schemas \
        %{_sysconfdir}/gconf/schemas/panel-compatibility.schemas \
        %{_sysconfdir}/gconf/schemas/panel-general.schemas \
        %{_sysconfdir}/gconf/schemas/panel-global.schemas \
        %{_sysconfdir}/gconf/schemas/panel-object.schemas \
        %{_sysconfdir}/gconf/schemas/panel-toplevel.schemas \
        %{_sysconfdir}/gconf/schemas/tasklist.schemas \
        %{_sysconfdir}/gconf/schemas/window-list.schemas \
        %{_sysconfdir}/gconf/schemas/workspace-switcher.schemas \
  > /dev/null || :
  if [ -f %{_sysconfdir}/gconf/schemas/notification_area_applet.schemas ]; then
    gconftool-2 --makefile-uninstall-rule \
        %{_sysconfdir}/gconf/schemas/notification_area_applet.schemas > /dev/null || :
  fi
fi

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{gettext_package}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LIB COPYING-DOCS NEWS README
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/gnome-panel
%exclude %{_datadir}/gnome-panelrc
%{_datadir}/idl/gnome-panel-2.0
%{_datadir}/gnome-2.0/ui/*.xml
%dir %{_datadir}/omf/clock
%dir %{_datadir}/omf/fish
%{_datadir}/man/man*/*
%{_datadir}/applications/gnome-panel.desktop
%{_bindir}/gnome-panel
%{_bindir}/gnome-desktop-item-edit
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*.server
%{_sysconfdir}/gconf/schemas/*.schemas
%{_sysconfdir}/gconf/schemas/*.entries

%{_sysconfdir}/dbus-1/system.d/org.gnome.ClockApplet.Mechanism.conf
%{_datadir}/dbus-1/system-services/org.gnome.ClockApplet.Mechanism.service
%{_datadir}/polkit-1/actions/org.gnome.clockapplet.mechanism.policy

%files libs
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/panel-test-applets
%{_libdir}/pkgconfig/*
%{_includedir}/panel-2.0
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/*

%changelog
* Tue Aug 17 2010 Ray Strode <rstrode@redhat.com> 2.30.2-5
- More panel drag fixes
  Related: #614997

* Mon Aug 09 2010 Ray Strode <rstrode@redhat.com> 2.30.2-4
- Update translations
  Resolves: #563030

* Thu Jul 15 2010 Ray Strode <rstrode@redhat.com> 2.30.2-3
- Allow "Super" key to be mouse modifier
  Resolves: #614997

* Wed Jun 30 2010 Ray Strode <rstrode@redhat.com> 2.30.2-2
- Fix crash when going to workspace switcher
  Resolves: #587762

* Tue Jun 22 2010 Ray Strode <rstrode@redhat.com> 2.30.2-1
- Update to 2.30.2-1.el6 for maintainability
  Resolves: #595418

* Mon Jun 14 2010 Ray Strode <rstrode@redhat.com> 2.28.0-24
- Don't crash notification area on multi-screen setups
  Resolves: #601241

* Fri Jun 11 2010 Ray Strode <rstrode@redhat.com> 2.28.0-23
- Properly hide uninstalled preferred apps from panel
  Resolves: #584542

* Tue May 11 2010 Matthias Clasen <mclasen@redhat.com> 2.28.0-22
- Updated translations
Resolves: #563030

* Mon May  3 2010 Matthias Clasen <mclasen@redhat.com> 2.28.0-21
- Make clock docs show up in yelp
Resolves: #588547

* Fri Mar 26 2010 Ray Strode <rstrode@redhat.com> 2.28.0-20
- Support relocatable .gnome2 directory
  Resolves: #577301

* Mon Feb 15 2010 Matthias Clasen <mclasen@redhat.com> 2.28.0-19
- Use 12/24 hour formats consistenly in the clock applet
- Don't default to copying folder when using DND from the places menu

* Fri Jan 29 2010 Ray Strode <rstrode@redhat.com> 2.28.0-18
- Spec file clean ups (bug 559979)

* Fri Jan 15 2010 Matthias Clasen <mclasen@redhat.com> 2.28.0-17
- Tighten the clock applets policy

* Tue Dec 08 2009 Ray Strode <rstrode@redhat.com> 2.28.0-16
- Fix clock crash (bug 537798)

* Mon Nov  9 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-15
- Improve the behaviour of the panel when screen resolution
  changes (gnome #341441)

* Fri Nov  6 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-14
- Revert the last change, it didn't have the desired effect

* Mon Nov  2 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-13
- Don't add padding before the first and after the last applet (#532410)

* Thu Oct 29 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-12
- Make padding work correctly in non-expanded panels (#529614)

* Tue Oct 20 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-11
- Remove a leftover debugging statement

* Tue Oct 20 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-10
- Reduce the inter-applet padding

* Mon Oct 19 2009 Ray Strode <rstrode@redhat.com> 2.28.0-9
- Add explicit libs requires (bug 525600)

* Mon Oct 19 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-9
- Actually set non-zero padding

* Sat Oct 17 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-8
- Add padding around status icons

* Fri Oct 16 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-6
- Put status icons in a predictable order

* Wed Oct 14 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-5
- Tweaks to the default panel configuration

* Thu Oct  8 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-4
- Fix possible crashes related to randr events

* Thu Oct  8 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-3
- Accept more bookmarks in the places menu before overflowing

* Wed Oct  7 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-2
- Add a default location to the clock applet

* Wed Sep 23 2009 Matthias Clasen <mclasen@redhat.com> 2.28.0-1
- Update to 2.28.0

* Wed Sep  9 2009 Matthias Clasen <mclasen@redhat.com> 2.27.92-1
- Update to 2.27.92

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhat.com> 2.27.91-1
- Update to 2.27.91

* Sat Aug 22 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-9
- Actually apply the 'clear recent' patch

* Thu Aug 13 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-8
- Stricter clock-applet PolicyKit policy

* Wed Aug  5 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-7
- Make 'Clear Recent Documents' follow the menu-images setting

* Sun Aug  2 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-6
- Save some space

* Fri Jul 31 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-5
- Reduce the excessive 'about'-ing in the System menu

* Mon Jul 27 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-4
- Drop unneeded direct deps

* Fri Jul 24 2009 Ray Strode <rstrode@redhat.com> 2.27.4-3
- Make my panels show up again on login (gnome bug 589632)

* Wed Jul 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.4-2
- Make category icons follow the menu-images setting

* Wed Jul 15 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.4-1
- Update to 2.27.4

* Tue Jun  9 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.2-3
- Port to PolicyKit 1

* Tue Jun  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.2-2
- Replace tomboy by gnote in the default panel configuration

* Wed May 20 2009 Ray Strode <rstrode@redhat.com> 2.26.2-1
- Update to 2.26.2

* Mon Apr 27 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-3
- Don't drop schemas translations from po files

* Wed Apr 15 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-2
- Fix the clock applets network tracking code

* Tue Apr 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1

* Mon Apr 13 2009 David Zeuthen <davidz@redhat.com> - 2.26.0-2
- Handle emblemed icons (GNOME #578859)

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Mar  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Fri Feb 27 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-3
- Require PolicyKit-authentication-agent

* Mon Feb 23 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-2
- Fix panel behaviour on screen size changes

* Thu Feb 19 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.90-1
- Update to 2.25.90

* Fri Jan 23 2009 Ray Strode <rstrode@redhat.com> - 2.25.5.1-1
- Update to 2.25.5.1
- Fixes bug 481029

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.5-1
- Update to 2.25.5

* Fri Jan 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.3-4
- And don't write %%s into desktop files

* Fri Jan 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.3-3
- Fix the 'smart launcher' patch

* Thu Dec 18 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-3
- Remove the mixer from the default panel config as well
- Update search and preferred apps patches

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.3-2
- Update to 2.25.3
- Drop mixer from default config

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-6
- Rebuild

* Sun Nov  9 2008 Ray Strode <rstrode@redhat.com> - 2.24.1-4
- Don't unhide drawers by default.  Patch from
  Leszek Matok <lam@lac.pl> (bug 470719)

* Mon Nov  3 2008 Ray Strode <rstrode@redhat.com> - 2.24.1-3
- Fix up panel slide in patch to work better with empty panels

* Mon Nov  3 2008 Ray Strode <rstrode@redhat.com> - 2.24.1-2
- Fix up panel slide in patch to
  1) not have odd effects with vertical panels
  2) set up struts earlier

* Wed Oct 22 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Wed Oct 22 2008 Ray Strode  <rstrode@redhat.com> - 2.24.0-8
- Don't make nautilus slide down as the panel slides down,
  instead push nautilus out of the way immediately, and slide
  in the available space.

* Sun Oct 12 2008 Ray Strode  <rstrode@redhat.com> - 2.24.0-7
- Update smooth slide patch to be simpler based on feedback
  on gnome bug (554343)

* Thu Oct  9 2008 Ray Strode  <rstrode@redhat.com> - 2.24.0-6
- Hide shutdown item if unavailable

* Thu Oct  9 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.0-5
- Don't show menuitems which fail the tryexec test

* Fri Sep 26 2008 Ray Strode  <rstrode@redhat.com> - 2.24.0-4
- Try to make initial panel slide-in animation be smooth

* Thu Sep 25 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.0-3
- Save some space

* Thu Sep 25 2008 Ray Strode  <rstrode@redhat.com> - 2.24.0-2
- Requires: gnome-session-xsession so it gets pulled in for
  typical GNOME installs.

* Tue Sep 23 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Sat Aug 23 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.90.1-1
- Update to 2.23.90.1

* Tue Aug  5 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.6-1
- Update to 2.23.6

* Wed Jul 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.23.5-2
- fix license tag

* Tue Jul 22 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.5-1
- Update to 2.23.5

* Fri Jul 18 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.4-5
- Fix one more icon

* Wed Jul  9 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.4-4
- Move panel-test-applets to the -devel package

* Wed Jul  9 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.4-3
- Use more standard icon names

* Tue Jul  8 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.4-2
- Fix debuginfo generation

* Wed Jun 18 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.4-1
- Update to 2.23.4

* Tue Jun 10 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.3-2
- Avoid unnecessary wakeups in the clock for monitoring 
  Gentoo config file locations

* Wed Jun  4 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.3-1
- 2.23.3

* Wed May 14 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.2.1-1
- Update to 2.23.2.1

* Wed May 14 2008 Adam Tkac <atkac redhat com> - 2.23.1-2
- rebuild

* Fri Apr 25 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Wed Apr 23 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.1.2-6
- Remove an erroneous addition in the last patch

* Tue Apr 22 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.1.2-5
- Add another patch that may fix timezone setting problems (#443415)

* Fri Apr 18 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.1.2-4
- Use gio to open places 
- Fix a 64bit issue with timezone handling in the clock

* Fri Apr 18 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.1.2-3
- Move the trash applet back where it belongs, to the corner (#439416)

* Wed Apr 16 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.1.2-2
- Make help buttons work in clock preferences

* Thu Apr 10 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.1.2-1
- Update to 2.22.1.2 (significant performance and usability 
  improvements for the clock applet)

* Tue Apr 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.1.1-1
- Update to 2.22.1.1

* Mon Apr  7 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Sun Apr  6 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-12
- Fix a typo in the CK shutdown patch, spotted by Kevin Kofler

* Sat Apr  5 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-11
- Handle PolicyKit errors returned from ConsoleKit

* Fri Apr  4 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-10
- Ignore dbus errors when setting the time

* Wed Apr  2 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-9
- Fix a possible crash in the clock applet

* Fri Mar 28 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-8
- Fix editing of locations in the clock applet

* Fri Mar 28 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-7
- Convert the edit and find location windows to dialogs

* Thu Mar 27 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-6
- Improve the time settings window

* Thu Mar 27 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-5
- Make the find-location window of the clock larger

* Sat Mar 15 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-4
- Only save the session when the users wants it

* Fri Mar 14 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-3
- Populate the location list before showing the preference window

* Mon Mar 10 2008 Matthias Clasen  <mclasen@redhat.com> - 2.22.0-2
- Bump revision

* Mon Mar 10 2008 Jon McCann <jmccann@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Sat Mar  8 2008 Will Woods <wwoods@redhat.com> - 2.21.92-6
- Add "About This Computer" item to System menu if it exists

* Mon Mar  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-5
- Fix a redraw problem with the clock map

* Mon Mar  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-4
- Make the clock applet handle multiple locations in the 
  same timezone meaningfully

* Mon Mar  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-3
- Some upstream clock applet fixes

* Mon Mar  3 2008 Ray Strode <rstrode@redhat.com> - 2.21.92-2
- Don't crash with Zimbra connector (bug 435355)

* Tue Feb 26 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Fri Feb 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-9
- Report sunrise/sunset times in local time

* Thu Feb 21 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-8
- Make drawers open again

* Wed Feb 20 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-7
- Make the last patch work 

* Wed Feb 20 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-6
- Try harder to avoid resizing the popup 

* Tue Feb 19 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-5
- Take daylight savings time into account when calculating offsets

* Mon Feb 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-4
- Another round of intlclock fixes

* Sun Feb 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-3
- First round of intlclock fixes

* Fri Feb 15 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-2
- Drop gnome-vfs BR

* Wed Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-1
- Update to 2.21.91
- Update patches

* Sun Feb  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.90-3
- Ensure the logout dialog gets focus. 

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.90-1
- Update to 2.21.90
- Drop upstreamed patch

* Fri Jan 25 2008 Jon McCann <jmccann@redhat.com> - 2.21.5-2
- Add ConsoleKit restart/shutdown support

* Wed Jan 16 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.5-1
- Update to 2.21.5
- Drop separate intlclock

* Thu Dec 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.2-2
- Adapt to libgweather api changes

* Tue Nov 27 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.2-1
- Update to 2.20.2 (translation updates)

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-7
- Fix a problem with the intlclock GConf schema

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-6
- Reenable intlclock

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-5
- Split off a libs subpackage to break a cyclic dependency
- Build without intlclock for bootstrapping purposes

* Mon Oct 29 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-4
- Intlclock: make default units work correctly

* Sun Oct 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-3
- Intlclock: add weather preferences, show temperature in panel

* Sat Oct 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-2
- Fix some issues with the offset display in the intlclock

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-1
- Update to 2.20.1

* Sun Oct 14 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-9
- Install the right intlclock icons, and the right gconf schema

* Sun Oct 14 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-8
- Add network monitoring to the intlclock

* Sat Oct 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-7
- Another round of intlclock updates
  * show offsets in popup
  * vary clock faces throughout the day

* Fri Oct 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-6
- Sharper icons

* Tue Oct  9 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-5
- Some intlclock updates

* Fri Oct  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-4
- Replace clock by intlclock

* Wed Oct  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-3
- Make it possible to start s-c-d from the clock menu again (#316921)

* Fri Sep 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-2
- Don't pop up an error if an applet from the default
  configuration is missing  

* Tue Sep 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-1
- Update to 2.20.0.1

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-7
- Can't require tomboy where there's no mono

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-6
- Turns out we need requires for applets in the default config (#293261)

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-5
- Drop the requires for fast-user-switch-applet (#253831)

* Thu Sep 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-4
- Fix some memleaks
- Remove OpenOffice launchers from the default configuration
- Add Tomboy to the default configuration

* Mon Sep 10 2007 Ray Strode <rstrode@redhat.com> - 2.19.92-3
- create ~/.local/share/applications before writing out 
  preferred app launchers

* Thu Sep  6 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-2
- Improve the handling of preferred apps in launchers

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-1
- Update to 2.19.92

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 2.19.6-2
- Rebuild for build ID

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-1
- Update to 2.19.6

* Mon Aug  6 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-7
- Update license field again
- Use %%find_lang for help files, too

* Sat Aug  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-6
- Update license field

* Wed Jul 25 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-5
- Make the panel talk to gnome-power-manager again.
- Drop the patch to add suspend to the menu, it was
  rejected by upstream

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 2.19.5-4
- Rebuild for RH #249435

* Tue Jul 24 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-3
- Fix launcher tooltips to react to changes.  (#212164)

* Thu Jul 12 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-2
- Fix a crash in the new timezone code in the clock applet

* Sun Jul  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-1
- Update to 2.19.5

* Sat Jul  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-2
- Fix directory ownership issues

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-1
- Update to 2.19.4

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-3
- Rebuild again

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-2
- Rebuild against new libwnck

* Mon Jun 04 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-1
- Update to 2.19.3

* Tue May 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-2
- Don't ship a pointless empty file in /usr/share

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2

* Fri Apr 13 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-9
- Apply upstream patch from Ross Burton (upstream bug 416120)
  to show completed tasks in the clock applet as completed.

* Wed Apr  4 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-8
- fix invalid read and potentially fix 234544

* Wed Apr  4 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-7
- Allow users to correct desktop launchers when given an 
  error initially (bug 233015)

* Tue Apr  3 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-6
- update the clock after timezone changes (bug 230832)

* Sat Mar 31 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-5
- Remove the bug-buddy patch again; fixed better in libgnome

* Fri Mar 30 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-4
- Fix bug-buddy support in the other applets

* Fri Mar 30 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-3
- Fix bug-buddy support in the clock applet

* Fri Mar 30 2007 Ray Strode <rstrode@redhat.com> - 2.18.0-2
- hide "Lock Screen" menu item when logged in as root

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Tue Mar  6 2007 Alexander Larsson <alexl@redhat.com> - 2.17.92-1
- Add xdg-user-dirs patch

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> 2.17.92-1
- Update to 2.17.92

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> 2.17.91-6
- Put the fast user switch applet in the default panel configuration

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> 2.17.91-5
- Update to 2.17.91

* Sat Feb 10 2007 Matthias Clasen <mclasen@redhat.com> 2.17.91-4.svn20070207
- Run autoheader since HAVE_LANGINFO_H is missing in config.h.in

* Fri Feb  9 2007 Kristian Høgsberg <krh@redhat.com> 2.17.91-3.svn20070207
- Update compiz support patch (#227986).

* Thu Feb  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-2.svn20070207
- Hide the "Switch User" button on the logout dialog again

* Mon Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90
- Clean up BuildRequires
- Allow user switching from the logout dialog

* Sun Jan 14 2007 Matthias Clasen <mclasen@redhat.com> - 2.16.2-2
- Check for the right tracker desktop file

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.2-1
- Update to 2.16.2
- Drop upstreamed patches

* Wed Nov 29 2006 Ray Strode <rstrode@redhat.com> - 2.16.1-8
- don't ask user if they want to logout if they've set the
  preference not to 

* Wed Nov 29 2006 Stepan Kasal <skasal@redhat.com> - 2.16.1-7
- Add BuildRequires: libtool; without it, the aclocal call failed.

* Tue Nov 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-6
- Support tracker 

* Thu Nov 16 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-5
- Fix previous patch and also include the fix
  for gnome bug 359707

* Tue Nov 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-4
- Fix copying of launchers by DND, bug 214334

* Tue Nov 14 2006 Ray Strode <rstrode@redhat.com> - 2.16.1-3
- fix "Add this launcher to panel" chinese translation.
  Patch by Caius Chance (bug 211569)

* Fri Oct 27 2006 Matthew Barnes <mbarnes@redhat.com> - 2.16.1-2
- Update BuildRequires for evolution-data-server-devel.
- Rebuild against evolution-data-server-1.9.1.

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-5
- Fix scripts according to packaging guidelines

* Wed Sep 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-4.fc6
- Copy translations for "Suspend" menu item from
  gnome-power-manager

* Tue Sep 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-3.fc6
- Fix some directory ownership issues
- Add a %%preun to uninstall gconf schemas
- Require hicolor-icon-theme (#204237)

* Mon Sep 18 2006 Soren Sandmann <sandmann@redhat.com> - 2.16.0-2.fc6
- Add patch to make the pager preference box deal with viewports when compiz
  is running. (Bug 205905).

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Fri Sep  1 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-3.fc6
- Avoid unneeded wakeups in the clock applet (204862)

* Fri Aug 25 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-2.fc6
- Install omf files in the proper location (#201034)

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-1.fc6
- Update to 2.15.92
- Require pkgconfig in the -devel package
- Drop upstreamed patches
- Drop stale code from .spec

* Fri Aug 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-4.fc6
- Make clearing recent files work more than once

* Wed Aug 16 2006 Ray Strode <rstrode@redhat.com> - 2.15.91-3.fc6
- add more complete fix for bug 201439

* Fri Aug 15 2006 Alexander Larsson <alexl@redhat.com> - 2.15.91-2.fc6
- Also use beagle for search actions (#201424)

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.91-1.fc6
- Update to 2.15.91

* Wed Aug  9 2006 Ray Strode <rstrode@redhat.com> - 2.15.90-5
- remove suspend from logout dialog

-* Mon Aug  7 2006 Matthew Barnes <mbarnes@redhat.com> - 2.15.90-4
- Rebuild against evolution-data-server-1.7.91

* Mon Aug  7 2006 Ray Strode <rstrode@redhat.com> - 2.15.90-3
- fix double free in menu editor launcher (bug 201439)

* Fri Aug  4 2006 Ray Strode <rstrode@redhat.com> - 2.15.90-2
- move suspend to menu again
- remove autogenerated panel-typebuiltins.c from move-suspend-to-menu (caolanm)

* Fri Aug  4 2006 Ray Strode <rstrode@redhat.com> - 2.15.90-1
- update to 2.15.90

* Fri Jul 28 2006 Ray Strode <rstrode@redhat.com> - 2.14.2-8
- don't get stuck in infinite recursion loop from previous
  fix.  Patch by Fredric Crozat

* Wed Jul 26 2006 Ray Strode <rstrode@redhat.com> - 2.14.2-7
- don't try to talk to X if the connection is dead (bug 200149)

* Tue Jul 18 2006 Ray Strode <rstrode@redhat.com> - 2.14.2-6
- change "Suspend" to "Hibernate" where appropriate (bug 190791)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.14.2-5.1
- rebuild

* Mon Jun 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-5
- Add a patch to support transparent backgrounds in the
  notification area

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-4
- Update to new gnome-power-manager interface
- Conflict with gnome-power-manager < 2.15.3

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-3
- Add missing BuildRequires

* Mon May 29 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-2
- Update to 2.14.2
- Drop upstreamed patches

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-4
- Make it build in mock

* Fri May 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-3
- Close the about dialog

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1
- Update patches

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- update to 2.14.0

* Tue Feb 28 2006 Karsten Hopp <karsten@redhat.de> 2.13.91-5
- Buildrequires: ORBit2-devel, which, libxml2-python, libX11-devel,
  libXt-devel, gnome-doc-utils, dbus-devel

* Mon Feb 27 2006 Ray Strode <rstrode@redhat.com> - 2.13.91-4
- ignore unknown options (bug 182734)

* Sun Feb 19 2006 Ray Strode <rstrode@redhat.com> - 2.13.91-3
- bring back shutdown menu item

* Wed Feb 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.91-2
- fix up the gnome-power-manager integration patch

* Mon Feb 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.91-1
- update to 2.13.91

* Mon Feb 13 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-3
- use beagle if available for search tool

* Sun Feb 12 2006 Ray Strode <rstrode@redhat.com> - 2.13.90-2
- add first pass at gnome power manager integration

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.90-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.90-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 27 2006 Matthias Clasen <mclasen@redhat.com> 2.13.90-1
- Update to 2.13.90

* Fri Jan 20 2006 Matthias Clasen <mclasen@redhat.com> 2.13.5-2
- Remove "Switch user" button

* Tue Jan 17 2006 Matthias Clasen <mclasen@redhat.com> 2.13.5-1
- Update to 2.13.5

* Thu Jan  5 2006 Matthias Clasen <mclasen@redhat.com> 2.13.4-1
- Update to 2.13.4
- reinstate the desktop-menu-renaming

* Wed Dec 21 2005 Ray Strode <rstrode@redhat.com> 2.13.3-3
- add patch from cvs to fix crasher bug

* Tue Dec 20 2005 Matthias Clasen <mclasen@redhat.com> 2.13.3-2
- Rebuild against new libedataserver

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com> 2.13.3-1
- Update to 2.13.3
- Use sed rather than patch for po files

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec  2 2005 Matthias Clasen <mclasen@redhat.com> 2.13.2-1
- Update to 2.13.2

* Sun Nov 13 2005 John (J5) Palmieri <johnp@redhat.com> 2.12.1-7
- Fix patch to refrence about-fedora.desktop and not fedora-about.desktop

* Sun Nov 13 2005 John (J5) Palmieri <johnp@redhat.com> 2.12.1-6
- add about fedora menu item
- readd gnome-main-menu.png as fedora-logo now installs it to
  the Bluecurve theme

* Sat Nov 12 2005 Florian La Roche <laroche@redhat.com>
- remove gnome-main-menu.png as this is part of fedora-logos

* Tue Nov  1 2005 Ray Strode <rstrode@redhat.com> 2.12.1-4
- rename "Desktop" menu to "System" menu (bug 170812)

* Thu Oct 20 2005 Matthias Clasen  <mclasen@redhat.com> 2.12.1-3
- Add trash applet to the default setup

* Mon Oct 17 2005 Matthias Clasen  <mclasen@redhat.com> 2.12.1-2
- Change the "Cancel" button on the "add to" dialog to "Close"
 
* Thu Oct  6 2005 Matthias Clasen  <mclasen@redhat.com> 2.12.1-1
- Update to 2.12.1
- Update patches

* Fri Sep 30 2005 Mark McLoughlin <markmc@redhat.com> 2.12.0-3
- Remove hacks to add battery applet to default panel configuration
  where ACPI/APM is available (#169621) and GIMLET in CJK locales (#169430) 

* Wed Sep 14 2005 Jeremy Katz <katzj@redhat.com> - 2.12.0-2
- we have mozilla (and e-d-s) on ppc64 now

* Tue Sep  6 2005 Mark McLoughlin <markmc@redhat.com> 2.12.0-1
- Update to 2.12.0

* Mon Aug 22 2005 Mark McLoughlin <markmc@redhat.com> 2.11.92-1
- Update to 2.11.92.

* Tue Aug 16 2005 Mark McLoughlin <markmc@redhat.com> 2.11.91-3
- Rebuild for new cairo

* Wed Aug 10 2005 Mark McLoughlin <markmc@redhat.com> 2.11.91-2
- Fix "Adjust Date & Time" (#165586)

* Wed Aug 10 2005 Mark McLoughlin <markmc@redhat.com> 2.11.91-1
- Update to 2.11.91

* Wed Aug 10 2005 Mark McLoughlin <markmc@redhat.com> 2.11.90-2
- Bump gtk2 req to 2.7.1
- Remove bogus/stale reqs: libxslt-devel, startup-notification-devel,
  gnome-keyring, libpng-devel, fontconfig-devel, libtool, automake,
  autoconf ...

* Thu Aug  4 2005 Matthias Clasen <mclasen@redhat.com> 2.11.90-1
- New upstream version

* Tue Jul 26 2005 Mark McLoughlin <markmc@redhat.com> 2.11.4-3
- Rebuild

* Tue Jul 12 2005 Matthias Clasen <mclasen@redhat.com> 2.11.4-2
- Rebuild

* Fri Jul  8 2005 Matthias Clasen <mclasen@redhat.com> 2.11.4-1
- Update to 2.11.4

* Mon Jun 27 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-11
- Fix "panel doesn't notice new screen size" issue (bug #160439)

* Wed May 11 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-10
- Fix "dialogs pop up under panel dialogs" issue (bug #156425)

* Wed May  4 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-9
- Fix crash with "Recent Documents" menu (bug #156633)

* Mon May  2 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-8
- Update to new OpenOffice.org .desktop file locations in
  openoffice.org-1.9.97-3 (bug #156064)

* Wed Apr 27 2005 Mark McLoughlin <markmc@redhat.com> - 2.10.1-7
- Add patch to clamp the size of the icons on the panel at 48x48. Fixes
  "moved the panel to the side, can't move it back" issue (rh #141743)

* Wed Apr 27 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-6
- Reference the OpenOffice.org Impress .desktop file correctly

* Wed Apr 27 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-5
- Update launcher locations for OpenOffice.org icons

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 2.10.1-4
- silence %%post

* Mon Apr 25 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-3
- Add patch to make Wanda not use non-existent fortune
  command (rh #152948)

* Mon Apr 18 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-2
- Add the battery applet to the panel in %%post if ACPI is
  available (bug #143828) 

* Mon Apr  4 2005 Mark McLoughlin <markmc@redhat.com> 2.10.1-1
- Update to 2.10.1

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 2.10.0-2
- Update the GTK+ theme icon cache on (un)install

* Mon Mar 14 2005 Matthias Clasen <mclasen@redhat.com> 2.10.0-1
- Update to 2.10.0
- Bump BuildRequires for libwnck
- Update patches

* Wed Mar  4 2005 Mark McLoughlin <markmc@redhat.com> 2.9.91-4
- Fix a BuildRequires

* Wed Mar  2 2005 Mark McLoughlin <markmc@redhat.com> 2.9.91-3
- Rebuild with gcc4

* Thu Feb 10 2005 Mark McLoughlin <markmc@redhat.com> - 2.9.91-2
- Require gnome-desktop 2.9.91

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.91-1
- Update to 2.9.91

* Mon Feb  7 2005 Mark McLoughlin <markmc@redhat.com> - 2.9.90-4
- Don't use --makefile-install-rule to install .entries files (#147112)

* Fri Feb  4 2005 Mark McLoughlin <markmc@redhat.com> - 2.9.90-3
- Update schemas list (#147112)

* Thu Feb  3 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.90-2
- Look for vendor-prefixed .desktop files

* Mon Jan 31 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.90
- Update to 2.9.90

* Fri Jan 28 2005 Florian La Roche <laroche@redhat.com>
- rebuild

* Thu Jan 27 2005 Jeremy Katz <katzj@redhat.com> - 2.8.1-8
- really disable e-d-s support

* Wed Jan 26 2005 David Malcolm <dmalcolm@redhat.com> - 2.8.1-7
- Make the evolution-data-server dependency optional at packaging time.
- Disable it for now to ease transition to Evolution 2.2 (bug #146283)

* Fri Nov 26 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.1-6
- Add patch to fix launcher animation artifact (bug #136938)

* Fri Nov 12 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.1-5
- Use /apps/panel for configuration so that homedir sharing with
  previous versions works reasonably well. This is the location
  upstream is using from GNOME 2.10 onwards.
- Install old pager.schemas and tasklist.schemas so that
  old configurations which reference the old schema names
  continue to work

* Mon Nov  1 2004 Mark McLoughlin <markmc@redhat.com> - 2.8.1-4
- Fix use-correct-applications-uri patch to not crash on
  ia64 - fix from Dave Malcolm (#136908)

* Mon Oct 18 2004  <jrb@redhat.com> - 2.8.1-3
- change redhat-web.desktop and redhat-email.desktop to be in /usr/share instead of using the menu path

* Fri Oct 15 2004 Matthias Clasen <mclasen@redhat.com>
- Make dropping non-ASCII uris work.  (#135874)

* Tue Oct 12 2004 Mark McLoughlin <markmc@redhat.com>
- Update to 2.8.1
- Change the default no. pager rows back to 1
- Add a new tamil translation

* Thu Oct  7 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-3
- Add the Input Method Switcher applet in certain locales (#134659)

* Fri Oct  1 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-2
- New panel layout from Bryan and Seth

* Wed Sep 29 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0.1-1
- Update to 2.8.0.1

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-2
- Remove the print launcher from the default setup - it was removed
  from the desktop-printing package a while ago 

* Tue Sep 21 2004 Mark McLoughlin <markmc@redhat.com> 2.8.0-1
- Update to 2.8.0

* Tue Aug 31 2004 Mark McLoughlin <markmc@redhat.com> 2.7.92.1-1
- Update to 2.7.92.1

* Mon Aug 30 2004 Mark McLoughlin <markmc@redhat.com> 2.7.92-1
- Update to 2.7.92

* Wed Aug 25 2004 Mark McLoughlin <markmc@redhat.com> 2.7.91.1-2
- Pipe gconftool stdout to /dev/null - fixes bug #130506

* Thu Aug 19 2004 Mark McLoughlin <markmc@redhat.com> 2.7.91.1-1
- Update to 2.7.91.1

* Wed Aug 18 2004 Mark McLoughlin <markmc@redhat.com> 2.7.91-1
- Update to 2.7.91

* Tue Aug 10 2004 Mark McLoughlin <markmc@redhat.com> - 2.7.90-1
- Update to 2.7.90 and remove a bunch of patches

* Mon Aug  2 2004 David Malcolm <dmalcolm@redhat.com> - 2.6.0-11
- added dependency on evolution-data-server and rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 19 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-9
- Install battstat on the default panel on ppc too

* Mon Apr 19 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-8
- Only put the battstat applet on the default panel on ix86 (i.e. the
  platforms where apmd is built) - bug #121098

* Thu Apr 15 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-7
- Fix typo with laptop battery detection scriptlet - bug #120921

* Thu Apr 15 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-6
- Overwrite panel-compatibility.schemas with
  redhat-panel-backwards-compat-config.schemas and install that so
  it doesn't seem like we've forgotten panel-compatibility.schemas

* Thu Apr  8 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-5
- Fix problem with apm detection in %%post on machines whose
  APM bios doesn't have battery lifetime support

* Wed Apr  7 2004 Mark McLoughlin <markmc@redhat.com> - 2.6.0-4
- Add patch to make the applications list in the run dialog work
  correctly with the new vfs menu module. Bug #118305.

* Mon Apr  5 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-3
- Fix "vailed to parse hour_format" warnings on install (bug #119956)

* Fri Apr  5 2004 Mark McLoughlin <markmc@redhat.com> - 2.6.0-2
- Add patches to fixup how we install the default setup
- Require GConf2-2.6.0-2 for gconftool-2 --load fix

* Wed Mar 31 2004 Mark McLoughlin <markmc@redhat.com> 2.6.0-1
- Update to 2.6.0

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com>
- Update to 2.5.92

* Wed Mar 03 2004 Mark McLoughlin <markmc@redhat.com> 2.5.91-2
- Use the main menu icon in the menu bar (#100407)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Mark McLoughlin <markmc@redhat.com> 2.5.91-1
- Update to 2.5.91
- Split off a -devel package (#108618)
- Add a scrollkeeper PreReq and scrollkeeper, intltool and
  libpng-devel BuildRequires. (#110928, Maxim Dzumanenko)

* Fri Feb 27 2004 Mark McLoughlin <markmc@redhat.com> 2.5.90-1
- Update to 2.5.90
- Resolve conflicts with the lockf patch and re-work slightly

* Thu Feb 19 2004 Jeremy Katz <katzj@redhat.com> - 2.5.3.1-6
- and again for real this time

* Wed Feb 18 2004 Jeremy Katz <katzj@redhat.com> - 2.5.3.1-5
- rebuild without e-d-s

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 06 2004 Dan Williams <dcbw@redhat.com> 2.5.3.1-3
- Add in file locking retries for egg-recent-model stuff, as with
   gedit.  Makes gnome-panel and other apps like gedit not fight
   for recent files list on NFS home directories

* Tue Jan 27 2004 Alexander Larsson <alexl@redhat.com> 2.5.3.1-2
- Add evolution-data-server dependency and rebuild

* Thu Oct  9 2003 Owen Taylor <otaylor@redhat.com> 2.4.0-2
- Look up the largest size available when picking default images for 
  panel stock icons (#106673)

* Thu Sep  4 2003 Alexander Larsson <alexl@redhat.com> 2.3.90-1
- update to 2.3.90
- Add backwards compat panel config schemas

* Wed Aug 27 2003 Alexander Larsson <alexl@redhat.com> 2.3.7-1
- update to 2.3.7
- patch the right icon for the main menu (#102672)
- PreReq a new gconf (#102530)

* Mon Aug 25 2003 Alexander Larsson <alexl@redhat.com> 2.3.6.2-4
- Don't lock all objects on panel
- use "make DESTDIR=... install" so gconf rules are right

* Mon Aug 18 2003 Alexander Larsson <alexl@redhat.com> 2.3.6.2-3
- Update the default panel setup handling to the new way

* Thu Aug 14 2003 Jonathan Blandford <jrb@redhat.com> 2.3.6.2-1
- remove the right .la files.

* Thu Aug 14 2003 Alexander Larsson <alexl@redhat.com> 2.3.6.2-1
- update for gnome 2.3

* Tue Jul 29 2003 Havoc Pennington <hp@redhat.com> 2.2.2.1-3
- disable gtk doc

* Mon Jul 28 2003 Havoc Pennington <hp@redhat.com> 2.2.2.1-3
- rebuild

* Wed Jul  9 2003 Alexander Larsson <alexl@redhat.com> 2.2.2.1-2
- Fix redhat menu icon

* Mon Jul  7 2003 Havoc Pennington <hp@redhat.com> 2.2.2.1-1
- 2.2.2.1
- remove memleaks patch, now upstream
- remove applet-sm patch now upstream
- remove "null" patch, now upstream
- remove recent-monitor patch now upstream
- remove notification area crash fix, now upstream

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com> 2.2.0.1-8
- Rebuild with an updated libtool to fix #84742

* Thu Feb 20 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-6
- fix memleaks, #84489 #84467
- use icon theme for button widgets instead of stock ID #82301

* Fri Feb 14 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-5
- disable session management for all applets

* Tue Feb 11 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-4
- fix #83683 for real, very embarassing bug in the end

* Tue Feb 11 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-3
- add assertions to try to narrow down #83683 more

* Tue Feb 11 2003 Tim Waugh <twaugh@redhat.com> 2.2.0.1-2
- Fix notification area crash (bug #83683).

* Wed Feb  5 2003 Havoc Pennington <hp@redhat.com> 2.2.0.1-1
- 2.2.0.1

* Mon Feb  3 2003 Matt Wilson <msw@redhat.com> 2.2.0-2
- added gnome-panel-2.1.90.1-null.patch to avoid segv on 64 bit platforms
  #82978

* Mon Feb  3 2003 Alexander Larsson <alexl@redhat.com> 2.2.0-1
- Update to 2.2.0
- Add patch to disable monitoring in recent-files, since it made you not able to unmount cds.

* Thu Jan 30 2003 Matt Wilson <msw@redhat.com> 2.1.90.1-6
- disable optimizations on x86_64 to work around gcc bug

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Jonathan Blandford <jrb@redhat.com>
- put the control-center second

* Sat Jan 11 2003 Havoc Pennington <hp@redhat.com>
- fix the extra separator left when we lack screenshot menuitem

* Fri Jan 10 2003 Havoc Pennington <hp@redhat.com>
- fix the clock

* Thu Jan  9 2003 Havoc Pennington <hp@redhat.com>
- remove enhanced-errors patch now upstream
- change how we're doing the laptop-specific config to avoid cut-and-paste
- update clock-addons patch
- remove hardcoded change to default panel icon size, we'll put it in bluecurve
  theme.
- run xscreensaver fortune instead of just "fortune" from the fish
- add printer icon to panel

* Wed Jan  8 2003 Havoc Pennington <hp@redhat.com>
- 2.1.90.1

* Mon Dec 16 2002 Tim Powers <timp@redhat.com> 2.1.4-4
- rebuild

* Mon Dec 16 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Sat Dec 14 2002 Havoc Pennington <hp@redhat.com>
- require gnome-desktop 2.1.4
- include datadir/fish

* Fri Dec 13 2002 Havoc Pennington <hp@redhat.com>
- 2.1.4

* Mon Dec  2 2002 Havoc Pennington <hp@redhat.com>
- 2.1.3
- build req startup-notification-devel

* Wed Nov 13 2002 Havoc Pennington <hp@redhat.com>
- 2.1.2
- system tray is now in the main gnome-panel package

* Wed Oct 23 2002 Havoc Pennington <hp@redhat.com>
- 2.0.10
- remove memleaks-and-clock-format patch, should be upstream
- remove WIN_POS_MOUSE purge, done upstream

* Mon Oct 14 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix postun script

* Tue Oct  8 2002 Havoc Pennington <hp@redhat.com>
- 2.0.9 with menu edit stuff
- system-tray-applet 0.15 that doesn't crash all the time
- merge/remove patches as appropriate

* Wed Aug 28 2002 Owen Taylor <otaylor@redhat.com>
- Fix problem with "hold down print screen" (71432)

* Tue Aug 27 2002 Jonathan Blandford <jrb@redhat.com>
- panel-properties OnlyShowIn=GNOME;
- somehow the po file got screwed up.  Works now
- update po files

* Sun Aug 25 2002 Havoc Pennington <hp@redhat.com>
- fix from #71762 for clock applet popdown key
- no WIN_POS_MOUSE fixes #72167
- fix for #72540 from George

* Wed Aug 21 2002 Havoc Pennington <hp@redhat.com>
- system tray applet 0.11 with a small memleak fix and a couple translations

* Thu Aug 15 2002 Jonathan Blandford <jrb@redhat.com>
- menu tweaks

* Wed Aug 14 2002 Tim Powers <timp@redhat.com>
- bump release

* Wed Aug 14 2002 Preston Brown <pbrown@redhat.com>
- put battery applet on panel for laptops (#67296)

* Mon Aug 12 2002 Havoc Pennington <hp@redhat.com>
- 2.0.6 final from gnome 2.0.1
- remove gnome-panel-screenshot patch now upstream

* Thu Aug  8 2002 Jonathan Blandford <jrb@redhat.com>
- new system-tray-applet version
- Fix gnome-panel-screenshot

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- 2.0.4
- replace gnome-logo-icon-transparent.png with redhat-main-menu.png
  for the foot menu

* Fri Aug  2 2002 Havoc Pennington <hp@redhat.com>
- fix desktop (logout/lock) menu item location
  in Alt+F1 and in new menu applets
- remove Screenshot... menu item

* Fri Aug  2 2002 Havoc Pennington <hp@redhat.com>
- move around default applets, remove some of them
- system tray 0.9
- change default menu flags
- blow unpackaged files out of build root

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com>
- 2.0.3
- own libexecdir stuff

* Thu Jul 25 2002 Havoc Pennington <hp@redhat.com>
- new system tray that's prettier and doesn't clip the icon

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- system tray 0.7 that doesn't crash on startup
- get Mozilla desktop file right so we get web browser launcher

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- system tray 0.6 with server file fixed (work dammit)

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- tweak applet positions but I think it's just broken
- system tray 0.5 moved back to libdir not libexecdir

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- remove ltmain.sh hack
- new system-tray-applet that works

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- put office suite stuff on the panel

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- 2.0.2.90 cvs snap

* Wed Jul 10 2002 Havoc Pennington <hp@redhat.com>
- update the clock patch to be a little smarter in a couple ways

* Thu Jun 27 2002 Owen Taylor <otaylor@redhat.com>
- Fix problem where system tray applet was being looked for in /unst
- Fix a crash in the system tray applet

* Wed Jun 26 2002 Owen Taylor <otaylor@redhat.com>
- Fix typo in the pt_BR translation that was causing GConf problems

* Mon Jun 24 2002 Havoc Pennington <hp@redhat.com>
- add the system tray applet
- add system tray applet by default
- add more launcher by default

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Havoc Pennington <hp@redhat.com>
- use correct gettext package name, and add check for missing translations

* Mon Jun 17 2002 Havoc Pennington <hp@redhat.com>
- add the calendar and configuration patch 

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 2.0.0
- add control center desktop file to file list
- add gnome-panelrc to file list
- try fixing panel size (blind, no text box at home)

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- updates to default configuration

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- fix schemas installation

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- unset old panel schemas when installing new ones
- put in a broken panel config to see errors about
- add a patch to give some decent error messages about what's wrong
  with the default panel config

* Sun Jun 09 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Sun Jun  9 2002 Havoc Pennington <hp@redhat.com>
- don't provide/obsolete gnome-core

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 1.5.24
- ldconfig

* Mon Jun 03 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Fri May 31 2002 Havoc Pennington <hp@redhat.com>
- 1.5.23

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- 1.5.22
- provide gnome-core
- add a bunch of extra build requires so build system 
  won't get confused

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 1.5.19

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- add the keep-libtool-from-relinking hack so 
  we get the gen util applet

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- obsoletes gnome-core-devel
- include libdir/*.so

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- get libpanel-applet in the package

* Tue Apr 16 2002 Havoc Pennington <hp@redhat.com>
- Initial build.


